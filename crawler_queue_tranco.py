"""Schedule crawling jobs
Usage:
    crawler_queue_tranco.py
    crawler_queue_tranco.py -i <indirflag>
    crawler_queue_tranco.py -i <indirflag> -s <starturl> -e <endurl>
"""

import os
from typing import List, Dict
from docopt import docopt
import json

LAST_EXTENSION = -1  # set to ```-1``` if you want to run all extensions available

ZERO = 0
MAX_URLS = 12
URLS_VISITED = [
    "https://example.com",
    "https://google.com",
    "https://cnn.com",
    "https://ebay.com",
    "https://facebook.com",
    "https://amazon.com",
    "https://tiktok.com",
    "https://youtube.com",
    "https://twitter.com",
    "https://apple.com",
    "https://microsoft.com",
    "https://example.net/",
]
SLEEP_EVERY = 13
SLEEP_FOR_HOW_MANY_SECONDS = 60  # used to be 60 initially


def main(arguments, urls: List[str] = URLS_VISITED):
    with open("tranco/tranco10.txt", "r") as f:
        tranco_file = f.read()

    # Split the data into lines
    lines = tranco_file.split("\n")

    # Process each line to remove the number and the first comma
    tranco_top_x = [line.split(",", 1)[1] for line in lines]

    for url in tranco_top_x:
        print(url)
        timeout = "-t 120"
        cmd = f"python3 ./scripts/vv8-cli.py crawl -pp Mfeatures --no-headless --show-chrome-log  --disable-screenshot --disable-artifact-collection --disable-har  --disable-gpu --disable-features=NetworkService --js-flags='--no-lazy' {timeout} -u {url}"
        print(cmd)
        os.system(cmd)


def load_urls(json_file: str) -> Dict[str, List[str]]:
    with open(json_file, "r") as fout:
        data = json.load(fout)
    return data


if __name__ == "__main__":
    arguments = docopt(__doc__, version="Schedule jobs on vv8+fv8 crawler 1.0")
    main(arguments)
