# Semantic Datalayer — Mini Starter


Small demo project to show ingestion -> extraction -> structured output.


## Setup
1. Create a Python 3.9+ virtualenv.
2. `pip install -r requirements.txt`
3. Place some `.txt` or `.pdf` files into `sample_data/`.
4. Run `python main.py --input sample_data --output output/results.json`


## What it does
- Extracts text from files
- Runs spaCy NER to extract person/org/date entities
- Saves results as JSON