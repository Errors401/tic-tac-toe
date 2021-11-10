# Software Requirements

## Vision

What is the vision of this product?

Our project is based on communicating with the user through the command line.

What pain point does this project solve?

To begin with our game will be created for entertainment purpose and to let the user break out the boring routine.

Why should we care about your product?

Because our project is keeping up with latest technologies, and it convert a traditional game into an electronic one.

## Scope (In/Out)

IN - What will your product do

Describe the individual features that your product will do.

### Tic-Tac-Toe

1. The user should be able to play the game with the bot or with another player through the command line.
2. The user should be able to choose X or O.
3. Each user should be able to see his total score.
4. The user would be able to discover the game rules at the beginning if he is not familiar with the game.

OUT - What will your product not do.

1. Our product will never turn into an IOS or Android app.
2. Our product will not use a graphical user interface

## Minimum Viable Product

What will your MVP functionality be?

Our product is for entertainment purpose, and we will use Python and its dependent libraries to ensure that we can communicate with the user through the command line, so he could experience a fun game.

What are your stretch goals?

Try to present an images through the command line for winning or losing

What stretch goals are you going to aim for?

Using Python GUI.

## Functional Requirements:

List the functionality of your product:

1. A user can see a welcoming message when he start the game.
2. A user can see the game options.
3. A user can seee the game rules if he choose so.
4. A user can start the game and choose to play either with another player or with the bot.
5. A user will have the ability to play with X or O.
6. A user will see the board once he start the game.
7. A user will see his result for each game.
8. A user will see his total score whenever he finish the game.

## Data Flow

1. First step once the user enter the game he will receive a welcoming message.
2. Second step the user will be able to choose one of the game options (Start, Game Rules, Quit).
3. Third step taking the user input.
4. Forth step if the user enter "Quit" he will get out of the game.
5. Fifth step if the user enter "Game Rules" the game rules will appear as a message, and he will have the option list again.
6. Sixth step if the user enter "Start", a new message will appear asking the user to choose his preferences to play with: another player, bot.
7. Seventh step after the user choose his preferences he will receive a new message asking him to pick X or O.
8. Eighth step in this step the user will actually start playing the game.
9. Ninth step after each round the user will know his result in that round.
10. Tenth step if the user decide to quit the game he will receive a message with his total score the game.

## Non-Functional Requirements:

Non-Functional Requirements judge the software system based on non-functional standards that are critical to the success of the software system. In our product we meet with NFR in Usability, so we offer the ability for the user to easily interact with the game. Moreover, our product also meet with the testability so we will use the 'GitHub' actions to automate and test the work flow of our product.
