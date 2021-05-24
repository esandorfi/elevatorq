"""
Dispatch the Queues and set database records

Support direct execution for test purpose, 
in that case, load django env + VERBOSE = True
>> python eq.py
"""

from typing import Optional
import sys
import random

VERBOSE = False  # print console verbose mode
if __name__ == "__main__":
    import utils

    utils.main_start_django()
    VERBOSE = True


# load elevatorq data model
from elevatorq.models import PressBtnQ, BuildingElevator, ElevatorQ
from elevatorq import appsettings


#
# HELPER FOR PRINT OUTPUT
#


def verbose_headline(h, c=""):
    """
    print helper to show headline with
    a string,
    >> verbose_headline('my headline')
    a function name,
    >> verbose_headline(sys._getframe().f_code.co_name)
    a function name + classname:
    >> verbose_headline(sys._getframe().f_code.co_name, self.__class__.__name__)

    default : VERBOSE=True with in the __name__ == '__main__'
    future : add toggle global verbose from settings

    """
    if not VERBOSE:
        return
    elif c:
        print("{:.^50}{}".format(h, c))
    else:
        print("{:.^50}".format(h))


#
# FLAGS SYSTEM
#


class FlagsSystem:
    """
    Manage records attributs in ElevatorQ Database
    """

    def enable_elevators_at_lobby_floor(self):
        """
        set all buildingelevator to ENABLED, IDLE, FLOOR 0,
        flush pressbtnq end elevatorq
        """
        BuildingElevator.objects.all().update(
            status=appsettings.ElevatorStatus.ENABLED,
            current_direction=appsettings.PositionDirection.IDLE,
            current_floor=appsettings.EQ_DEFAULT_LOBBY_FLOOR,
        )

    def reset_pressbtnq(self):
        PressBtnQ.objects.all().delete()

    def reset_elevatorq(self):
        """in real world, we should insure the elevators go back to lobby"""
        ElevatorQ.objects.all().delete()


#
# RESET DATABASE FOR TEST / DEMO MODE
#


class ResetDatabase(FlagsSystem):
    """
    Reset database for demonstration and testing purpose
    Inherit of 'Flags' database definition object for ElevatorQ
    """

    def reset(self):
        """do the reset"""
        self.reset_pressbtnq()
        self.reset_elevatorq()
        self.enable_elevators_at_lobby_floor()

    def fill_elevator_q(self, elevator_name: Optional[str] = ""):
        """insert fake values for elevators q"""
        verbose_headline(sys._getframe().f_code.co_name, self.__class__.__name__)
        #
        qs = BuildingElevator.objects.all()
        if elevator_name:
            qs = qs.filter(name=elevator_name)
            if not qs.exists():
                raise ValueError(
                    f"No elevator {elevator_name} found in the building elevators settings."
                )

        try:
            nb = len(qs)
            print(f"Find {nb} elevator(s)")
            for q in qs.iterator(chunk_size=100):

                # get the data from orm and affect to variables
                # so we continue in orm free algorithm
                range_min_floor = q.range_min_floor
                range_max_floor = q.range_max_floor
                lobby_floor = q.lobby_floor

                # do not include lobby floor in random
                if lobby_floor == range_min_floor:
                    range_min_floor += 1
                # get a random floor
                start_floor = random.randint(range_min_floor, range_max_floor)
                # get a random direction
                d = random.randint(0, 1)
                direction = (
                    appsettings.PositionDirection.DOWN
                    if d
                    else appsettings.PositionDirection.UP
                )
                if direction == appsettings.PositionDirection.DOWN:
                    # if going down, assume we go the lobby
                    final_floor = lobby_floor
                else:
                    # if going up, assume we found the final floor and we coming from the lobby
                    final_floor = start_floor
                    start_floor = 0  # lobby_floor

                print(
                    f"start_floor {start_floor} direction {direction} final_floor {final_floor}"
                )

                # add to the queue the steps with a direction
                # start_floor has an IDLE direction
                o1 = ElevatorQ.objects.create(
                    elevator=q,
                    floor=start_floor,
                    direction=appsettings.PositionDirection.IDLE,
                )
                print(f"{o1} created floor {start_floor}")
                o2 = ElevatorQ.objects.create(
                    elevator=q, direction=direction, floor=final_floor
                )

                print(f"{o2} created foor {final_floor}")

        except Exception as e:
            print(f"Error {e}")

    def display_elevatorq(self):
        """display data for test purpose"""
        verbose_headline(sys._getframe().f_code.co_name, self.__class__.__name__)
        #
        qs = ElevatorQ.objects.all()
        for q in qs.iterator(chunk_size=100):
            print(f"{q.elevator} -> {q}")


#
# DISPATCH SYSTEM
#


class DispatchSystem:
    """
    dispatch pressbtn actions to elevators
    use as :
    DispatchEQ().main() # to process all
    DispatchEQ().main('0UP30') # to process one action
    """

    version = 1

    def __init__(self):
        self.elevators = BuildingElevator.objects.all()

    def main(self, btn_code: str = ""):
        verbose_headline(sys._getframe().f_code.co_name, self.__class__.__name__)
        #
        """main function"""
        if not btn_code:
            self.scan_pressbtnq()
        else:
            self.add_btn_code(btn_code)
            # return elevator name and waiting indicator
        return

    def add_btn_code(self, btn_code: str):
        """add another action to the pressbtn table,
        validate regex"""
        # *TODO* Add a pressbtn manually
        pass

    def scan_pressbtnq(self):
        """get all pressbtn not affected to an elevator"""
        qs = PressBtnQ.objects.filter(elevator__isnull=True)
        for pressbtn in qs:
            print(f"scan_pressbtnq : find {pressbtn}")
            self.dispatch_elevator(pressbtn)

    def dispatch_elevator(self, pressbtn: PressBtnQ):
        """the algorithm

        DISPATCH :
        1) direct availability - check for each build elevators

            a) first available idle at start floor and correct direction -> affect

        2) get each elevators q

            a) find the less waiting time -> affect
            b) smart and try to insert -> affect

        WAITING INDICATOR:
        for elevator, return waiting time to open from pressbtn floor

        """

        for elev in self.elevators:

            # find first elevators at the same floor first
            # *TODO* we need to check which one is better to affect
            if elev.current_floor == pressbtn.start_floor:
                self.affect_elevator(pressbtn, elev)
                break

    def calculate_waiting_indicator(
        self, pressbtn: PressBtnQ, elevator: BuildingElevator
    ) -> str:
        """return waiting time to open from pressbtn floor"""
        # *TODO* we need to calculate the number of move of the elevator
        return "not implemented yet"

    def affect_elevator(self, pressbtn: PressBtnQ, elevator: BuildingElevator):
        """affect elevator to a pressbtn,
        add to the elevator q the action"""

        # add new elevatorq record /
        ElevatorQ.objects.create(
            elevator=elevator, floor=pressbtn.start_floor, direction=pressbtn.direction
        )
        ElevatorQ.objects.create(
            elevator=elevator,
            floor=pressbtn.final_floor,
            direction=appsettings.PositionDirection.IDLE,
        )

        # update pressbtnq record
        pressbtn.elevator = elevator
        pressbtn.waiting_indicator = self.calculate_waiting_indicator(
            pressbtn, elevator
        )
        pressbtn.save()


#
# test mode
#

if __name__ == "__main__":
    """
    while build our first program, we think about the test cases for pytest
    """

    """ RESET """

    resetdb = ResetDatabase()

    # test_wrong_elevator_name()
    # resetdb.fill_elevator_q(elevator_name="toto")

    # test_correct_elevator_name()
    # resetdb.fill_elevator_q(elevator_name="A")

    resetdb.reset()
    resetdb.fill_elevator_q()
    resetdb.display_elevatorq()

    """ DISPATCH """

    DispatchSystem().main()
