import lxml.html.soupparser
import lxml.etree

scontents = (open("freshdump.txt","r")).read()
open("freshdump2.txt","w").write(lxml.etree.tostring(lxml.html.soupparser.fromstring(scontents)))
