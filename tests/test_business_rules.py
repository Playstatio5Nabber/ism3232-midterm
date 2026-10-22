from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    get_rental_discount,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)


def test_calculate_rental_cost_multiple():
    assert round(calculate_rental_cost(60.00, 2), 2) == 120.00


def test_calculate_rental_cost_one_day():
    assert round(calculate_rental_cost(85.50, 1), 2) == 85.50


def test_discount_two_days():
    assert get_rental_discount(2) == 0.0


def test_discount_three_days():
    assert get_rental_discount(3) == 0.10


def test_discount_six_days():
    assert get_rental_discount(6) == 0.10


def test_discount_seven_days():
    assert get_rental_discount(7) == 0.20


def test_discount_contractor_two_days():
    assert get_rental_discount(2, True) == 0.10


def test_discount_contractor_seven_days():
    assert get_rental_discount(7, True) == 0.20


def test_quote_at_waiver_limit_has_no_waiver():
    assert round(calculate_quote(150.00, 1), 2) == 150.00


def test_quote_just_below_waiver_limit_adds_waiver():
    assert round(calculate_quote(149.99, 1), 2) == 174.99


def test_quote_contractor_short_rental():
    assert round(calculate_quote(60.00, 2, True), 2) == 133.00


def test_deposit_at_limit_is_required():
    assert requires_deposit(1000.00) is True


def test_deposit_just_below_limit_not_required():
    assert requires_deposit(999.99) is False


def test_inspection_at_five_days_over_quote_limit():
    assert needs_inspection(5, 900.00) is True


def test_no_inspection_at_four_days():
    assert needs_inspection(4, 900.00) is False


def test_no_inspection_at_quote_limit():
    assert needs_inspection(5, 800.00) is False


def test_inspection_just_over_quote_limit():
    assert needs_inspection(5, 800.01) is True


def test_total_quoted_two_rentals():
    rentals = [
        {"customer": "A", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "B", "daily_rate": 85.00, "days": 4, "contractor": False},
    ]

    assert round(total_quoted(rentals), 2) == 451.00


def test_total_quoted_empty_list():
    assert total_quoted([]) == 0.0


def test_largest_rental_tie_returns_first():
    rentals = [
        {"customer": "First", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Second", "daily_rate": 60.00, "days": 2, "contractor": False},
    ]

    assert largest_rental(rentals) == "First"


def test_largest_rental_empty_list():
    assert largest_rental([]) == ""
