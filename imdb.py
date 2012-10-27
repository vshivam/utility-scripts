import urllib2
from BeautifulSoup import BeautifulSoup
import re
import sys

def parse_tag(tag_to_parse):
        index_begin = tag_to_parse.find(">")
        index_end = tag_to_parse.find("<", index_begin)
        return tag_to_parse[index_begin+1:index_end] 

class Imdb:
    def __init__(self, name):
        name = name.split()
        url = '+'.join(name)
        prefix = "http://www.imdb.com/find?q="
        suffix = "&s=all"
        search_url = prefix+url+suffix;

        http_proxy_full_auth_string = "http://%s:%s@%s:%s" % ('username','password','proxy_server','port')
        proxy_handler = urllib2.ProxyHandler({"http": http_proxy_full_auth_string})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        search_result = urllib2.urlopen(search_url).read()
        
        title = re.search(r'/title/tt[0-9]*/', search_result)
        movie_url = "http://imdb.com"+title.group(0)
        self.movie_source = urllib2.urlopen(movie_url).read()

        self.soup = BeautifulSoup(self.movie_source)
    
    def get_rating(self):
        self.rating = self.soup.findAll("span", itemprop="ratingValue")
        for i in self.rating:
            print (''.join(i.findAll(text=True)))

    def get_voters(self):
        self.voters = self.soup.findAll("span", itemprop="ratingCount")
        for i in self.voters:
            print (''.join(i.findAll(text=True)))

    def get_directors(self):
        self.directors = self.soup.findAll("a", itemprop="director")
        for i in self.directors:
            print (''.join(i.findAll(text=True)))

    def get_actors(self):
        self.actors = self.soup.findAll("a", itemprop="actors")
        for i in self.actors:
            print (''.join(i.findAll(text=True)))

    def get_storyline(self):
        index_begin = self.movie_source.find("<h2>Storyline</h2>")
        index_storyline = self.movie_source.find("<p>", index_begin)
        index_end = self.movie_source.find("<em", index_storyline+1)
        print self.movie_source[(index_storyline+3):index_end]

movie_name = sys.stdin.readline()
imdb = Imdb(movie_name)
print "\nRating :" 
imdb.get_rating()
print "\nVoters :"
imdb.get_voters()
print "\nDirectors :"
imdb.get_directors()
print "\nActors :"
imdb.get_actors()
print "\nStoryline :"
imdb.get_storyline()


