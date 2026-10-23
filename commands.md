# Terminal Record: Ridgeline Tool Rental

## 1. Building the project

```
mkdir ism3232-midterm
cd ism3232-midterm
git init -b main
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pytest ruff
python3 -m pip freeze > requirements.txt
mkdir tests
touch business_rules.py main.py commands.md README.md .gitignore tests/__init__.py tests/test_business_rules.py
nano .gitignore
git remote add origin https://github.com/playstatio5nabber/ism3232-midterm.git
git push -u origin main
```

## 2. The virtual environment

```
which python3
```

```
/Users/samiali/ism3232-midterm/.venv/bin/python3
```

The path ends in .venv/bin/python3 inside the project folder, which shows the virtual environment is active.

## 3. The project structure

```
tree -L 2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The __pycache__ folder is on my computer but not in my GitHub repository because .gitignore keeps it out.

## 4. Every function and test

```
rg 'def '
```

```
tests/test_business_rules.py:def test_calculate_rental_cost_multiple():
tests/test_business_rules.py:def test_calculate_rental_cost_one_day():
tests/test_business_rules.py:def test_discount_two_days():
tests/test_business_rules.py:def test_discount_three_days():
tests/test_business_rules.py:def test_discount_six_days():
tests/test_business_rules.py:def test_discount_seven_days():
tests/test_business_rules.py:def test_discount_contractor_two_days():
tests/test_business_rules.py:def test_discount_contractor_seven_days():
tests/test_business_rules.py:def test_quote_at_waiver_limit_has_no_waiver():
tests/test_business_rules.py:def test_quote_just_below_waiver_limit_adds_waiver():
tests/test_business_rules.py:def test_quote_contractor_short_rental():
tests/test_business_rules.py:def test_deposit_at_limit_is_required():
tests/test_business_rules.py:def test_deposit_just_below_limit_not_required():
tests/test_business_rules.py:def test_inspection_at_five_days_over_quote_limit():
tests/test_business_rules.py:def test_no_inspection_at_four_days():
tests/test_business_rules.py:def test_no_inspection_at_quote_limit():
tests/test_business_rules.py:def test_inspection_just_over_quote_limit():
tests/test_business_rules.py:def test_total_quoted_two_rentals():
tests/test_business_rules.py:def test_total_quoted_empty_list():
tests/test_business_rules.py:def test_largest_rental_tie_returns_first():
tests/test_business_rules.py:def test_largest_rental_empty_list():
tests/test_business_rules.py:def test_format_line_no_deposit_no_inspection():
tests/test_business_rules.py:def test_format_line_deposit_and_inspection():
business_rules.py:def calculate_rental_cost(daily_rate: float, days: int) -> float:
business_rules.py:def get_rental_discount(days: int, contractor: bool = False) -> float:
business_rules.py:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
business_rules.py:def requires_deposit(quote: float) -> bool:
business_rules.py:def needs_inspection(days: int, quote: float) -> bool:
business_rules.py:def total_quoted(rentals: list) -> float:
business_rules.py:def largest_rental(rentals: list) -> str:
business_rules.py:def format_rental_line(
```

business_rules.py defines 8 functions and tests/test_business_rules.py defines 23 tests.

## 5. Which files print

```
rg -l 'print'
```

```
main.py
README.md
```

main.py is the only Python file that prints, because business_rules.py returns values and leaves the printing to main.py.

## 6. The commit history

```
git log --oneline
```

```
ff05d42 Fix README headings, code blocks, typos
e1a9c14 Add README with rules, run and test steps, and AI statement
d1fe7d0 Add main report that loops over rentals and prints summary
2056770 Add report line formatter with yes and no tests
f4bdbf1 Add total and largest rental loops with list tests
2a9cc42 Add deposit and inspection rules with boundary tests
fd3cee2 Add quote tests for waiver limit and contractor case
9a648ff Add quote calculation with damage waiver and waiver limit tests
67b82e9 Add rental discounts and boundary tests
1ba56ca Add base rental cost calculation and two tests
e38ed73 Set up midterm structure and python dependencies
```

There were 11 commits at that point.
