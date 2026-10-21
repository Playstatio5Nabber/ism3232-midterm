SHORT_RENTAL_DAYS = 3

LONG_RENTAL_DAYS = 7

STANDARD_DISCOUNT = 0.10

LONG_RENTAL_DISCOUNT = 0.20

CONTRACTOR_DISCOUNT = 0.10

DEPOSIT_LIMIT = 1000.00
INSPECTION_DAYS = 5
INSPECTION_QUOTE_LIMIT = 800.00


WAIVER_THRESHOLD = 150.00
WAIVER_FEE = 25.00


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


def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Return the discounted rental cost including any waiver fee."""
    cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    quote = cost * (1 - discount)
    if quote < WAIVER_THRESHOLD:
        quote += WAIVER_FEE
    return quote


def requires_deposit(quote: float) -> bool:
    """Return True when the quote requires a deposit."""
    return quote >= DEPOSIT_LIMIT


def needs_inspection(days: int, quote: float) -> bool:
    """Return True when the rental needs a pickup inspection."""
    return days >= INSPECTION_DAYS and quote > INSPECTION_QUOTE_LIMIT
