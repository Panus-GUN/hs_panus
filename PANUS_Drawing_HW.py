import turtle

# Set up my turtle
turtle.speed(10)
turtle.shape('turtle')
turtle.bgcolor('black')

#set up the color 
turtle.color('yellow')

#set up to make the star more in the middle 
turtle.penup()
turtle.backward(250) #from half of the length that gonna drawing 
turtle.pendown()

#fill yellow color 
turtle.begin_fill()

#start drwaing 
turtle.forward(500)  # First side
turtle.right(144)
turtle.forward(500)  # Second side
turtle.right(144)
turtle.forward(500)  # Third side
turtle.right(144)
turtle.forward(500)  # Fourth side
turtle.right(144)
turtle.forward(500) 

# End fill yellow 
turtle.end_fill()

# wirte STARDEE
turtle.penup()
turtle.goto(-210, 200)
turtle.pendown()
turtle.color('yellow')
turtle.write("STARDEE", font=("Courier", 100, "bold"))

# write statement 
turtle.penup()
turtle.goto(-200, -350)
turtle.pendown()
turtle.color('white')
turtle.write("Ai guide PANUS write ;)", font=("Comic Sans MS", 30, "bold"))

# move turtle out of the frame 
turtle.penup()
turtle.goto(-1000,-1000)

# Keep the window open until closed manually
turtle.mainloop()