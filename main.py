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


if __name__ == '__main__':
    main()
