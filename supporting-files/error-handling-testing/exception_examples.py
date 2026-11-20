# Worked examples from Exceptions.
# Run from a separate practice folder.

try:
    n = 0
    res = 100 / n
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid value provided.")
else:
    print("Result:", res)
finally:
    print("Execution complete.")

try:
    x = int("hello")     # will cause ValueError
    inv = 1 / x          # would cause ZeroDivisionError if x were 0
except ValueError:
    print("That value cannot be converted to a number.")
except ZeroDivisionError:
    print("Zero has no multiplicative inverse.")

items = ["10", "twenty", 30]  # mixed input

try:
    total = int(items[0]) + int(items[1])
except (ValueError, TypeError) as e:
    print("Conversion error:", e)
except IndexError:
    print("List index out of range.")

try:
    result = "100" / 20  # TypeError: dividing string by number
except ArithmeticError:
    print("Some arithmetic problem occurred.")
except:
    print("Something went wrong!")

class AgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set_age(-5)
except AgeError as e:
    print(e)

print(isinstance("20", (str, int)))
print(isinstance(20.5, (str, int)))
print(isinstance(True, int))
print(isinstance(True, bool))
