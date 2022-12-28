# DFASimulator
A Deterministic Finite-state Automata simulator I made in python.

A DFA is a machine that has states and transitions. It reads an input string, and accepts only if the machine is at an accept state when the string is finished being read.
Each state must have exactly one output transition for each letter in the alphabet.
The machine always starts at the start state.

The machine is specified as a dictionary. Each state is a key and the value is another dictionary. 
The start state is the first state in the dictionary.
The keys in that dictionary are the the outgoing arrow transitions and the values are the states that they go to.
To mark an accept state, put a key in the state dictionary called "accept", and set it's value to True.

DFAs can be specified using this format.

The program asks the user for an input string. It must contain letters only from the outgoing transitions. (The string must have the same alphabet).
The program then runs the DFA on the input string one letter at a time. It ouputs the transitions taken and if the string was accepted or rejected.
