import urllib
import re
def songspk(movie_name):
    movie_name = "_".join(movie_name.split())
    print movie_name
    first_char = movie_name[0:1]
    movie_list_url = "http://www.songspk.pk/" + first_char.lower()+"_list.html"
    source = urllib.urlopen(movie_list_url).read()
    reg = "http://www.songspk.pk/.*"+movie_name.lower()+".*.html"
    print reg
    regex = re.compile(reg)
    list  = regex.findall(source)
    print list
    print list[0]
    movie_page_source = urllib.urlopen(list[0]).read()
    reg_song_name = "http://link[0-9]*\.songspk\.pk/song[0-9]*\.php\?songid=[0-9]*"
    regex_2 = re.compile(reg_song_name)
    list_2 = regex_2.findall(movie_page_source)
    print list_2
    count=2
##    for i in list_2:
##        urllib.urlretrieve(i, "C:\\"+movie_name+"song_"+str(count)+".mp3")
##        count=count+1
songspk("Jism 2")