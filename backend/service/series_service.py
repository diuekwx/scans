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
    {"name": "HiveToon", "type": "direct", "base_url": "https://hivetoons.org", "query_url": "https://hivetoons.org/series/"},
    {"name": "VortexScans", "type": "direct", "base_url": "https://vortexscans.org", "query_url": "https://vortexscans.org/series/"}
]

def external_query(title: str, db: Session = Depends(get_db)):
    res = []

    encoded_title = urllib.parse.quote(title)
    
    for source in SOURCES:
        if source["type"] == "scraper":
            href = scraper(source["base_url"], encoded_title, source["query_url"], title)
            if href is None:
                continue
        else:
            print("LOL")
            href = no_query(source["base_url"], source["query_url"], title)
            if href is None:
                continue
            
        if not any (d["source"] == source["name"] for d in res):
            res.append({
                "source": source["name"],
                "link": href
            })
    return res

def scraper(base_url: str, encoded_title: str, query_url: str, title: str):
    url = query_url + encoded_title
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # hasve anther check that the tiile matches exactly wtf is webtoon printing out LOL.
    found = soup.find_all(string=re.compile(re.escape(title), re.IGNORECASE))
    for match in found:
        href = find_parent(match)
        print(base_url)
        if href: 
            if base_url not in href:
                print("base")
                return base_url + href
            else:
                print(href)
            return href
    return None

def no_query(base_url: str, query_url: str, title: str):
    replaced_title = title.replace(" ", "-")
    url = query_url + replaced_title
    r = requests.get(url, allow_redirects=True)
    if r.url.rstrip("/") == base_url.rstrip("/"):
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    print(f" soup {soup}")
    return url

def find_parent(element):
    parent = element
    while parent:
        parent = parent.parent
        if parent and parent.name == "a":
            return parent.get("href")
    return None
