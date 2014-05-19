from celery import Celery

import os

from wekeypedia.wikipedia_page import WikipediaPage as Page, url2title, url2lang
from wekeypedia.parser.mediawiki import Mediawiki as mw
from wekeypedia.dataset import Dataset


rabbitmq_host = os.environ['RABBITMQ_PORT_5672_TCP_ADDR']
mongodb_host = os.environ['MONGODB_PORT_27017_TCP_ADDR']

BROKER_URL = 'amqp://worker:98b4840644@%s:5672/worker'  % (rabbitmq_host)
RESULTS_URL = 'mongodb://%s:27017//' % (mongodb_host)

print "broker host: %s" % (BROKER_URL)
print "results host: %s" % (RESULTS_URL)

app = Celery(broker=BROKER_URL)

app.conf.update(
#  CELERY_BROKER_URL=BROKER_URL,
  CELERY_RESULT_BACKEND=RESULTS_URL,
  CELERY_ACCEPT_CONTENT = ['application/json'],
  CELERY_TASK_SERIALIZER = "json"
)

@app.task
def dataset_timeline(url):
  print "timeline: %s" % (url)
  d = Dataset( "%s:27017" % (mongodb_host) )

  title = url2title(url)
  lang = url2lang(url)

  regex_string = "%s\/%s\/revision/([0-9]*$)" % (lang, title)

  r = d.find({ "url" : { "$regex" : regex_string } }, { "dataset.timestamp" : 1, "dataset.revid" : 1 })

  timeline = []

  for result in r:
    i = { "timestamp": result["dataset"][0]["timestamp"], "revid": result["dataset"][0]["revid"] }
    timeline.append(i)

  timeline = sorted( timeline, key=lambda rev: rev["timestamp"])

  print "start: %s" % (timeline[0])
  print "end: %s" % (timeline[-1])

  k = "%s/%s/timeline" % (lang, title)
  d.write(k, timeline)

  print r.count()


@app.task()
def dataset_blocks(url):
  print "blocks: %s" % (url)
  d = Dataset( "%s:27017" % (mongodb_host) )

  page = d.read(url)

  txt = mw(page["dataset"][0]["*"])

  (blocks, structure) = txt.get_blocks()

  key = "%s/blocks" % (url)
  value = {  "structure" : structure, "blocks": blocks }

  d.write(key, value)

  return value

@app.task(bind=True)
def store_revisions(self, page_url):
  """
  Retrieve all the revision of a give wikipedia page_url

  parameters:
    - page_url: a wikipedia page URL
  """

  p = Page()

  d = Dataset( "%s:27017" % (mongodb_host) )

  title = url2title(page_url)
  lang = url2lang(page_url)

  p.fetch_from_api_title(title, lang=lang)

  revisions = p.get_all_editors()

  i = 0

  for revision in revisions:
    i += 1

    # ex: en/crimea/revision/999999
    key = "%s/%s/revision/%s" % (lang,title,revision["revid"])

    # fetch the revision from the internet
    value = p.get_revisions(extra_params={ "rvstartid": revision["revid"], "rvlimit" : 1})

    # write in it the database handler
    d.write(key, value)
    self.update_state( state='PROGRESS',
      meta= { 'current': i, 'total': len(revisions)})