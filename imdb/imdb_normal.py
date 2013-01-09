import urllib2
import lxml.html.soupparser
import lxml.etree

def get_page(sURL):
    opener = urllib2.urlopen(sURL)
    return opener.read()

def write_page_to_file(sfilename, scontents):
    try:
        f = open(sfilename,"wt")
        try:
            f.write(scontents)
        finally:
            f.close()
    except IOError:
        pass

def another_grab(scontents):
    tree = lxml.html.soupparser.fromstring(scontents)

def grab_movies_on_page(scontents):
    doc_html = lxml.etree.HTML(scontents)
    body = doc_html.xpath("/html/body")
    print body
    #tree = etree.parse(scontents)
    #r = tree.xpath("/html/body")
    ##doc_html = lxml.html.soupparser.fromstring(scontents)
    pass

def iterate_for_x_movies(start_url, total_movies):
    movie_count = 1
    l = []

    while movie_count < total_movies:
        current_url = start_url + str(movie_count)
        s_htmlcontents = get_page(current_url)

        l_new = grab_movies_on_page(s_htmlcontents)
        l.extend(l_new)
        movie_count += len(l_new)

    return l


if __name__ == "__main__":
    #TOTAL_MOVIES = 694896
    """
    TOTAL_MOVIES = 150
    START_URL = "http://www.imdb.com/search/title?languages=en&start="

    iterate_for_x_movies(START_URL, TOTAL_MOVIES)
    """
    START_URL = "http://www.imdb.com/search/title?languages=en&start="
    s_html = get_page(START_URL + str(1))
    another_grab(s_html)
















