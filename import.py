from legistar.scraper import LegistarScraper
from legistar.config import Config, DEFAULT_CONFIG
import settings
import datetime
import csv

# Configure and create a scraper

csv_headers = ["Municipality","Person Name","E-mail","Web Site"]

with open('legistar-people.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

  writer.writerow(csv_headers)
    
  for scraper_target in settings.SCRAPER_TARGETS: 

    print "Municipality:", scraper_target['municipality']
    print "Endpoint:", scraper_target['endpoint']

    config = Config(
      hostname = scraper_target['endpoint'],
      fulltext=True,
    ).defaults(DEFAULT_CONFIG)
    scraper = LegistarScraper(config)

    # get all agenda items
    members_list = scraper.councilMembers(follow_links=False)

    try:
      for member in members_list:
        member['Municipality'] = scraper_target['municipality']
        # member['Created Date'] = datetime.datetime.utcnow()

        row = []
        for col in csv_headers:
          extracted_val = ''
          if col in member.keys():
            if type(member[col]) == dict:
              extracted_val = member[col]['label']
            else:
              extracted_val = member[col]

          row.append(extracted_val.encode('utf-8'))

        print row
        writer.writerow(row)

    except:
      print "Failed to scrape!"