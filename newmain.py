import time
import feedparser
from art import tprint

tprint("RSS-PARSER", font='bulbhead')
while True:
    with open('links.txt', 'r') as t:
        lines = t.readlines()

    for i in range(len(lines)):
        Feed = feedparser.parse(lines[i])
        pointer = Feed.entries[0]
        with open('upload.txt') as u:
            lines1 = u.read()
        if pointer.summary not in lines1:
            with open('upload.txt', 'a') as u:
                u.write(f'{pointer.link}  ------->  {pointer.summary} \n')
        else:
            pass
    print('Last time check - ', time.asctime())
    time.sleep(299)