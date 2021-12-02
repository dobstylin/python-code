# python-code
Python Code Created for Masters Course Work

Grading Logic Objective:
Consider the grading logic for this class:
• If the assignment is not submitted as a single uncompressed .py file, the grade is 0.
• If the assignment does not include the author’s name and date, the grade is 0.
• If the assignment does not include the honor statement, “I have not given or received any
unauthorized assistance on this assignment”, the grade is 0
• If the assignment does not include a link to an unlisted 3-minute YouTube video presenting the
code and answering the assigned questions, the grade is 0.
• If the assignment satisfies all of the above conditions…
o Up to ten points are awarded based on the correctness of the code; that is, how well it
meets the given specifications.
o Up to ten points are awarded based on the elegance of the code (data structure selection,
algorithm efficiency, function implementation, etc.).
o Up to ten points are awarded based on the code hygiene (white space, docstrings, etc.).
o Up to ten points are awarded based on the quality of the discussion in the YouTube video.
• Late assignments lose 1% (of total possible) per hour.
Write a python function which asks the user a series of questions based on the above logic. For example,
“Did the student include their name?” or “Out of ten points, how would you evaluate the correctness of
the code?”
Notice that if the student did not include their name, there is no reason to ask any more questions.
Likewise, if the assignment was not late, there is no reason to ask how late it was.
The function should return the student’s total score

Coprime.py Objective:
In number theory, two integers a and b are said to be coprime if the only positive integer that divides both
of them is 1.
Write a function coprime_test_loop() that asks the user for two numbers. This function will pass those
two numbers onto a second function coprime(a,b) which will return true or false depending on whether
or not the numbers are coprime. The function coprime_test_loop() will print out a message indicating
the result. It will then ask the user for another pair of numbers and query coprime(a,b) again. It will
continue this loop until the user indicates that they wish to exit the program.

GoldbachConjecture.py Objective:
Goldbach's Conjecture is one of the oldest and best-known unsolved problems in number theory and all
of mathematics. It states that every even integer greater than 2 can be expressed as the sum of two
primes. The conjecture has been shown to hold for all integers less than 4 × 1018, but remains unproven
despite considerable effort.
Test Goldbach's Conjecture on for all integers less than one hundred. For each integer, print out a single
line showing how two primes can sum to the integer. For example:
4 = 2 + 2
6 = 3 + 3
8 = 3 + 5
…etc.

HappyPrimes.py Objective:
A prime number (or a prime) is a natural number greater than 1 that cannot be formed by multiplying two
smaller natural numbers.
“Happy” has many definitions (even in mathematics). For our purposes, a happy number is a number
defined by the following process: Starting with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number either equals 1 (where it will stay), or it loops
endlessly in a cycle that does not include 1. Those numbers for which this process ends in 1 are happy
numbers, while those that do not end in 1 are unhappy numbers (or sad numbers). For example, 19 is
happy, as the associated sequence is:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Write code that endless loops, requesting/accepting an int from the user. Given the input, your code
should print out whether it is a happy prime, sad prime, happy non-prime, or sad non-prime.

HumanPyramid.py Objective: 
A human pyramid is a way of stacking people vertically in a triangle. With the exception of the people in
the bottom row, each person splits their weight evenly on the two people below them in the pyramid. For
example, in the pyramid above, person A splits her weight across people B and C, and person H splits his
weight – plus the accumulated weight of the people he is supporting – onto people L and M. It can be
mighty uncomfortable to be in the bottom row, since you'll have a lot of weight on your back! In this
assignment, you will explore just how much weight that is. Let us assume that everyone in the pyramid
weighs exactly 128 pounds.
Write a recursive function – def humanPyramid(row, column): – that takes as input the row and column
number of a person in a human pyramid, then returns the total weight on that person's back. The row and
column are each zero-indexed, so the person at row 0, column 0 is on top of the pyramid, and person M
in the above picture is at row 4, column 2.
Your implementation of humanPyramid must be implemented recursively and must not use any loops.
You may be surprised how little code is required!

GoldbachDuece.py Objective:
Given a list of length integers, do any two of them sum to sum? You solved this problem in last week’s
Goldbach’s Conjecture assignment. However, I bet your running time was O(n2). If not, great! This
assignment will be a snap. For the rest of you…
Ask the user for length and sum. Create a list of length random numbers between 0 and 100. Determine
if two of the numbers sum to sum in O(n.log(n)). Output the appropriate results.

Dice_Cups.py Objective:
Write a class SixSidedDie. The class should include the following methods: roll(), getFaceValue(), and
__repr__(). For example:
>>> d = SixSidedDie()
>>> d.roll()
3
>>> d.getFaceValue()
3
>>> d
SixSidedDie(3)
Create a TenSidedDie and a TwentySidedDie class. These two class must extend SixSidedDie. They must
provide the same functionality. They must not re-implement any code that is not necessary.
Create a Cup class. A cup will hold several dice that may be rolled at once. The cup may hold any number
of six-, ten-, or twenty- sided dice. For example, we could create a cup with one of each type of die as
follows:
>>> cup = Cup(1,1,1)
…or we could create a cup with 3 six-sided dice…
>>> cup = Cup(3,0,0)
By default, the cup will contain one of each type of die.
>>> cup = Cup()
The Cup class should include the following functionality: roll(), getSum(), __repr__(). For example:
>>> cup = Cup(1,2,1)
>>> cup.roll()
28
>>> cup.getSum()
28
>>> cup
Cup(SixSidedDie(3),TenSidedDie(5),TenSidedDie(3),TwentySidedDie(17))

CupsandDice.py Objective:
For this problem you will use the classes from the previous problem to build a game. The game will work
as follows:
1. Greet the user and ask their name.
2. Provide the user with a balance of 100 dollars.
3. Ask them if they would like to play a game.
4. Generate a random number between 1 and 100. This number will be called the goal.
5. Ask the user how much they would like to bet. This money is deducted from their account.
6. Ask the user how many of each die they would like to roll.
7. Create a cup filled with dice according to the user’s input.
8. Roll the cup and display the results.
9. If the roll exactly matches the goal, the user receives 10x bet added to their balance.
10. Otherwise, if the roll is within 3 of the goal but not over, the user receives 5x bet added to their
balance.
11. Otherwise, if the roll is within 10 of the goal but not over, the user receives 2x bet added to their
balance.
12. Report the results to the user. The message should include their name and updated balance.
13. Ask if they would like to play again. If so, go to step 4.

PalindromeDate.py Objective:
A palindrome date is a date that is the same when read forwards and backwards, e.g., ‘02/02/2020’. Write
a program that identifies and saves to a file all the palindrome dates in the 21st century using the
DD/MM/YYYY format. Do not use recursion. Do not use any built-in calendar-ish packages. To keep
things simple, treat leap years as regular years.

prng.py Objective:
Use the text version of War and Peace by Leo Tolstoy. You will use it create a pseudo random
number generator. The PRNG should be an object:
 prng = WarAndPeacePseudoRandomNumberGenerator()
Alternatively, you should be able to pass a seed when you create the object:
 prng = WarAndPeacePseudoRandomNumberGenerator(12345)
Then, you should be able to generate pseudo random numbers [0,1):
 r = prng.random()

OverlappingEllipses.py Objective:
In this problem you will use a pseudo random numbers to estimate the area of two overlapping ellipses.
An ellipse is a curve in a plane surrounding two focal points such that the sum of the distances to the two
focal points is constant for every point on the curve.
Create a Point class that takes the x and y coordinates of the point:
 p1 = Point(2,3)
 p2 = Point(4,3)
Create an Ellipse class that takes two points and the width of the long axis:
 e1 = Ellipse(p1,p2,4)
Write a function that takes two ellipses and returns the area of the overlap:
 overlap = computeOverlapOfEllipses(e1,e2)
This function should leverage the pseudo random number generator you built in the previous assignment.

PlotGenerator.py Objective:
A story generator or plot generator is a tool that generates basic narratives or plot ideas….The tool may
allow the user to select elements for the narrative, or it may combine them randomly, a specific variation
known as a random plot generator. Such tools can be created for virtually any genre, although they tend
to produce formulaic and hackneyed situations. – Wikipedia, 2019
Create a class called SimplePlotGenerator that when queried for a plot returns “Something happens”.
>>pg = SimplePlotGenerator()
>>pg.generate()
Something happens
Create a class called RandomPlotGenerator that when queried for a plot returns a random plot produced
from the seven files found on the D2L in the form <plot_names>, a <plot_adjectives> <plot_profesions>,
must <plot_verbs> the <plot_adjectives_evil> <plot_villian_job>, <plot_villains>. RandomPlotGenerator
must extend SimplePlotGenerator.
>>pg = RandomPlotGenerator()
>>pg.generate()
Aaliyah Mosley, a abiding alabasterer, must acknowledge the
assuming assassin, Acheron Redwood.
Create a class called InteractivePlotGenerator that when queried for a plot offers the user a list of five
random plot_names. After the user selects one, the system will offer the user a list of five random
plot_adjectives. Etc. After the user has made all seven selections, InteractivePlotGenerator should return
the final plot. InteractivePlotGenerator must extend SimplePlotGenerator.
Give special attention to how you query the user. Nothing in any of the plot generators should assume
the form of the I/O. That means no ‘print’ing and no ‘input’ing. Instead, each of the plot generators
should register the plot viewer. When it needs to query the user, it should do something like:
result = self.pv.queryUser(“Enter a number: ”)

PlotViewer.py Objective:
Write a class called PlotViewer. It will serve as the both the view and the controller for the plot generator
classes. The PlotViewer class will be able to register any plot generator.
>>pv = PlotViewer()
>>pv.registerPlotGenerator( SimplePlotGenerator() )
>>pv.generate()
Something happens
>>pv.registerPlotGenerator( RandomPlotGenerator() )
>>pv.generate()
Aaliyah Mosley, a abiding alabasterer, must acknowledge the
assuming assassin, Acheron Redwood.
>>pv.registerPlotGenerator( InteractivePlotGenerator() )
>>pv.generate()
Chose a hero’s name from the following list:
…
A critical concern is how the generator classes handle input/output. When they are connected to a
view/controller they must use the i/o of the view/controller. It may be simple text i/o. It may be a
complicate GUI. It may be a cell phone app. It may be a webpage. The generator (model) should not
know or care.

NumpyIntro.py Objective:
For this assignment you are going to practice the basic functions of NumPy.
1. Import NumPy
2. Use arange to create a NumPy array with 100 equally spaced values in the range 0 through 100
(not including 100). Name this NumPy array a.
3. Use arange to create a NumPy array with 10 equally spaced values in the range 0 through 100
(not including 100). Name this NumPy array b.
4. Use linspace to create a NumPy array in the range 0 through 10 (inclusive) with values spaced at
0.1. Call this NumPy array c.
5. Create a random two-dimensional array with the dimensions 10 by 10. Call this NumPy array d.
6. Reshape a so that it is a two-dimensional array with the dimensions 10 by 10.
7. Show the results of “a[4,5]”.
8. Show the results of “a[4]”.
9. Show the sum of d.
10. Show the max of a.
11. Show the transpose of b.
12. Show the results of adding a and d.
13. Show the results of multiplying a and d.
14. Show the results of computing the dot product of a and d.

GameOfLife.py Objective:
Read the Wikipedia article on Conway’s Game of Life. We will implement this simulation on a torus
because it will make the code easier and we won't need to deal with boundaries. This means that cells on
the top are adjacent to cells on the bottom and the same is true for the left and right sides.
Write a function called conway(s, p) that generates a board, which is a square two dimensional NumPy
array of size s by s. The board should be randomly populated with probability p. If p is set to 0, all cells
should be 0 (dead). If p is set to 1, all cells should be 1 (alive). Start with p=0.1; about 10 percent of cells
should 1.
Write a function advance(b,t) that accepts a Conway board and advances it t time steps according to the
rules:
• Any live cell (marked as 1) with fewer than two live neighbors dies, as if by underpopulation.
• Any live cell (marked as 1) with two or three live neighbors lives on to the next generation.
• Any live cell (marked as 1) with more than three live neighbors dies, as if by overpopulation.
• Any dead cell (marked as 0) with exactly three live neighbors becomes a live cell, as if by
reproduction.
Write a function to pleasantly display the board.


