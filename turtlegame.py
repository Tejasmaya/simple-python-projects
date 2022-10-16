'''
Advanced level turtle programming involves more usage of conditionals, loops etc. Whenever there’s a need of making recurring design patterns or games conditionals, loops are widely used.
So far we have learnt how to make basic shapes, then some intermediate level designs in this article of Beginners to Advanced Turtle Projects and now is the time to finally use turtle for which it is famous; game development. Let us make a unique game using the turtle library.

(A) Whose turtle is faster?
The aim of this game is to show two turtles and their specific targets where they have to reach. This will be a two-player game, wherein each user will roll a dice and the turtle will move that number of steps and the same goes for the second player. The game will end once any one of the players reaches the target destination.

Getting started:

Step 1: Set up the game environment and import the required library
Step 2: Working on the designing part that is the turtles and the target destination.
Step 3: Coding for the logical part. How and when the turtle should move, the winning criteria etc

Step 1: Setting up the environment and importing the library


'''

import turtle
import random

'''
Explanation: Here we have imported two libraries namely turtle and random. Turtle library will help us in the designing part whereas random library will help in building the logical part for the game.
the random library helps in picking random elements by providing various functions that are capable of performing such operations.

Step 2: Working on the designing part

In this step, we have to create two turtles and their destination i.e a circle. The colour of both the turtle should be different and their destination should match that respective colour.

Code for two turtles:
'''
p_one = turtle.Turtle()
p_one.color("purple")
p_one.shape("turtle")
p_one.penup()
p_one.goto(-200,100)
p_two = p_one.clone()
p_two.color("orange")
p_two.penup()
p_two.goto(-200,-100)

'''
Explanation: We used purple colour for player 1 and orange colour for player 2.
p_one.shape(“turtle”): This function shape() sets the turtle shape to the one that is passed as argument.
p_one.goto(-200,100): This will set the position of the turtle at x = -200 and y = 100
p_one.clone(): This method simply copies the characteristics of the p_one turtle. Player two’s turtle was made by cloning player one’s turtle, changing its colour, and moving it to a new starting place.

Please note that once the turtles have been formed, we must set them in their beginning places and ensure that they are aligned.

We must now create houses for the turtles. These houses will serve as the turtles’ destination. A circle will represent each of the turtles’ houses. We must ensure that both destinations are equidistant from the starting point in this case:

Code for destinations:
'''
p_one.goto(300,60)
p_one.pendown()
p_one.circle(40)
p_one.penup()
p_one.goto(-200,100)
p_two.goto(300,-140)
p_two.pendown()
p_two.circle(40)
p_two.penup()
p_two.goto(-200,-100)

'''Explanation: For the designing of two destinations, we have made use of a circle(). To set the position of the destinations we made use of the goto() method.

Step 3: Coding for the logical part.

It’s time to start working on the rest of the game’s programming. Because we’ll be using loops and conditional expressions, pay attention to the indentations and spaces. This process is repeated until one of the turtles achieves the target, at which point the programme ends. The following is an example of the code:
'''

die = [1, 2, 3, 4, 5, 6]
for i in range(20):
    if p_one.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif p_two.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    else:
        p_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("Result of the die roll is: ")
        print(die_outcome)
        print("Number of steps will be: ")
        print(20*die_outcome)
        p_one.fd(20*die_outcome)
        p_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("Result of the die roll is: ")
        print(die_outcome)
        print("Number of steps will be: ")
        print(20*die_outcome)
        p_two.fd(20*die_outcome)

'''Explanation:
Line 1: This line is a variable that is list and it stores the numbers ranging from 1-6.
Line 2: This line of code represents the for loop that will run in the range of 1 to 20.
Line 3 to 8: These lines check for the player’s status that is win or lose. Based on the position of the loop it is decided whether to terminate the loop or not. If the specified condition is reached then the loop breaks and prints the statements.
Line 9: If no player has won then the flow of the code moves to the else statement.
Line 10: Requests the user by printing a statement to take a turn by pressing Enter key.
Line 11: Selects a random element from the die list and assigns the value to the variable die_outcome.
Line 12: This line prints the line “Result of the die roll is: “
Line 13: This line prints the value stored in die_outcome
Line 14: Same as line 11.
Line 15: This is done in order to decrease the number of steps required.
Line 16: Take the turtle in the forwarding direction.
Line 17 to 23: These lines are the same for player 2. The same functionalities need to be applied to
player 2.
The for loop continues its flow till any one of the players reaches the destination.

Finally, here’s the end to our game project. Try to add new functionalities to this game. Make the UI look good, add background colour, add images, change the speed of the turtle etc. This library is all one need to develop amazing projects.

Explore more by reading official documentation: Python Turtle Library
'''
