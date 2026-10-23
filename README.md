# ISM4343 Midterm: Ridgeline Tool Rental

- **Name:** Sami Ali
- **Version:** [Alpha]
- **Date:** October 22, 2026


## What This Program Does

This program turns ridgeline tool rental's pricing rules into multiple functions on python functions. It works out a quote for indivual rentals. it also checks iif the rental would needa deposit or a pickup inspection, and printsa report with a summary of all rentals.

##Business Rules 

-The rentals cost is the daily rate times the number of days.
- Rentals under 3 days get no discount, 3 to 6 days get 10% off, and 7 days or more get 20% off.
- Licensed contractors always get atleast 10% off, even with rentals under 3 days.
- A $25 damage waiver is added when the discounted cost is under $150.
- A quote of $1,000 or more needs a deposit.
- A rental needs a pickup inspection when it is 5 days or longer and the quote is over $800.


## How to run 

...
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
...


## How to Test

...

ruff format .
ruff check .
python3 -m pytest -v
... 


The project has 23 pytest tests.

## Files in this Repository 

-'business_rules.py' : the eight functions that carry out the rental
- 'main.py' : the rental list and the code that prints the report 
-'tests/test_business_rules.py' : the 23 pytest tests for thr functions 
- 'commnds.md' : the terminal record of how the project was built and checked
- 'requirements.txt': the termonal record of how the project was built and checked
- 'README.md' : the file 
-'requirements.txt': the python packages the project needs, from pip freeze
- '.gitignore' : keeps .venv and __pycache__ out of the repository

## AI Use Statement 

NO AI was used in the process of this assignment, All work was hand typed by yours truly with the assistance of my notes taken from this class. 
