How You Should Work Daily for every session

Open VS Code
Open the project folder
Activate .venv (VS Code usually auto-does it)
Code
Commit & push when something works

Leave .venv
deactivate
prompt will change to PS

Nuke venv
rmdir /s /q .venv

Recreate venv
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

1️⃣ README.md (Non-Optional)
What it does
Explains what the project is
Explains what problem it solves
Explains how data flows
Beginner rule
Write it in plain English
No math, no jargon
Example content

“This project scrapes trading card prices from multiple sites every few hours and stores historical price data to compare spreads and grading differences.”

This is what interviewers read first.

2️⃣ notebooks/playground.py (Your Safe Space)
What it is
Your scratchpad
Line-by-line execution
Debugging
Learning Python
What goes here
Trying out one scraper
Printing raw HTML
Testing parsing logic
Quick calculations

What NEVER goes here
❌ Final logic
❌ Scheduled jobs
❌ Production code

Think of it like rough work on paper.

3️⃣ config/sites.yaml (Configuration, Not Code)

What it does

Stores site-specific values

URLs

Pagination rules

Currency

Headers (eventually)

Why this matters

You don’t hard-code site details

Easier to add/remove sites

Less copy-paste

Beginner mental model

“If I change this, I shouldn’t touch Python code.”

4️⃣ scrapers/ (Where Data Comes From)
scrapers/base.py

What it does

Defines what a scraper must do

NOT how scraping works

Think of it as a template.

Example responsibilities

“Every scraper must return price data”

“Every scraper must handle errors”

What not to put here
❌ Site-specific logic
❌ URLs
❌ Parsing rules

scrapers/site_a.py, site_b.py

What they do

One file = one website

Fetch HTML

Extract prices

Clean messy text

Beginner rule

If two websites work differently → they get different files.

What they return

Clean, structured data

No printing

No saving to files

5️⃣ models/price_record.py (Your Data Shape)

This is VERY important.

What it does

Defines what one price entry looks like

Instead of random dictionaries everywhere, you have one standard format.

Beginner explanation

“This is what one row in my spreadsheet means.”

Fields like:

timestamp

site

card name

raw vs graded

grade value

price

Why this helps beginners

Less confusion

Easier analysis later

Fewer bugs

6️⃣ storage/ (Where Data Is Saved)
storage/local_store.py

What it does

Saves data locally (CSV or SQLite)

Acts as a backup

Lets you re-run analysis

Why not save directly to Google Sheets

APIs fail

Rate limits

Debugging pain

Local storage = safety net.

storage/sheets.py

What it does

Uploads cleaned data to Google Sheets

Handles authentication

Knows nothing about scraping

Beginner rule

Storage should never scrape.
Scrapers should never upload.

This separation is professional.

7️⃣ analysis/compare_prices.py (Thinking Happens Here)

What it does

Compare prices across sites

Compare raw vs graded

Calculate spreads

What it does NOT do
❌ Scraping
❌ Saving files
❌ Scheduling

It only:

Takes data in

Produces insights out

8️⃣ run.py (The Orchestrator)

This is the only file you run in production.

What it does

Calls scrapers

Collects results

Saves data

Triggers analysis

Beginner mental model

“This is the big red START button.”

Later:

Cron runs this

GitHub Actions runs this

9️⃣ tests/ (Don’t Fear This)

You will barely use this at first.

What it’s for

Making sure scraping still works

Detecting site changes

Preventing silent failure

Beginner reassurance

Tests come later

Even basic checks help

IMPORTANT Beginner Rules (Memorise These)

One responsibility per file

No copying logic between files

Notebooks = experiments only

Scrapers return data, not files

run.py is the only entry point

