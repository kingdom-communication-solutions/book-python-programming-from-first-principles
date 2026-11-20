# OOP workspace: Python Programming from First Principles

This folder contains the Object-Oriented Programming part of the book as files you can run on your own computer:
the Library checkpoints and modules, one notebook per runnable listing, one notebook per Coding Challenge,
and the University Course System starter project.

## Set up once

1. Install Python 3.10 or later (see Getting Started in the book).
2. Open a terminal in this folder and create a virtual environment:
   - macOS, Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
3. Install the packages: `python -m pip install -r requirements.txt`. The OOP part needs only the standard
   library; the file prepares the environment for the whole book.
4. For notebooks, also run `python -m pip install notebook`, then `jupyter notebook`.

## Run the code

- A Python file: open a terminal in its folder and run `python library_stage_05.py`. In VS Code or PyCharm,
  open the folder and run the file.
- A notebook: open it in Jupyter, VS Code or PyCharm and run the cells from the top.
- The University project: in `ch07-university-course-project/university_app`, run
  `python check_university.py` after each change, and `python main.py` to use the console application.

Solutions are not included. Download the complete repository ZIP to keep all companion files together.
