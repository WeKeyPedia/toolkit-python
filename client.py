# -*- coding: utf-8 -*-

import re
import os

from worker import store_revisions, store_last_revisions, dataset_blocks, dataset_timeline
from pymongo import MongoClient


mongodb_host = os.environ['MONGODB_PORT_27017_TCP_ADDR']

client = MongoClient("mongodb://%s/" % (mongodb_host))
db = client["datasets"]


def build_revisions():
  for page_url in open("/data/sources/wicrimea-seeds.extended.txt", "r"):
    print page_url.strip()
    store_revisions.delay(page_url.strip())

# regex = re.compile("|$([a-z]*)/(!/*)/revision/([0-9]*)$|")

def build_blocks():
  all_revisions = db.datasets.find({ "url": {"$regex": "^([a-z]*)\/(.*)\/revision\/([0-9]*)$" }})

  for revision in all_revisions:
    key =  "%s/blocks" % ( revision["url"] )

    test = db.datasets.find_one({ "url" : key })

    #print revision["url"].encode("utf8")

    if test is None:
      #print "... computing!"  
      #print revision["dataset"][0]["*"]
      dataset_blocks(revision["url"])

def build_timelines():
  for page_url in open("wicrimea-seeds.extended.txt", "r"):
    dataset_timeline.delay(page_url.strip())

def build_latest_blocks():
  all_timelines = db.datasets.find({ "url": {"$regex": "^([a-z]*)\/(.*)\/timeline$"} }, { "url": 1, "dataset" : { "$slice" : -1 }})

  for timeline in all_timelines:
    s =  timeline["url"].split("/")
    revid = timeline["dataset"][0]["revid"]
    url = "%s/%s/revision/%s" % (s[0], s[1], revid)

    print url.encode("utf8")

    rev = db.datasets.find_one({ "url": url })
    dataset_blocks.delay(url)

def build_last_revisions():
  all_timelines = db.datasets.find({ "url": {"$regex": "^([a-z]*)\/(.*)\/timeline$"} }, { "url":1 })

  for tl in all_timelines:
    url = tl["url"]
    print url.encode("utf8")

    # print tl["url"].encode("utf8")

    # lang =
    # page = 

#    print tl["dataset"][0]
    store_last_revisions.delay( url )  

# build_revisions()
# build_blocks()
# build_last_revisions()
# build_timelines()
build_latest_blocks()
