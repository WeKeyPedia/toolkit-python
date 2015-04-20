# -*- coding: utf-8 -*-
import os
import codecs
import sys
import urllib
import json

from wekeypedia.wikipedia_page import WikipediaPage as Page, url2title, url2lang
from wekeypedia.wikipedia_network import WikipediaNetwork
from wekeypedia.exporter.nx_json import NetworkxJson

from multiprocessing.dummy import Pool as ThreadPool

sources_file = "sources.txt"
pages_file = "pagenames.txt"

def sources_pages(sources):
  pages = []

  for s in sources:
    print s.strip()

    w = Page()
    w.fetch_from_api_title(s.strip())
    pages.extend(w.get_links())

  return list(set(pages))


sources = codecs.open(sources_file,"r", "utf-8-sig").readlines()

pages = sources_pages(sources)

# remove special pages
pages = [ p for p in pages if not(":" in p) ]
print len(pages)

pages = sorted(pages)

with codecs.open(pages_file,"w", "utf-8-sig") as f:
  for p in pages:
    f.write("%s\n" % (p))
  f.close()

# exit()

pages = codecs.open("pagenames.txt","r", "utf-8-sig").readlines()
pages = map(lambda x: x.strip(), pages)

def fetch_page(source):
  if os.path.exists("pages/%s.json" % (source)) == True:
    return

  print "📄  fetching: %s" % source.encode('utf-8-sig')

  p = Page()
  r = p.fetch_from_api_title(source.strip(), { "redirects":"true", "rvparse" : "true", "prop": "info|revisions", "inprop": "url", "rvprop": "content" })

  with codecs.open("pages/%s.json" % (source), "w", "utf-8-sig") as f:
    json.dump(r, f)

def fetch_revisions(source):
  if os.path.exists("revisions/%s.json" % (source)) == True:
    return

  print "📄  fetching revisions: %s" % source.encode('utf-8-sig')

  p = Page()
  p.fetch_from_api_title(source.strip())
  r = p.get_all_editors()

  with codecs.open("revisions/%s.json" % (source), "w", "utf-8-sig") as f:
    json.dump(r, f)  

def fetch_pageviews(source):
  if os.path.exists("pageviews/%s.json" % (source)) == False:
    print "📄  fetching pageviews: %s" % source.encode('utf-8-sig')

    p = Page()
    p.fetch_from_api_title(source.strip())
    r = p.get_pageviews()  

    with codecs.open("pageviews/%s.json" % (source), "w", "utf-8-sig") as f:
      json.dump(r, f)

# print pages

pool = ThreadPool(8)

for p in pages:
#  title = p["pagename"]
  title = p
  # fetch_page(p["pagename"])
  # fetch_revisions(p["pagename"])
  # fetch_pageviews(p["pagename"])

  pool.apply_async(fetch_page, args=(title,))
  pool.apply_async(fetch_revisions, args=(title,))

  # this one is particulary slow. skip it for demo purposes
  # pool.apply_async(fetch_pageviews, args=(title,))

pool.close()
pool.join()

