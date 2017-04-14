# Problem Description
Suppose you have a wedding to plan, and want to arrange the wedding seating for a certain
number of guests in a hall. The hall has a certain number of tables for seating.

-- Some pairs of guests are Firends (F) and want to sit together at the same table.

-- Some other pairs of guests are Enemies (E) and must be separated into different tables.

-- The rest of the pairs are Indifferent (I) to each other and do not mind sitting together or not.

-- Each pair of guests can have only one relationship, (F), (E) or (I).

-- Each guest should be seated at one and only one table

++ Tables have no limit in capacity.

## Input
Input must be a file containing a few lines, for example:

![alt tag](https://github.com/aly78ahmady/satisfy-algorithm/raw/master/inexample.png)

First line contains two integers. First one is the number of guests and the second is the number of tables.
Each line after the first one, contains two integers and a character, that represents a relation between two guest. 

In the above example: The weeding has 4 guest totally. And the hall has 2 tables. Gest {1} and guest {2} are Firends and must seat at the same table. Guest {2} and guest {3} are Enemies and must seat at diffrent tables.

## Output
Output must be a file and must have following lines as an example:

![alt tag](https://github.com/aly78ahmady/satisfy-algorithm/raw/master/outexample.png)

First line must be "yes" if the problem is satisfiable, else "no" and program stops writting in the output.
If "yes" was the first line, following lines must be the seating arrangement. Each line must has two integers first one as guest's number, and the second one as table's number.

Above example, is a solver for input example. It shows: Problem has answer. guest {1} must seat at the table {2}. guest {2} must seat at the table {2}. guest {3} must seat at the table {1}. guest {4} must seat at the table {1}.
