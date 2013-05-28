Google-EmailScraper
===================

This is a scraper that searches Google based on a query and scrapes all
emails found on each page Google finds.

Requirements
------------
* Python 2.6+

Instructions
------------
To use this scraper, you'll need to run main.py with Python and pass in
the following arguments

* -query (this is what we're telling Google to search for)
* -pages (number of Google search results pages we should scrape)
* -o     (output filename) 

Example
-------
```
python main.py -query "adoption agency email" -pages 10 -o emails.csv
```
