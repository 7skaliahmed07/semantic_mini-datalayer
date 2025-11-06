import argparse
import json
from connectors.local_reader import list_files
from processing.extract import extract_texts
from processing.ner import extract_entities

def main(input_dir, output_path):
    # 1️⃣ List all input files
    files = list_files(input_dir)
    print(f"✅ Loaded {len(files)} text files")

    # 2️⃣ Extract text
    texts = extract_texts(files)
    if len(texts) > 0:
        print("📄 Sample text preview:", texts[0]['text'][:200])

    # 3️⃣ Run NER extraction
    results = []
    for f in texts:
        ents = extract_entities(f['text'])
        results.append({"file": f['path'], "entities": ents})

    print("🧠 Extracted entities:", results)

    # 4️⃣ Save output JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Wrote results to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input_dir", required=True)
    parser.add_argument("--output", dest="output_path", required=True)
    args = parser.parse_args()

    main(args.input_dir, args.output_path)
