def delivery_fee(total):
    if total < 0:
        raise ValueError("Total cannot be negative")
    return 0 if total >= 20 else 3
