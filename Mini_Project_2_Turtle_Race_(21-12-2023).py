from turtle import Turtle, Screen  # Importing necessary modules for graphics
import random
from tkinter import *  # Importing the Tkinter library for the user interface


def start_race(color, chosen_color):
    global user_score
    # Set up the screen for the turtle race
    screen = Screen()
    screen.title("Make Your Bet")  # Title of the graphical window
    screen.setup(width=500, height=400)  # Setting up the size of the graphical window
    
    # Initial positions for the turtles in the race
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []  # List to hold all the turtles
    
    # Colors for the turtles available for selection
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    
    # Create turtles for each color and position them on the screen
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)  # Add each turtle to the list
    
    is_race_on = True  # Flag to control the race
    user_score = 0  # User's score for winning the race
    
    # Start the race
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False  # End the race if a turtle reaches the finish line
                winning_color = turtle.pencolor()
                print(f"You chose the {chosen_color} turtle.")  # Display user's chosen turtle
                if winning_color == color:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                    user_score += 10  # Update user score if they win
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                break
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)  # Move the turtles forward randomly
    
    # Clear and hide turtles after the race
    for turtle in all_turtles:
        turtle.clear()
        turtle.hideturtle()

    print(f"Your current score is: {user_score}")  # Display user's score
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        # Reset turtles' positions for a new round and show the color selection window
        for turtle in all_turtles:
            turtle.goto(x=-230, y=y_positions[all_turtles.index(turtle)])
        root.deiconify()
    else:
        print("Thanks for playing!")  # End of the game message
        screen.bye()  # Close the turtle graphics window
        root.destroy()  # Close the tkinter window

def set_color():
    color = var.get()
    chosen_color = var.get()  # Get the user's chosen color
    root.withdraw()  # Hide the tkinter window when the game starts
    start_race(color, chosen_color)

# Setup the Tkinter window for color selection
root = Tk()
root.title("Turtle Race")
root.geometry("300x100")  # Set the initial window size

var = StringVar(root)
var.set("Select the color of your turtle")  # Text displayed in the color selection menu
option = OptionMenu(root, var, "red", "orange", "yellow", "green", "blue", "purple")  # Dropdown menu with color options
option.pack()  # Display the color selection menu

submit_button = Button(root, text="Submit", command=set_color)  # Button to start the race
submit_button.pack()  # Display the button

root.mainloop()  # Run the Tkinter event loop for user interaction
