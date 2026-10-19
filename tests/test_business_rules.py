from business_rules import calculate_rental_cost


def test_calculate_rental_cost_multiple():
    assert round(calculate_rental_cost(60.00, 2), 2) == 120.00


def test_calculate_rental_cost_one_day():
    assert round(calculate_rental_cost(85.50, 1), 2) == 85.50
