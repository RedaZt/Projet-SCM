# Projet-SCM

## Summary
This was a school assignment where we were told to code an application that can calculate the transportation cost using three optimization algorithms (NorthWest Corner, Least Cost and Balas-Hammer algorithm).


## Problematic
Imagine you’re the owner of a factory that specializes in a certain product, like any other business owner your goal is to maximize the profit, and the way to that is to optimize the various processes involved in production as much as possible, one of these processes being the transportation of that said product from your factory to a to a number of warehouses or customers, with The objective being to fully satisfy the destination requirements within the operating production capacity constraints at the minimum possible cost.

Now let's take this even a step further and say instead of one, you own multiple factories, with the cost of shipping from each one of them to each destination being different and known, how would you go about minimizing the cost of transportation in this case ?

What I just described to you is known as the transportation problem, it is a special class of linear programming, which deals with shipping commodities from sources to destinations. The objective of the transportation problem is to determine the shipping schedule that minimizes that total shipping cost while satisfying supply and demand limits. The transportation problem has an application in industry, communication network, planning, scheduling transportation and allotment etc.


## Algorithms
Luckily for us this problem has already been worked on and there exist some algorithms and methods that you can use to help you lower the transportation cost.
in this project we chose to address three main algorithms, which I won't go too deep into, but feel free to check them out if you’re interested.
  * NorthWest Corner
  * Least Cost
  * Balas-Hammer
  
(You can check the code for these methods in the "/Projet-SCM/algorithms" folder)


## Requirements
  * [Python 3.4+](https://www.python.org/downloads/)
  * [PyQt5](https://pypi.org/project/PyQt5/)


## Usage
Start by downloading the "Projet-SCM.zip" file from the latest release [here](https://github.com/RedaZt/Projet-SCM/releases) and installing the required packages. 
Upon running the "main.py" script you'll be met with this simple, self explanatory UI

<p align="center">
  <img src="/src/1.png" width="70%"/>
</p>

In the top section you can see a customizable table where you can set the transportation cost between each source and each destination.

After matching the values of the table to your problem, the next step is to solve it using one of the three methods, which you can do by just pressing the button with the name of your desired method.

<p align="center">
  <img src="/src/2.png" width="70%"/>
</p>

the solution will appear in the bottom section, you can view the first five iterations using the "show iterations" button.

<p align="center">
  <img src="/src/3.png" width="70%"/>
</p>