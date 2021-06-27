from scrapers import indeed_scraper 
from scrapers import linkedIn_scraper

def run(job, location):
    if job == None:
        print('\n')
        job = input("Enter the job: ")
    if location == None:
        location = input("Enter the location: ")
    print("\n\tWorking with Indeed scraper")
    indeed_scraper.run(job, location)
    print("\n\tWorking with LinkedIn scraper")
    linkedIn_scraper.run(job, location)