import csv
import json
from pathlib import Path

# Keep readings.csv beside this script; run from this folder.
source_path = Path("readings.csv")
archive_path = Path("journal.json")
summary_path = Path("summary.txt")

# TODO: read rows with DictReader and convert each year to int.
# TODO: save the records as JSON, reload them and compare equality.
# TODO: write and reread the title summary, then print the three results.
# TODO: check the header-only CSV case described in the book.
