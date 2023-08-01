# src folder called as a package 
# because it has __init__.py
from src.loan import Loan    # src act as a package with __init__.py
from src.vehicle import Vehicle

# Python gives Entry point of a program
if __name__ == "__main__":

    person1 = Loan(1, "sambath", "No", 740)    # without __name__ executes line by line
    person1.status()

    hero = Vehicle("Hero", "Self and Kick")
    hero.disp()