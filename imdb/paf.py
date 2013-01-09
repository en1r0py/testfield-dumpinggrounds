import lxml.html.soupparser
import lxml.etree

def somejazz():
    scontents = "<html><body></body></html>"
    doc_html = lxml.html.soupparser.fromstring(scontents)
    print doc_html
    

somejazz()
