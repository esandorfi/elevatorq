"""
Dispatch the Queues
"""

import utils
import look

if __name__ == "__main__":
    utils.main_start_django()  # quick test purpose

from elevatorq.models import (
    PressBtnQ,
    BuildingElevator,
    ElevatorQ,
    ElevatorStatus,
    PositionDirection,
)


class ResetDB:
    """
    reset the elevatorq db for testing purpose
    """

    def enable_elevators_at_lobby_floor(self):
        pass


class DispatchEQ:
    """
    dispatch pressbtn actions to elevators
    use as :
    DispatchEQ().main() # to process all
    DispatchEQ().main('0UP30') # to process one action
    """

    version = 1

    def __init__(self):
        print("DispatchQ v{self.version}")
        # _v1.1 -> add filter(status=ElevatorStatus.ENABLED)
        #       -> raise if no elevators available
        self.elevators = BuildingElevator.objects.all()

    def main(self, btn_code: str = ""):
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
            direction=PositionDirection.IDLE,
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

    # Request array
    arr = [176, 79, 34, 60, 92, 11, 41, 114]
    head = 50

    direction = "up"

    print("Initial position of head:", head)

    look.LOOK(arr, head, direction)

    # This code is contributed by rag2127
