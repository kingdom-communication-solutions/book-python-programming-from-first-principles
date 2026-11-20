class RegistrationError(Exception):
    pass


def validate_registration(name, age):
    # TODO: apply the registration exercise rules; return (stripped_name, integer_age).
    pass


requests = [("Ada", 20), ("", 19), ("Bo", "twenty"), ("Cy", 150), ("Dee", 25)]

# TODO: handle RegistrationError for each row, retaining valid records.
# TODO: print accepted names and the rejection count.
# TODO: check boundaries, integer text, Boolean/fractional inputs and empty batches.
