import matplotlib.pyplot as plt
import numpy as np

# globals
MIN_REQUEST = 0
MAX_REQUEST = 199
IORequests = []
head_ptr = 0  # 53

# outputs
sequence = []
total_head_mov = 0


def calc_head_mov():
    total = 0
    for i in range(1, len(sequence)):
        total += abs(sequence[i] - sequence[i - 1])
    return total


def fcfs():
    global sequence, total_head_mov

    sequence.append(head_ptr)
    for i in range(len(IORequests)):
        sequence.append(IORequests[i])

    total_head_mov = calc_head_mov()


def sstf():
    global sequence, total_head_mov

    sequence.append(head_ptr)
    curr = head_ptr
    finished_requests = [False for _ in IORequests]

    # While there's at least a waiting request
    while False in finished_requests:
        diff = [abs(curr - request) for request in IORequests]
        waiting_requests_diff = []

        # Getting only the unfinished requests
        for i in range(len(diff)):
            if not finished_requests[i]:
                waiting_requests_diff.append(diff[i])

        # Getting the minimum cost, appending the request and mark as finished
        for i in range(len(diff)):
            # If more than one minimum get the unfinished request
            if not finished_requests[i]:
                nearest_request_index = diff.index(min(waiting_requests_diff))
            else:
                diff[i] = max(diff)

        curr = IORequests[nearest_request_index]
        sequence.append(curr)
        finished_requests[nearest_request_index] = True

    total_head_mov = calc_head_mov()


def scan():
    global sequence, total_head_mov
    left = []
    right = []

    left.append(head_ptr)
    left.append(0)
    for i in range(0, len(IORequests)):

        if IORequests[i] < head_ptr:
            left.append(IORequests[i])
        else:
            right.append(IORequests[i])

    # we move from head ptr to left then to right
    left.sort()
    left.reverse()

    right.sort()

    for i in range(0, len(left)):
        sequence.append(left[i])

    for i in range(0, len(right)):
        sequence.append(right[i])

    total_head_mov = calc_head_mov()


def c_scan():
    global sequence, total_head_mov
    left = []
    right = [head_ptr]

    left.append(0)
    right.append(199)
    for i in range(0, len(IORequests)):

        if IORequests[i] > head_ptr:
            right.append(IORequests[i])
        else:
            left.append(IORequests[i])

    # we move from head ptr to right then to left (last point in right = first point in left) .
    left.sort()

    right.sort()

    for i in range(0, len(right)):
        sequence.append(right[i])

    for i in range(0, len(left)):
        sequence.append(left[i])

    total_head_mov = calc_head_mov()


def look():
    global sequence, total_head_mov
    left = []
    right = []

    left.append(head_ptr)
    for i in range(0, len(IORequests)):

        if IORequests[i] < head_ptr:
            left.append(IORequests[i])

        else:
            right.append(IORequests[i])

    # we move from head ptr to left then to right
    left.sort()
    left.reverse()

    right.sort()

    for i in range(0, len(left)):
        sequence.append(left[i])

    for i in range(0, len(right)):
        sequence.append(right[i])

    total_head_mov = calc_head_mov()


def c_look():
    global sequence, total_head_mov

    start = 0
    temp = 0
    IORequests.append(head_ptr)

    # Sorting the array
    for i in range(0, len(IORequests)):
        for j in range(i + 1, len(IORequests)):
            if IORequests[i] > IORequests[j]:
                temp = IORequests[i]
                IORequests[i] = IORequests[j]
                IORequests[j] = temp

    for i in range(1, len(IORequests)):
        if IORequests[i] == head_ptr:
            start = i

    for i in range(start, len(IORequests)):
        sequence.append(IORequests[i])

    for i in range(0, start):
        sequence.append(IORequests[i])

    total_head_mov = calc_head_mov()


def newly_opt_alg():
    global sequence, total_head_mov

    temp = 0
    sequence.append(head_ptr)

    if head_ptr != 0:
        IORequests.append(0)

    # Sorting the array
    for i in range(0, len(IORequests)):
        for j in range(i + 1, len(IORequests)):
            if IORequests[i] > IORequests[j]:
                temp = IORequests[i]
                IORequests[i] = IORequests[j]
                IORequests[j] = temp

    for i in range(0, len(IORequests)):
        sequence.append(IORequests[i])

    total_head_mov = calc_head_mov()


def plot_graph():
    y_axis = []

    # Initializing the Y-axis
    for i in range(len(sequence) - 1, -1, -1):
        y_axis.append(i)

    # Plotting the sequence
    plt.plot(sequence, y_axis)
    plt.xlim(MIN_REQUEST, MAX_REQUEST)
    plt.xticks(np.arange(MIN_REQUEST, MAX_REQUEST, 20))

    # Placing the request number in annotations
    fig, ax = plt.subplots()
    ax.plot(sequence, y_axis, 'bo-')
    ax.set_xlabel("I/O requests")

    for X, Y in zip(sequence, y_axis):
        ax.annotate('{}'.format(X), xy=(X, Y), xytext=(-5, 5), ha='right', textcoords='offset points')

    plt.show()


def main():
    global IORequests, head_ptr, sequence, total_head_mov

    # User's input
    # I/O requests: 98, 183, 37, 122, 14, 124, 65, 67
    # Head pointer: 53
    queue = input("I/O requests: ")
    for request in queue.split(", "):
        if int(request) < MIN_REQUEST or int(request) > MAX_REQUEST:
            print(f"The I/O requests must be between {MIN_REQUEST}-{MAX_REQUEST}")
            exit()
        else:
            IORequests.append(int(request))
    head_ptr = int(input("Head pointer: "))

    # Picking an algorithm
    while True:
        print("\nPick an algorithm's number:")
        print("1- FCFS\n2- SSTF\n3- SCAN\n4- C-SCAN\n5- LOOK\n6- C-LOOK\n7- Newly optimized algorithm\n0- Exit")

        # Handling non-numeric options
        try:
            op = int(input("> "))
        except ValueError:
            print("Unknown option")
            continue

        # Switching to the correct option
        if op == 0:
            print("Exiting..")
            exit()

        elif op == 1:
            fcfs()

        elif op == 2:
            sstf()

        elif op == 3:
            scan()

        elif op == 4:
            c_scan()

        elif op == 5:
            look()

        elif op == 6:
            c_look()

        elif op == 7:
            newly_opt_alg()

        else:
            print("Unknown option")
            continue

        # Output
        print(f"Sequence: {', '.join(str(x) for x in sequence)}")
        print(f"Total head movement: {total_head_mov}")

        plot_graph()

        # reset the output variables
        sequence.clear()
        total_head_mov = 0


if __name__ == '__main__':
    main()
