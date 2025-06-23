import turtle

# Define a list of rainbow colors. Can be extended or modified as needed
RAINBOW_COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def draw_fractal_tree(turtle_obj, branch_length, angle, recursion_level, max_recursion_level):
    """
    Recursively draws a generic binary fractal tree, painting each level a different color.

    Args:
        turtle_obj: The turtle object used for drawing.
        branch_length: The length of the current branch segment.
        angle: The angle for branching (half of the total split angle).
        recursion_level: The current level of recursion (decreases with depth).
        max_recursion_level: The initial maximum recursion level (constant for all calls,
                             used to determine the current depth for coloring).
    """
    if recursion_level == 0:
        return # Base case: stop drawing

    # Determine the color for the current level
    color_index = (max_recursion_level - recursion_level) % len(RAINBOW_COLORS)
    turtle_obj.color(RAINBOW_COLORS[color_index])

    # Draw the current branch segment
    turtle_obj.forward(branch_length)

    # Save current position and heading (at the end of the drawn segment)
    current_pos = turtle_obj.position()
    current_heading = turtle_obj.heading()

    # Draw the left sub-branch
    turtle_obj.left(angle)
    # Pass max_recursion_level to the recursive calls as it's constant
    draw_fractal_tree(turtle_obj, branch_length * 0.65, angle, recursion_level - 1, max_recursion_level)

    # Return to the point where the current segment ended (where the split occurred)
    turtle_obj.penup() # Lift pen to avoid drawing while repositioning
    turtle_obj.goto(current_pos)
    turtle_obj.setheading(current_heading) # Restore original heading before right turn
    turtle_obj.pendown() # Put pen down to draw the right branch

    # Draw the right sub-branch
    turtle_obj.right(angle)
    # Pass max_recursion_level to the recursive calls as it's constant
    draw_fractal_tree(turtle_obj, branch_length * 0.65, angle, recursion_level - 1, max_recursion_level)

    # After drawing both sub-branches, return the turtle to the START of
    # the current branch segment to allow proper backtracking for previous levels.
    # This is necessary to ensure the turtle can draw the next segment correctly.
    turtle_obj.penup() # < Lift pen here to prevent drawing on backtrack
    turtle_obj.goto(current_pos) # Ensure it's at the end of the current segment
    turtle_obj.setheading(current_heading) # Restore heading before moving backward
    turtle_obj.backward(branch_length)
    turtle_obj.pendown() # < Put pen down, so it can draw the next segment correctly

# Set up the turtle and screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("lightgrey") # Set a light background for better contrast with the tree colors
pen = turtle.Turtle()
pen.speed(0) # Fastest drawing speed (0 for instant)
pen.pensize(2) # Make lines slightly thicker for visibility

pen.penup() # Ensure pen is up initially before moving to starting position
pen.goto(0, -280) # Start lower on the screen to accommodate tree height
pen.left(90) # Point upwards to start drawing the trunk
pen.pendown() # Put pen down only for the very first trunk segment draw

# Get recursion level from user
try:
    level = int(input("Enter recursion level (e.g., 8-12 for a dense tree): "))
except ValueError:
    print("Invalid input. Using default recursion level (10).")
    level = 10 # Default to a level that produces a nice tree

# Draw the fractal tree, passing the initial 'level' as max_recursion_level
# This 'max_recursion_level' acts as a reference for calculating the current depth for coloring.
draw_fractal_tree(pen, 250, 35, level, level)

# Keep the window open until manually closed
screen.mainloop()
