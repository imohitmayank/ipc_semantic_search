# IPC Semantic Search

Steps:
- Scrap the `devgan.in` website to get the different sections in IPC
- Use `LegalBERT` to get the embeddings of the descriptions of the IPC sections
- Perform Cosine Similarity to get the nearest matching section wrt query.

Code:
- `devganscrap`: Scrapy code to crawl and extract IPC sections and their description from the `devgan.in`

Data Credits:
- http://devgan.in
