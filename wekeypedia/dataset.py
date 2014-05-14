from pymongo import MongoClient

import json

class Dataset():
  def __init__(self, mongo_conf):
    client = MongoClient("mongodb://%s/" % (mongo_conf))

    self.db = client["datasets"]

  def write(self, key, value):
    # print key
    # print json.JSONEncoder().encode(value)

    item = {
      "url": key,
      "dataset": value
    }

    self.db.datasets.insert(item)