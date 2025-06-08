from queue import Queue

# Initialize a global queue to hold incoming requests
request_queue = Queue()
request_id = 1  # Global counter to assign unique IDs to requests


def generate_request():
    """
    Generate a new request and add it to the queue.

    Each request is assigned a unique identifier in the format 'Request-{ID}'.
    """
    global request_id
    request = f"Request-{request_id}"
    request_queue.put(request)
    print(f"Added: {request}")
    request_id += 1


def process_request():
    """
    Process the next request in the queue.

    If the queue is not empty, the request is removed and processed.
    Otherwise, a message is printed indicating the queue is empty.
    """
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processed: {request}")
    else:
        print("Queue is empty.")


def main():
    """
    Main interactive loop of the program.

    Displays a menu with three options:
    1. Generate a new request
    2. Process the next request
    3. Exit the program
    """
    while True:
        print("\nMenu:")
        print("1. Create new request")
        print("2. Process request")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            generate_request()
        elif choice == '2':
            process_request()
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
