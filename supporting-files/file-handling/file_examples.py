# Worked examples from File Handling in Python.
# Run from a separate practice folder.

f = open("notes.txt", "r", encoding="utf-8")
print(f)
f.close()

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

with open("notes.txt", "r", encoding="utf-8") as f:
    print("Filename:", f.name)
    print("Mode:", f.mode)
    print("Is closed?", f.closed)

print("Is closed after block?", f.closed)

with open("story.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("Project Summary\n")
    f.write("================\n")
    f.write("All tasks completed successfully.\n")

with open("app.log", "a", encoding="utf-8") as f:
    f.write("User logged in\n")
    f.write("User opened settings\n")

with open("large_dataset.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

try:
    with open("config.ini", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: The configuration file is missing.")
