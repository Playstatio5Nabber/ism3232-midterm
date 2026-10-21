SHORT_RENTAL_DAYS = 3
LONG_RENTAL_DAYS = 7
STANDARD_DISCOUNT = 0.10
LONG_RENTAL_DISCOUNT = 0.20
CONTRACTOR_DISCOUNT = 0.10


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return the rental cost before any discount."""
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return the discount based on rental days and contractor status."""
    if days >= LONG_RENTAL_DAYS:
        return LONG_RENTAL_DISCOUNT
    elif days >= SHORT_RENTAL_DAYS:
        return STANDARD_DISCOUNT
    elif contractor:
        return CONTRACTOR_DISCOUNT
    return 0.0
