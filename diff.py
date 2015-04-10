import wekeypedia

import nltk

import pandas as pd

from bs4 import BeautifulSoup

from collections import defaultdict
from multiprocessing import Pool as ThreadPool

import codecs
import json


ignore_list = "{}()[]<>./,;\"':!?&#"

lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()

# page =  "Michel Maffesoli"
# page =  "Love"
# page = "War"
page = "Wisdom"

p = wekeypedia.WikipediaPage()
p.fetch_from_api_title(page)

added = defaultdict(dict)
deleted = defaultdict(dict)

inflections = {}
inflections["added"] = defaultdict(set)
inflections["deleted"] = defaultdict(set)

def get_revs():
  revisions = p.get_revisions_list()

  return revisions

def red(r):
  a = r[0]
  d = r[1]
  i = r[2]

  for s in ["added" , "deleted"]:
    for w in i[s]:
      inflections[s][w] |= i[s][w]

  for w, c in a:
    if not("count" in added[w]):
      added[w]["count"] = 0

    added[w]["count"] += c
    added[w]["inflections"] = ", ".join(list(inflections["added"][w]))

  for w, c in d:
    if not("count" in deleted[w]):
      deleted[w]["count"] = 0

    deleted[w]["count"] += c
    deleted[w]["inflections"] = ", ".join(list(inflections["deleted"][w]))

def normalize(word):
  # old = word
  word = word.lower()
  word = stemmer.stem_word(word)
  word = lemmatizer.lemmatize(word)
  # print word
  return word

def count(a, sentence, which):
  for w in nltk.word_tokenize(sentence):
    old = w
    w = normalize(w)
    if not(w in ignore_list):
      inflections[which][w] = inflections[which][w] | set([ old ])
      a[w] += 1

def rev_diff(revid):
  ad = defaultdict(int)
  de = defaultdict(int)

  d = p.get_diff(revid)

  # bug with Ethics#462124891
  if d == False:
    return ({},{}, { "added": [], "deleted": [] })

  d = BeautifulSoup(d, 'html.parser')

  # check additions of block
  addedlines = d.find_all("td", "diff-addedline")
  for tag in addedlines:
    inner = tag.find_all("ins")

    # check that there is no inner addition
    if len(inner) == 0:
      count(ad, tag.get_text(), "added")

  ins_tags = d.find_all("ins")

  for txt in map(lambda x: x.get_text(), ins_tags):
    count(ad, txt, "added")

  deletedline = d.find_all("td", "diff-deletedline")
  for tag in deletedline:
    inner = tag.find_all("del")

    if len(inner) == 0:
      count(de, tag.get_text(), "deleted")

  del_tags = d.find_all("del")

  for txt in map(lambda x: x.get_text(), del_tags):
    count(de, txt, "deleted")

  print("%s %s|%s" % (revid, "+"*len(ad), "-"*len(de)))

  return (ad.items(),de.items(), { "added":inflections["added"], "deleted":inflections["deleted"] })


def write_revdif(revid):
  
  data = p.get_diff_full(revid)
  name = "data/%s/%s.json" % (page, revid)
  
  data = data["query"]["pages"][list(data["query"]["pages"].keys())[0]]
  
  if "diff" in data["revisions"][0]:
    data = data["revisions"][0]
    print revid
    with codecs.open(name, "w", "utf-8-sig") as f:
      json.dump(data, f, ensure_ascii=False, indent=2, separators=(',', ': '))

# print len(rev_list)
# print p.get_diff(rev_list[0]["revid"])
# print [ x["revid"] for x in rev_list ]
# print rev_diff(462124891)
# exit()

rev_list = get_revs()

pool = ThreadPool(4)

#result = pool.map(rev_diff, [ x["revid"] for x in rev_list ])
pool.map(write_revdif, [ x["revid"] for x in rev_list ])

# for r in rev_list:
#   rev_id = r["revid"]
#   # pool.apply_async( rev_diff, args=(rev_id, ), callback=red )
#   red(rev_diff(rev_id))

pool.close()
pool.join()

exit()

print "## reduce results"
for r in result:
  red(r)

# print added

print "## save consolidated data"
#df1 = pd.DataFrame.from_dict(added, orient="index")
df1 = pd.DataFrame([ [ x[1]["count"], x[1]["inflections"] ] for x in added.iteritems() ], index=added.keys())
df1.columns = [ 'count', 'inflections']
df1.to_csv("added.csv", encoding="utf8")

#df2 = pd.DataFrame.from_dict(deleted, orient="index")
df2 = pd.DataFrame([ [ x[1]["count"], x[1]["inflections"] ] for x in deleted.iteritems() ], index=deleted.keys())
df2.columns = ['count', 'inflections']
df2.to_csv("deleted.csv", encoding="utf8")