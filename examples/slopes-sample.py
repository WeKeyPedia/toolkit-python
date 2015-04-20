# -*- coding: utf-8 -*-
import os
import codecs
import sys
import urllib
import json

from wekeypedia.wikipedia_page import WikipediaPage as Page, url2title, url2lang
from wekeypedia.wikipedia_network import WikipediaNetwork
from wekeypedia.exporter.nx_json import NetworkxJson

source = "List_of_geometry_topics"

hl = WikipediaNetwork("")
hl.keywords = hl.get_page_links(source)

hl.build()

exporter = NetworkxJson(hl.graph)
exporter.nx_export("adjacency", "_data/network.json")

# print hl.keywords
print ""

def fetch_page(source):
  print "📄  fetching: %s" % source.encode('utf-8-sig')

  p = Page()
  r = p.fetch_from_api_title(source.strip(), { "redirects":"true", "rvparse" : "true", "prop": "info|revisions", "inprop": "url", "rvprop": "content" })

  with open("path_points/%s.json" % (source), "w") as f:
    json.dump(r, f)

  with codecs.open("_path_points/%s.md" % (source), "w", "utf-8-sig") as file:
    file.write("---\n")

    # REWRITE ME
    result = r["query"]["pages"][r["query"]["pages"].keys()[0]]
    for k in result.keys():
      if k != "revisions":
        # print k
        # print result[k]

        content = result[k]

        if k == "fullurl":
          content = urllib.unquote(content)

        file.write("%s: %s\n" % (k, unicode(content)))

    file.write("---\n\n")

    if "revisions" in result.keys():
      file.write(result["revisions"][0]["*"])


# for k in hl.keywords:
#   fetch_page(k)