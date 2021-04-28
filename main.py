# globals
MIN_REQUEST = 0
MAX_REQUEST = 199
IORequests = []
head_ptr = 0


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
    print("\nPick an algorithm's number:")
    print("1- FCFS\n2- SSTF\n3- SCAN\n4- C-SCAN\n5- LOOK\n6- C-LOOK\n7- Newly optimized algorithm")
    
    alg = input("> ")


if __name__ == '__main__':
    main()
