# Data for the Museum Collection Explorer

`cma-paintings.csv`: the metadata of all 4,693 paintings in the collection of the Cleveland Museum of Art, saved from the museum's Open Access API on 3 November 2026. The museum publishes this metadata under the CC0 1.0 licence (https://www.clevelandart.org/open-access). Source, checksums and every transformation are in `datasets/cleveland-museum-paintings/provenance.json` in the book repository.

Columns: id, accession_number, title, department, culture, date_label, earliest_year, latest_year, artists, url. Negative years are years before the Common Era (-300 is 300 BCE). Three records have no latest year.
