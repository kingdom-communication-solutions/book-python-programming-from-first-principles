"""Library stage 01: a Book class and separate Book objects."""


class Book:
    pass


first_copy = Book()
second_copy = Book()
same_copy = first_copy

print(type(first_copy))
print(first_copy is second_copy)
print(first_copy is same_copy)
