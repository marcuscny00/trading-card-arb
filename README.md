# trading-card-arb
mini project for scraping and interpreting market data for ever popular trading cards


Project Architecture
trading-card-arb/
│
├── README.md
├── .gitignore
├── pyproject.toml   (or requirements.txt)
│
├── notebooks/       ← exploratory, line-by-line
│   └── scraping_tests.ipynb
│
├── src/
│   ├── config/
│   │   └── sites.yaml
│   │
│   ├── scraping/
│   │   ├── base_scraper.py
│   │   ├── site_a.py
│   │   └── site_b.py
│   │
│   ├── data/
│   │   ├── schema.py
│   │   └── validation.py
│   │
│   ├── storage/
│   │   ├── spreadsheet.py
│   │   └── local_cache.py
│   │
│   ├── analysis/
│   │   └── price_diff.py
│   │
│   └── main.py
│
└── tests/
    └── test_scrapers.py


Data Collected (In SGD)
| timestamp | site | card_name | condition | grading | price | currency |
from the following sites
Pricecharting (and by extension Ebay)
Yuyutei

Data Pushed to Live Spreadsheet at (WEBSITE) using cron?
Scrape → normalize → validate
Store locally (CSV / SQLite)
Push batched updates to spreadsheet

Limitations