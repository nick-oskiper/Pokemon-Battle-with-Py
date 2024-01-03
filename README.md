# Pokemon-Battle-with-Py
Introductory Python Pokemon game using only text. Meant to demonstrate usage of python classes and object oriented programming.

# Introduction and Application

The system I developed is a Pokemon mimicking game. It is played in the output screen and only consists of text, however, images could be introduced in the future. 
For those unfamiliar, Pokemon takes place in a fictional world with wild creatures called Pokemon that people can catch. These caught Pokemon can then be used in Pokemon battles, either to defeat other player’s Pokemon or to defeat uncaught, wild Pokemon. 
My game uses the elements of catching wild Pokemon and battling other people (trainers) with their own Pokemon. Like the Pokemon games, from the beginning the user is brought into a fantasy world and gets to catch their first Pokemon, involving a Professor. Then the user gets to embark on their own journey, either traveling to a nearby village, where they unsuspectingly meet trainers to fight or into the forest, where they will be able to catch even more Pokemon.
These features make the game interactive and slightly strategic. The user doesn’t win against the rival trainers every time (though if the user catches Pokemon in the forest before they enter the village then they can). But, rather than making a difficult game I focused more on creativity.

# Application Design

The main classes in the system are the Pokemon class and the Trainer class. The Pokemon class takes in attributes: name, level, and type. The Trainer class takes in attributes: name, level, p1, p2, p3 (where p1, p2, p3 are the trainers' three Pokemon in order).
	The other important features of the Pokemon class is that its health corresponds to its level and its type is important in battles (for example, due to type effectiveness, types of water are twice as effective against types of fire). These types are all in the type_chart, a dictionary that is indexed through whenever a Pokemon hits another. Additionally, when a Pokemon reaches 0 health or less, it faints and gets sent out of battle. 
	The other important features of the Trainer class is that, since Trainers carry Pokemon, it is linked to the Pokemon class. Thus, when trainers fight each other (denoted by def vs, vs2) the attributes of Pokemon are used to denote the winners. Pokemon hit each other, taking away health and battles go in the order attacking Pokemon hits, defending Pokemon hits back, etc, etc. 
	Lastly, several definitions are used outside of classes that may reference class definitions. For instance, there are functions that let you capture Pokemon, functions that let you choose out of three action options, and functions that write the attack sequences of a battle. 
 
# Instructions

Instructions are listed in the program but the most important ones to keep in mind are the following:
To move from one line to the next you must click the ‘Enter’ button. This is meant to mimic the Pokemon games, while also decreasing the text the user has to read at once.
When the user is asked: What will you do? 1 “...” 2 “...” 3 “...” , the user must type in the number they picked to correspond to an action, followed by ‘Enter’.
The user may quit whenever they want by stopping the code from running, but there are also options to quit after every main event takes place.


# Libraries and Tools

No libraries and tools were used, other than inspiration from the Nintendo Pokemon games. Previous Pokemon projects on Python were used for idea generation, but only the concept was used and no code was copied. References are below:

https://www.youtube.com/watch?v=Pbs6jQZrZA4 
https://www.youtube.com/watch?v=TExSs9pG2EY&list=PLSCSqxsPFtI7f1pTad_nsKg61zDyy1DwP 

# Demo inputs

The user is forced to help the Professor and catch their first Pokemon. 
If the user chooses to go to the village after getting their Pokemon from the Professor, they can only win if they do the following combinations.
If Bulbasaur is picked, they can only beat Maisie
If Charmander is picked, they can only beat Timmy
If Squirtle is picked, they can only beat Pip
(any other combination will result in a loss)
If the user chooses to go to the Forest after getting their Pokemon from the Professor, they must find all three Pokemon before they are able to leave. These Pokemon are generated randomly at 20% chance, so there is no fixed order of finding them. After finding them, these three Pokemon are then added to their team.
If the user goes to the Village after the Forest, they will currently be able to beat any trainer they select. However, if the user wants to play around with Pokemon levels, this could change.
In order to face other trainers after the user wins, they will have to rerun the program.
If the user ever types something in a field that isn’t valid, the system will ask them to try again. 
