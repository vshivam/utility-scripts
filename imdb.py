import urllib2
from BeautifulSoup import BeautifulSoup
import re

def imdb(movie_name):
    movie_name= movie_name.split()
    movie_url='+'.join(movie_name)
    url_pref = "http://www.imdb.com/find?q="
    url_suf = "&s=all"
    imdb_url = url_pref+movie_url+url_suf;
    print imdb_url
    source = urllib2.urlopen(imdb_url).read()
    title = re.search(r'/title/tt[0-9]*/', source)
    movie_url = "http://imdb.com"+title.group()
    movie_source = urllib2.urlopen(movie_url).read()
    print "Movie Page Fetched"
    soup = BeautifulSoup(movie_source)
    rating = soup.findAll("span", itemprop="ratingValue")
    for node in rating:
        print "Rating: " + (''.join(node.findAll(text=True)))+"/10"
    voters = soup.findAll("span", itemprop="ratingCount")
    for node in voters:
        print "Number of Voters: "+''.join(node.findAll(text=True))
    desc = soup.findAll("p", itemprop="description")
    for node in desc:
        print "Description: "+(''.join(node.findAll(text=True)))

movie_name = raw_input()
imdb(movie_name)

