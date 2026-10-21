from business_rules import calculate_quote, calculate_rental_cost, get_rental_discount


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
