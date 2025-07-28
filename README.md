# PDF Outline Extractor

Extracts the title and headings (H1, H2, H3) from a PDF and outputs JSON.

## How to Run (Offline, Dockerized)

1. Clone or copy files into a folder
2. Place a PDF as `sample.pdf` in the same folder
3. Build Docker image:
```bash
docker build -t pdf-outline-extractor .
