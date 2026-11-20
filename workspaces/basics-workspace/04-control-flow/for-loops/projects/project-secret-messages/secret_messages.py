# Project: Secret Messages - starter file
# The tasks are in the For Loops section of the book.

# An assistant's answer: it contains one mistake (Task 1).
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "meet me at the zoo at noon"
shift = 3

secret = ""
for letter in message:
    position = alphabet.find(letter)
    if position == -1:      # a space or punctuation mark stays as it is
        secret += letter
    else:
        secret += alphabet[position + shift]

print("Secret:", secret)

# Task 2: decrypt secret back into the original message.
# TODO: write a second loop here.

# Mission: agree on a shift with a partner, change message and shift above, and send only the
# secret text. Decrypt the message you receive. This cipher is for learning only: never use it
# for passwords or other confidential information.

# Task 3 (extend): break this message without knowing the shift.
intercepted = "wkh oleudub rshqv dw qlqh"
# TODO: an outer loop over every shift from 0 to 25, with the decryption loop inside it.
