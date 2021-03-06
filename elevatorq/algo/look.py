# Python3 program to demonstrate
# LOOK Disk Scheduling algorithm
# based on source :
# https://www.geeksforgeeks.org/look-disk-scheduling-algorithm/

size = 8
disk_size = 200


def LOOK(arr, head, direction):

    seek_count = 0
    distance = 0
    cur_track = 0

    left = []
    right = []

    seek_sequence = []

    # Appending values which are
    # currently at left and right
    # direction from the head.
    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Sorting left and right vectors
    # for servicing tracks in the
    # correct sequence.
    left.sort()
    right.sort()

    # Run the while loop two times.
    # one by one scanning right
    # and left side of the head
    run = 2
    while run:
        if direction == "left" or direction == "down":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]

                # Appending current track to
                # seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now the new head
                head = cur_track

            # Reversing the direction
            direction = "right"

        elif direction == "right" or direction == "up":
            for i in range(len(right)):
                cur_track = right[i]

                # Appending current track to
                # seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now new head
                head = cur_track

            # Reversing the direction
            direction = "left"

        run -= 1

    print("Total number of seek operations =", seek_count)
    print("Seek sequence length =", len(seek_sequence))
    print(f"Seek Sequence is {seek_sequence}")

    # for i in range(len(seek_sequence)):
    #     print(seek_sequence[i])

    return seek_sequence


#
# LOOK FOR ELEVATOR
#


def LOOKELEVATOR(arr, head, direction):

    seek_count = 0
    distance = 0
    cur_track = 0

    left = []
    right = []

    seek_sequence = []

    # Appending values which are
    # currently at left and right
    # direction from the head.
    len_arr = len(arr)
    for i in range(len_arr):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])
        if i > 1 and arr[i] == head:
            left.append(arr[i])

    # Sorting left and right vectors
    # for servicing tracks in the
    # correct sequence.
    left.sort()
    if len(left):
        left = list(set(left))
    right.sort()
    if len(right):
        right = list(set(right))

    # print(f"HEAD {head} DIRECTION {direction} LEFT {left} RIGHT {right}")

    # Run the while loop two times.
    # one by one scanning right
    # and left side of the head
    run = 2
    while run:
        if direction == "left" or direction == "DOWN":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]

                # Appending current track to
                # seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now the new head
                head = cur_track

            # Reversing the direction
            direction = "right"

        elif direction == "right" or direction == "UP":
            for i in range(len(right)):
                cur_track = right[i]

                # Appending current track to
                # seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now new head
                head = cur_track

            # Reversing the direction
            direction = "left"

        run -= 1

    # print("Total number of seek operations =", seek_count)
    # print("Seek sequence length =", len(seek_sequence))
    # print(f"Seek Sequence is {seek_sequence}")

    # for i in range(len(seek_sequence)):
    #     print(seek_sequence[i])

    return (seek_sequence, seek_count)


#
# test mode
#

if __name__ == "__main__":

    # Request array
    arr = [176, 79, 34, 60, 92, 11, 41, 114]
    head = 50

    direction = "up"

    print("Initial position of head:", head)

    LOOK(arr, head, direction)
