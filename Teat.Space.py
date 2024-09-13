import turtle

# Set up turtle
turtle.speed(1)
turtle.bgcolor('black')
turtle.penup()

# List of text styles with their names
styles = [
    ("Arial", 30, "normal"),
    ("Arial", 30, "bold"),
    ("Arial", 30, "italic"),
    ("Courier", 30, "normal"),
    ("Courier", 30, "bold"),
    ("Courier", 30, "italic"),
    ("Comic Sans MS", 30, "normal"),
    ("Times New Roman", 30, "normal"),
    ("Verdana", 30, "bold"),
    ("Helvetica", 30, "italic")
]

# List of corresponding colors for each style
colors = ['yellow', 'cyan', 'magenta', 'orange', 'lime', 'pink', 'purple', 'blue', 'red', 'white']

# Position the turtle at the top for writing the first text
y_position = 200

# Loop through the styles and display the text with each font style
for i, style in enumerate(styles):
    turtle.goto(-200, y_position)  # Position for writing
    turtle.color(colors[i])  # Set color for each line
    text = f"{style[0]}, {style[1]}, {style[2]}"  # Display font name, size, and style
    turtle.write(text, font=style)  # Write the text using the current style
    y_position -= 50  # Move down for the next text

# Hide the turtle and keep the window open
turtle.hideturtle()
turtle.mainloop()
