# IPC Semantic Search

**What:**
- The Indian Penal Code (IPC) is the official criminal code of India. [Wikipedia](https://en.wikipedia.org/wiki/Indian_Penal_Code)
- The intention behind this project is to provide an interfact for a common layman to search IPC sections.

**Steps:**
- Scrap the `devgan.in` website to get the different sections in IPC
- Use `LegalBERT` to get the embeddings of the descriptions of the IPC sections
- Perform Cosine Similarity to get the nearest matching section wrt query.

**Code:**
- `devganscrap`: Scrapy code to crawl and extract IPC sections and their description from the `devgan.in`

**Data:**
- `devagnscrp/sections_desc.csv`: IPC sections and descriptions *(Data Credits: http://devgan.in)*
