# Worked examples from Categorical Data with `Enum`.
# Run from a separate practice folder.

from enum import Enum

class Role(Enum):
    ADMIN = 1
    EDITOR = 2
    VIEWER = 3

print(Role.ADMIN)

class Sentiment(Enum):
    POSITIVE = 1
    NEGATIVE = 2
    NEUTRAL = 3

for code in [1, 99]:
    try:
        role = Role(code)
        print(role.name)
    except ValueError:
        print("Unknown role")
