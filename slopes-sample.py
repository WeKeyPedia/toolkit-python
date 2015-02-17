# -*- coding: utf-8 -*-
import os
import sys

from wekeypedia.wikipedia_page import WikipediaPage as Page, url2title, url2lang


if len(sys.argv) > 1:
  source = sys.argv[1]

  print ""
  print "📄  fetching: %s" % source

  p = Page()
  r = p.fetch_from_api_title(source.strip(), { "prop": "info|revisions", "inprop": "url", "rvprop": "content" })

  with open("%s.md" % (source), "w") as file:
    file.write("---\n")

    # REWRITE ME
    result = r["query"]["pages"][r["query"]["pages"].keys()[0]]
    for k in result.keys():
      if k != "revisions":
        file.write("%s: %s\n" % (k, result[k]))

    file.write("---\n\n")

    file.write(result["revisions"][0]["*"].encode('utf-8'))