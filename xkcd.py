import urllib
def xkcd_latest():
    source = urllib.urlopen('http://xkcd.com/').read()
    url_start = source.find('img src="http://imgs.xkcd.com/comics/')
    start_quote = source.find('"',url_start)
    end_quote = source.find('"',start_quote+1)
    url=source[start_quote+1:end_quote]
    file_name = url[28:end_quote]
    print file_name
    print url
    image_file = urllib.urlretrieve(url, "C:\\Python\\xkcd\\"+file_name)
xkcd_latest()