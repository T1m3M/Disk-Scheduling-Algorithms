# globals
MIN_REQUEST = 0
MAX_REQUEST = 199
IORequests = []
head_ptr = 0

# outputs
sequence = []
total_head_mov = 0


def fcfs():
    global sequence, total_head_mov

    sequence.append(head_ptr)
    for i in range(len(IORequests)):
        sequence.append(IORequests[i])
        total_head_mov += abs(IORequests[i] - sequence[i])


def sstf():
    global sequence, total_head_mov
    return


def scan():
    global sequence, total_head_mov
    return


def c_scan():
    global sequence, total_head_mov
    return


def look():
    global sequence, total_head_mov
    return


def c_look():
    global sequence, total_head_mov
    return


def newly_opt_alg():
    global sequence, total_head_mov
    return


def main():
    global IORequests, head_ptr

    # User's input
    queue = input("I/O requests: ")
    for request in queue.split():
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


if __name__ == '__main__':
    main()
