Legistar People Scraper

Scrapes the [People.aspx](chicago.legistar.com/People.aspx/) page on a given list of Legistar sites and saves to a CSV.



Uses [Legistar Scraper](https://github.com/fgregg/legistar-scrape) - a python library for scraping [Legistar sites](http://www.granicus.com/Legistar/Product-Overview.aspx) 
-- legislation management sites hosted by by [Granicus](http://www.granicus.com/Streaming-Media-Government.aspx).

## Installation

```console
git clone git://github.com/datamade/legistar-people.git
cd legistar-people
pip install -r requirements.txt
```

Copy over the settings file and update with your parameters
```console
cp settings.py.example settings.py
```

## Usage

Save all people listed on given Legistar sites to a csv.
```console
python import.py
```