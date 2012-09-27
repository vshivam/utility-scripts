import os
import urllib2
from BeautifulSoup import BeautifulSoup
import re

def imdb(movie_name):
    http_proxy_full_auth_string = "http://%s:%s@%s:%s" % ('f2009680','password','10.1.9.20','8080')
    proxy_handler = urllib2.ProxyHandler({"http": http_proxy_full_auth_string})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
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
        return (''.join(node.findAll(text=True)))

filenames = os.listdir("E:\\Share\\Movies\\")
print filenames

for i in filenames:
    new_name = i
    (filepath,filename)= os.path.split(i)
    imdb_loc = filename.find("IMDB")
    if(imdb_loc==-1):
        loc=filename.find('[')
        #print "loc_1"+str(loc)
        if(loc!=-1):
            new_name = filename[:(loc)]
            print new_name
        loc=new_name.find('(')
        #print "loc_2"+str(loc)
        if(loc!=-1):
            new_name=new_name[:loc]
            print new_name
        new_name= new_name.replace('.',' ')
        name = new_name.split()
        final_name =''
        for i in name:
            i=i.capitalize()
            final_name=final_name+i+" "
        print final_name
        rating = imdb(final_name)
        print rating
        os.rename("E:\\Share\\Movies\\"+filename,"E:\\Share\\Movies\\"+final_name+"[IMDB - "+rating+"]")




