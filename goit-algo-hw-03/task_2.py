import turtle


def koch_curve(length, level):
    """
    Draw a Koch curve segment recursively.

    Parameters:
    - length: Length of the current segment.
    - level: Current recursion depth.
    """
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_curve(length, level - 1)
        turtle.left(60)
        koch_curve(length, level - 1)
        turtle.right(120)
        koch_curve(length, level - 1)
        turtle.left(60)
        koch_curve(length, level - 1)


def draw_koch_snowflake(level):
    """
    Draw a complete Koch snowflake with the given recursion level.

    Parameters:
    - level: Recursion depth to control fractal complexity.
    """
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 90)
    turtle.pendown()

    for _ in range(3):
        koch_curve(300, level)
        turtle.right(120)

    turtle.hideturtle()
    turtle.done()


def main():
    """
    Entry point: ask user for recursion level and draw the fractal.
    Keeps prompting until valid input is received.
    """
    while True:
        try:
            level = int(input("Enter recursion level: "))
            if level < 0:
                print("Recursion level must be a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    draw_koch_snowflake(level)


if __name__ == "__main__":
    main()
