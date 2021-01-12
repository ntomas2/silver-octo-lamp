import argparse
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
import colorama

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here


parser = argparse.ArgumentParser(description="taking directory")
parser.add_argument("directory", help="Give directory for caching pages")
args = parser.parse_args()

# if os.access(args.directory, os.F_OK):
if not os.path.exists(args.directory):
    os.mkdir(args.directory)
# os.makedirs(yourDir, exist_ok=True) to avoid FileExistError

page_stack = deque()


def page_call(page_url):
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    content = colorama.Fore.BLUE + soup.get_text()
    print(content)
    page_stack.append(content)
    pagesplit = page_url.lstrip('https://').split('.')
    pagename = ".".join(pagesplit[:-1])
    with open(os.path.join(args.directory, pagename), 'w') as f:
        for line in content:
            f.write(line)


while True:
    inp = input()
    if inp == "exit":
        break
    elif inp == "back" and len(page_stack) > 1:
        page_stack.pop()
        print(page_stack.pop())
    # elif inp in os.listdir(args.directory)
    elif os.access(os.path.join(args.directory, inp), os.R_OK):
        with open(os.path.join(args.directory, inp), 'r') as rf:
            for line in rf:
                print(line)
    elif "." not in inp:
        print("error: no valid url")
    elif not inp.startswith('https://'):
        page_url = 'https://' + inp
        page_call(page_url)
    else:
        page_url = inp
        page_call(page_url)
