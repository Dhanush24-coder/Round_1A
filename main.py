import json
from utils import extract_headings

if __name__ == "__main__":
    result = extract_headings("sample.pdf")
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print("✅ Extraction complete. Output saved to output.json")
