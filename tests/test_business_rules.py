from business_rules import calculate_rental_cost, get_rental_discount


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
