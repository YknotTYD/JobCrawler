from seleniumwire import webdriver
from selenium_stealth import stealth
from fake_useragent import UserAgent

import gzip
import brotli
import json

import time
import parse_json

ua = UserAgent()
options = webdriver.ChromeOptions()

options.add_argument(f"user-agent={ua.random}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

driver.get("https://epitech.jobteaser.com/fr/companies/bouygues-telecom/job-offers?page=1")
time.sleep(5)

for r in driver.requests:

    if r.response and "search-dsn.jobteaser.com/1/indexes" not in r.url:
        continue

    body = r.response.body
    body = gzip.decompress(body)
    text = body.decode('utf-8', errors='ignore')
    data = json.loads(text)

    print(parse_json.parse_json_pages(data))

driver.quit()
