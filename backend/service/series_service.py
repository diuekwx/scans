from fastapi import Depends
from sqlalchemy.orm import Session
from backend.db.session import get_db 
from backend.models.db_series import Series
from bs4 import BeautifulSoup
import urllib.parse
import requests 
import re

def search(title: str, db: Session = Depends(get_db)):
    series = db.query(Series).filter(Series.title.ilike(f"%{title}")).first()
    return series

SOURCES = [
    {"name": "asuracomic", "type": "scraper", "base_url": "https://asuracomic.net/", "query_url": "https://asuracomic.net/series?page=1&name="},
    {"name": "Webtoon", "type": "scraper", "base_url": "https://www.webtoons.com", "query_url": "https://www.webtoons.com/en/search?keyword="},
]

def external_query(title: str, db: Session = Depends(get_db)):
    res = []
    title = urllib.parse.quote(title)
    for source in SOURCES:
        url = source["query_url"] + title
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        found = soup.find_all(string=re.compile(title, re.IGNORECASE))
        if found:
            res.append({
                "source": source["name"],
                "url": source["query_url"]
            })
        print(found)
    return res

        
        
