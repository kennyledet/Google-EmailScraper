'''
Copyright 2013 Kendrick Ledet

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

Google-EmailScraper

Purpose: Scraper that searches Google based on a query and scrapes all emails found on each page.
Output files are saved as csv.

Date: 5/26/13
'''
from xgoogle.search import GoogleSearch
import urllib2, re, csv, os
import argparse

class ScrapeProcess(object):
    emails = []  # for duplication prevention

    def __init__(self, filename):
        self.filename  = filename
        self.csvfile   = open(filename, 'wb+')
        self.csvwriter = csv.writer(self.csvfile)

    def go(self, query, pages):
        search = GoogleSearch(query)
        search.results_per_page = 10

        for i in range(pages):
            search.page = i
            results = search.get_results()
            for page in results:
                self.scrape(page)
            
    def scrape(self, page):
        try:
            request = urllib2.Request(page.url.encode("utf8"))
            html    = urllib2.urlopen(request).read()
        except Exception, e:
            return

        emails = re.findall(r'([A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*)', html)

        for email in emails:
            if email not in self.emails:  # if not a duplicate
                self.csvwriter.writerow([page.title.encode('utf8'), page.url.encode("utf8"), email])
                self.emails.append(email)

parser = argparse.ArgumentParser(description='Scrape Google results for emails')
parser.add_argument('-query', type=str, default='test', help='a query to use for the Google search')
parser.add_argument('-pages', type=int, default=10, help='number of Google results pages to scrape')
parser.add_argument('-o', type=str, default='emails.csv', help='output filename')

args   = parser.parse_args()
args.o = args.o+'.csv' if '.csv' not in args.o else args.o  # make sure filename has .csv extension

s = ScrapeProcess(args.o)
s.go(args.query, args.pages)