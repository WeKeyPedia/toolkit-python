# -*- coding: utf-8 -*-

import sys

import pprint

from  wekeypedia.parser.mediawiki import Mediawiki as mw
from  wekeypedia.parser.dataset import Dataset

mw_content = "yo"

pp = pprint.PrettyPrinter(indent=2)

if len(sys.argv) > 2:
  d = Dataset("/Users/tk/datasets/wicrimea")

  page = sys.argv[1]
  revision = sys.argv[2]

  mw_content = d.get_revision_content(page, revision) 

  #  print mw_content

txt = mw(mw_content)

#print unicode(txt.text)
#pp.pprint(txt.text.nodes)

headings = txt.get_headings()

for h in headings:
  print ("  " * (h.level - 2)) + str(h.title)

print "—"*10

blocks = txt.get_blocks()

print blocks