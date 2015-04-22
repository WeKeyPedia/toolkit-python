****************************************
Make custom queries to the wikipedia api
****************************************

Le toolkit wekeypedia inclut une classe qui permet de passer des requêtes
plus fines et adaptées à des recherches d'information spécifiques et peu
généralisables. Par exemple, la plupart des classes implémentées gèrent des
objets à une échelle individuelle alors que pour des raisons d'optimisation, il
est parfois nécessaire d'affiner les requêtes afin d'en réduire leur nombre.

.. automodule:: wekeypedia.wikipedia.api
   :members:

Examples
--------

Here is piece of code that retrieve all links included in the `Wisdom` page and
check if all these links (n=184) have an equivalent in the french wikipedia. It does so
by asking for langlinks of 50 pages at once instead of building one query per
links. In this case, the network load reduction goes from 184 queries to 4. #win

::

  from __future__ import division
  from math import ceil
  from collections import defaultdict

  import wekeypedia
  from wekeypedia.wikipedia.api import api as api

  def api_bunch(page_titles, lang, req):
    results = defaultdict(list)
    param  = req

    w = api(lang)

    for i in range(0,int(ceil(len(page_titles)/50))):
      param["titles"] = "|".join(page_titles[i*50:i*50+50-1])

      while True:
        r = w.get(param)
        results.update({ p["title"]: p['langlinks'] for pageid, p in r["query"]["pages"].items() if 'langlinks' in p })

        if "continue" in r:
          param.update(r["continue"])
        else:
          break

    return results

  def get_lang_projection(pages, source, target):
    """
    Retrieve all correspondance from a set of pages into another language

    Parameters
    ----------
    pages : list
      List of page titles

    Returns
    -------
    correspondances : list
      List of `(redirect(initial page), corresponding page)`
    """

    params = {
      "redirects": "",
      "format": "json",
      "action": "query",
      "prop": "info|langlinks",
      "lllimit": 500,
      "lllang": target,
      "continue":""
    }

    r = api_bunch(pages, source, params)

    return [ (page, t["*"]) for page,tt in r.items() for t in tt if t["lang"] == target ]

  u = wekeypedia.WikipediaPage("Wisdom")
  pages = list(set([ x["title"] for x in u.get_links() ]))

  get_lang_projection(pages, "en", "fr")
