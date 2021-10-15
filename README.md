# Elevator
## Problem Statement
Given a log of user inputs (button presses) from an efficient Elevator, create a program to determine the order in which the elevator car went to the different floors. Where the doors opened.

**Details**:
Design an efficient Elevator program that takes a sequence of user requests (button presses) from the past (a log),  and determines the most optimal order that they were fulfilled.
Return a sequence of floors, in the order the elevator car visited them, starting from where the elevator was. e.g [4,2,5,6] means the elevator car was at level 4, then went to levels 2,5,6 respectively.

**Button Presses include:**
A floor number e.g 1,5,11 (Pressed from inside the elevator)
Up or Down Arrows (Pressed from outside the elevator)

Design the input sequence and all the necessary OOP entities (Classes and their relationships, e.t.c)

**Case 1:**
A user on ground floor went to 11th Floor.  :)

**Case 2:**
3 users are on ground floor went to floors: Basement, 8, 9.

**Case 3:**
15 users from 5th floor went to ground floor.
2 users from Ground Floor went to 11th.

**Case 4:**
A user on Ground Floor went to 5th
A user on 4th went to 6th
A user on 2nd went to 11th
A user on 3rd went to the Basement

**Case 5:**
A playful child entered the elevator on level 5 and presses all the floors numbers.

### Assumptions & Constraints:

- The input sequence is NOT real time. It is the elevator's log of the user inputs **in the order that they were given, yesterday.**
You're investigating what the elevator did, given that set of input sequence.
- The elevator used the most optimal order of execution
- All users came from outside the elevator car.
- The car is considered to have gone to a floor, if the doors opened on that floor.
- Every user weighs 10kg.
- The elevator maximum allowed weight is 100kg.

# Elevator Algorithms

## Fist Come First Served (FCFS)
In this Disk Scheduling Algorithm, the requests are addressed in the order they arrive in the disk queue.

## Shortest Seek Time First (SSTF)
In this Disk Scheduling Algorithm, the request near the disk arm will get executed first.

## SCAN
In this Disk Scheduling Algorithm, the disk arm moves into a particular direction and services the requests coming in its path and after reaching the end of disk, it reverses its direction and again services the request arriving in its path.

## LOOK
In this Disk Scheduling Algorithm, the disk arm moves into a particular direction and services the requests coming in its path and after reaching the end of disk goes to the last request to be serviced in front of the head and then reverses its direction from there only.

# Algorithms implemented
- FCFS
- SSTF
- SCAN

# Installation and Setup
>- Clone the repository.
>- Navigate to the project folder and open it in your most suitable editor.
>- In main.py, under the Operator() instance which takes an array of tuples.
>- For every turple, there are two elements. 
>- In the first index, the direction the user wants to go "up", "down" or "go" if the user was inside the car.
>- In the second index, the floor to which the user is calling the car from for "up" or "down" or for which the car to go to for "go".
>- Run the main.py file.

# Known Issues/Blockers
- High space complexity for sorting algorithm.

# Author(s) information: 
> Namugera Bbaale Philip

# Contact information.
> To collaborate, reach out to namugera.philip@gmail.com

# License and Copyright information.
> The MIT License (MIT) Copyright © 2020 Namugera Bbaale Philip.
