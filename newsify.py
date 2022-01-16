#!/usr/bin/env python3
import feedparser
import time
import sys
import rich
if len(sys.argv) > 1:
    newsfeed = sys.argv[1]
    keyword = sys.argv[2]
    newsfeed = feedparser.parse(newsfeed)
for i in range(5):
    if keyword in newsfeed['entries'][i]['title']:
        rich.print("[blink green on white]Keyword found[/blink green on white]")
        print(newsfeed['entries'][i]['title'])
        print(newsfeed['entries'][i]['link'])
        print("\n")
    else:
        print(newsfeed['entries'][i]['title'])
