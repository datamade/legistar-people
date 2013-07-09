OpenGovernment.org Legistar Importer 

Uses [Legistar Scraper](https://github.com/fgregg/legistar-scrape) - a python library for scraping [Legistar sites](http://www.granicus.com/Legistar/Product-Overview.aspx) 
-- legislation management sites hosted by by [Granicus](http://www.granicus.com/Streaming-Media-Government.aspx).

## Installation

```console
git clone git://github.com/opengovernment/opengovernment-legistar-scrape.git
cd opengovernment-legistar-scrape
virtualenv .env --no-site-packages
source .env/bin/activate
pip install -r requirements.txt
```

## Usage

```console
python import.py
```