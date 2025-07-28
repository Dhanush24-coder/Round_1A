import fitz  # PyMuPDF

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    font_sizes = {}
    heading_data = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    size = round(span["size"])
                    font_sizes[size] = font_sizes.get(size, 0) + 1

    if not font_sizes:
        return {"title": "", "headings": []}

    sorted_sizes = sorted(font_sizes.items(), key=lambda x: -x[1])
    top_sizes = sorted([fs[0] for fs in sorted_sizes])[-4:]  # Pick top 4 sizes

    level_map = {size: i+1 for i, size in enumerate(reversed(top_sizes))}
    title_size = max(level_map.keys())

    title = ""
    doc_headings = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = round(span["size"])

                    if size == title_size and title == "":
                        title = text
                    elif size in level_map and text:
                        doc_headings.append({
                            "text": text,
                            "level": level_map[size],
                            "page": page_num
                        })

    return {"title": title, "headings": doc_headings}
