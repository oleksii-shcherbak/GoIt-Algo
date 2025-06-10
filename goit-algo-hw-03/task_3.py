import time


# Set animation delay (in seconds).
# Adjust this value to control the speed of the animation.
# Use 0 for instant transitions (no animation).
ANIMATION_DELAY = 0.5

step_counter = 0  # Global counter for number of steps

def hanoi(n, source, target, auxiliary, state, total_height):
    """
    Recursively solve the Tower of Hanoi.
    Moves n disks from source to target using auxiliary as helper rod.
    """
    if n == 1:
        move_disk(source, target, state, total_height)
    else:
        hanoi(n - 1, source, auxiliary, target, state, total_height)
        move_disk(source, target, state, total_height)
        hanoi(n - 1, auxiliary, target, source, state, total_height)

def move_disk(src, dst, state, total_height):
    """
    Move a single disk from src rod to dst rod, update state and display it.
    """
    global step_counter
    disk = state[src].pop()
    state[dst].append(disk)
    step_counter += 1
    print(f"\nStep {step_counter}: Move disk {disk} from {src} to {dst}")
    print_state(state, total_height)
    time.sleep(ANIMATION_DELAY)

def print_state(state, total_height):
    """
    Print the visual representation of the rods and disks.
    Disks are displayed using proportional width.
    """
    max_disk = max((disk for rod in state.values() for disk in rod), default=1)
    tower_width = 2 * max_disk - 1
    spacing = 4  # Space between rods

    # Build visual representation for each rod
    visual = {
        rod: [draw_disk(d) for d in state[rod]]
        for rod in "ABC"
    }

    # Print from top to bottom
    for row in range(total_height - 1, -1, -1):
        line = ""
        for rod in "ABC":
            if row < len(visual[rod]):
                line += visual[rod][row].center(tower_width)
            else:
                line += " " * tower_width
            line += " " * spacing
        print(line)

    # Print base and labels
    base = "—" * tower_width
    labels = [f"{rod}".center(tower_width) for rod in "ABC"]

    print(f"{base}{' ' * spacing}{base}{' ' * spacing}{base}")
    print(f"{labels[0]}{' ' * spacing}{labels[1]}{' ' * spacing}{labels[2]}")

def draw_disk(disk_size):
    """
    Return a string representing a disk of given size.
    Disk width is proportional to its size.
    """
    return "#" * (2 * disk_size - 1)

def main():
    """
    Main function to prompt user for number of disks and initiate the algorithm.
    """
    global step_counter
    step_counter = 0

    while True:
        try:
            n = int(input("Enter number of disks: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    state = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    print("\nInitial state:")
    print_state(state, total_height=n)
    time.sleep(ANIMATION_DELAY)

    hanoi(n, 'A', 'C', 'B', state, total_height=n)

    print("\nFinal state:")
    print_state(state, total_height=n)
    print(f"\nTotal steps taken: {step_counter}")

if __name__ == "__main__":
    main()
