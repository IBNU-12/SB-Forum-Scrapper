import click
import urllib.request
from bs4 import BeautifulSoup

from setuptools import setup

@click.command()
@click.option('--user',help = "Specifies to only scrape posts from that user")
@click.option('--pages',default = 1,help = 'The number of pages to scrape')
@click.argument('url',type = str,)
def cli(user,pages,url):
    """ This script is designed to help scrape xeno-forum posts. Type the words
    Hello along with a url to scrape the page."""
    for i in range(1,pages + 1):
        thread = urllib.request.urlopen((url + 'page-{}').format(i)).read()
        page = BeautifulSoup(thread,'lxml')
        posts = page.find_all('li',{"class" : "message"}) # extracts the post from the background of the website
        if user:
            for post in posts :
                author = str(post["data-author"]) # Turns the author of the post into a comparable string
                post_text = post.find('div',{"class" : "messageContent"}) # Verifies it's authority
                if (author == user): # Checks if it's long enough to be let's read
                    print (post_text.text)
                    print ("*" * 30) # Seperates Posts

        else:
            for post in posts:
                post_text = post.find('div',{"class" : "messageContent"})
                print (post_text.text)
                print ("*" * 30) # Seperates Posts
