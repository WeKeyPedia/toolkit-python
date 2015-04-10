# -*- coding: utf-8 -*-
import sys

# import wikipedia
import urllib

try:
  from urllib.parse import unquote
except ImportError:
  from urllib import unquote

from bs4 import BeautifulSoup
import requests

from colorama import Fore

from datetime import date

from wekeypedia.wikipedia.api import api as API

def url2title(url):
  """
  Transform an url into a title

  Parameters
  ----------
  url : string

  Returns
  -------
  title : string
  """
  title = url.split("/")

  if(len(title) > 4):
    title = title[4]
    title = title.encode("ascii")
    title = unquote(title).decode("utf8")
    title = title.replace("_", " ")
  else:
    title = title[3]

  return title

def url2lang(url):
  """
  Transform an language code into a title

  Parameters
  ----------
  url : string

  Returns
  -------
  lang : string
  """
  lang = url.split("/", 3)[2]
  lang = lang.split(".")[0]
  
  return lang

class WikipediaPage(object):
  """

  - http://www.mediawiki.org/wiki/API:Query
  - http://www.mediawiki.org/wiki/API:Revisions

  """
  def __init__(self, title=None, lang="en"):
    self.ready = False
    self.query = None
    self.page = None
    self.problem = None

    self.content = ""

    self.lang = lang

    if (title):
      title = title.strip()
      self.fetch_info(title, lang=self.lang)

  def fetch_info(self, title, opt_params={ "prop": "info", "inprop": "url" }, lang="en"):
    api = API(lang)

    params = {
      "format": "json",
      "action": "query",
      "titles": u""+title
      # "rvprop": "content",
      # "redirects": ""
    }

    params.update(opt_params)

    r = api.get(params)
    # print r.json()

    pages = r["query"]["pages"]

    self.page_id = list(pages.keys())[0]
    self.title = pages[ self.page_id ]["title"]
    self.lang = lang
    self.url = pages[ self.page_id ]["fullurl"]

    # print r.url
    # print r.text

    return r

  # def get_all_editors(self):
  #   api = API()

  #   params = {
  #     "format": "json",
  #     "action": "query",
  #     "titles": self.title,
  #     "prop": "revisions",
  #     "rvprop": "user|userid|timestamp|size|ids|sha1",
  #     "rvlimit": "max",
  #     "redirects": "",
  #     "continue": ""
  #   }

  #   last = dict()
  #   revisions = []

  #   while True:
  #     current = params.copy()
  #     current.update(last)

  #     r = api.get(current)

  #     pages = r["query"]["pages"]
  #     keys = list(pages.keys())

  #     if ("revisions" in pages[ keys[0] ]):
  #       # print pages[ pages.keys()[0] ]["revisions"]
  #       revisions = revisions + pages[ keys[0] ]["revisions"]

  #     if 'continue' not in r: break

  #     last = r["continue"]

  #   return revisions

  def get_content(self, revid="", force=False, extra_params = {}):
    """
    Get the current content of the page (content of the current revision) or
    specific content if a revid is given as a parameter.

    For more paramaters, you can check the `wikipedia API <http://www.mediawiki.org/wiki/API:Revisions>`_
    documentation.

    Examples
    --------

    >>> p = WikipediaPage("Pi")
    >>> p.get_content()

    Parameters
    ----------
    revid : string, optional
      Revision id of the article. If none is given, it just check the last
      revision id give by the wikipedia API
    force : boolean, optional
      If set to `True`, it fetch the content whatever is in the cache object.
      Useful to retrieve different version without touching the cache
    extra_params : dict
      todo: document extra_params@get_content

    Returns
    -------
    content : string
      todo: document content@get_content
    """

    if (force == False) and (self.content != "") and (revid == ""):
      content = self.content
      return content

    q = {
      "redirects":"true",
      "rvparse" : "true",
      "prop": "info|revisions",
      "inprop": "url",
      "rvprop": "content"
    }

    if revid != "":
      q["rvstartid"] = revid
      q["rvlimit"] =  1

    # add extra parameters to current query
    q.update(extra_params)

    json = self.fetch_info(self.title, q)

    content = json["query"]["pages"][list(json["query"]["pages"].keys())[0]]
    content = content["revisions"][0]["*"]

    if force == False:
      self.content = content

    return content

  def get_diff_full(self, rev_id=""):
    """
    Return the full json response from a request for diff.

    Parameters
    ----------
    rev_id : string, optional
      If no revision id is supplied, the method retrieve the diff from the
      current version of the page and compare it to its predecessor.
    """
    api = API(self.lang)

    q = {
      "format": "json",
      "action": "query",
      "titles": self.title,
      "redirects":"true",
      #"rvparse" : "true",
      "prop": "info|revisions",
      "inprop": "url",
      # "rvlimit": 1,
      # "rvprop": "content",
      "rvdiffto" : "prev"
    }

    if rev_id != "":
      q.update({ "rvlimit":1, "rvstartid": rev_id })

    r = api.get(q)

    return r

  def get_diff(self, rev_id=""):
    """
    Return diff content between a revision and its predecessor. The content is
    extracted from the API json response. To get the full response, you can
    still use `get_diff_full`

    Parameters
    ----------
    rev_id : string, optional
      If no revision id is supplied, the method retrieve the diff from the
      current version of the page and compare it to its predecessor.

    Returns
    -------
    content : string

    See Also
    --------
    get_diff_full

    """
    api = API(self.lang)

    q = {
      "format": "json",
      "action": "query",
      "titles": self.title,
      "redirects":"true",
      #"rvparse" : "true",
      "prop": "info|revisions",
      "inprop": "url",
      # "rvlimit": 1,
      # "rvprop": "content",
      "rvdiffto" : "prev"
    }

    if rev_id != "":
      q.update({ "rvlimit":1, "rvstartid": rev_id })

    r = api.get(q)

    content = r["query"]["pages"][list(r["query"]["pages"].keys())[0]]
    if "diff" in content["revisions"][0]:
      content = content["revisions"][0]["diff"]["*"]
    else:
      content = False
    # content = BeautifulSoup(content, 'html.parser')

    return content

  def get_revisions_list(self, extra_params={}):
    """
    Retrieve all the revisions and their info

    Return
    ------
    revisions : list
    """
    api = API()

    revisions = []

    params = {
      "format": "json",
      "action": "query",
      "titles": self.title,
      "prop": "revisions",
      "rvprop": "user|userid|timestamp|size|ids|sha1|comment",
      "rvlimit": "max",
      "redirects": "",
      "continue": ""
    }

    while True:
      r = api.get(params)

      pages = r["query"]["pages"]
      page = pages[ list(pages.keys())[0] ]

      revisions += page["revisions"]

      if "continue" in r:
        params.update(r["continue"])
      else:
        break

    return revisions

  def get_revisions(self, extra_params={}):
    """
    Parameters
    ----------
    extra_params : dictionary

    Returns
    -------
    revisions : list
      todo: document revisions@get_revisions
    """
    api = API()

    params = {
      "format": "json",
      "action": "query",
      "titles": self.title,
      "prop": "revisions",
      "rvprop": "user|userid|timestamp|size|ids|sha1|comment|content",
      "rvlimit": "max",
      "redirects": "",
      "continue": ""
    }

    params.update(extra_params)

    # print params

    revisions = []

    while True:
      r = api.get(params)

      # print r
      pages = r["query"]["pages"]
      page = pages[ list(pages.keys())[0] ]

      revisions += page["revisions"]
      
      if "continue" in r:
        params.update(r["continue"])
      else:
        break

    return revisions

  def get_langlinks(self):
    """
    Fetch the list of hyperlinks to translation of the current page

    Returns
    -------
    langlinks : list
      List of language codes (e.g "en", "fr", "es", "ru", etc)
      todo: put a link to a page with the list of languages
    """
    api = API(self.lang)

    langlinks = []

    params = {
      "format": "json",
      "action": "query",
      "titles": self.title,
      "prop": "langlinks",
      "lllimit": 500
    }

    r = api.get(params)

    # print r

    page = r["query"]["pages"][ list(r["query"]["pages"].keys())[0] ]

    if ("langlinks" in page):
      langlinks += page["langlinks"]

    return langlinks

  def get_pageviews(self, fr="200712", to=""):
    """
    Retrieve daily page view statistics from http://stats.grok.se/

    Parameters
    ----------
    fr : string, optional
      Start of the range (minimum is december 2007) represented as `yearmonth` (`%Y%m`).

    to : string, optional
      End of the range represented as `yearmonth` (`%Y%m`).

      If no end date is given, the current date is used as an end date.

    Returns
    -------
    pageviews : list
      List of page views per day represented as tuples `[(day, views),...]`

    """
    results = []

    base_url = "http://stats.grok.se/json/%s" % (self.lang)

    if (to == ""):
      year_end = date.today().year
      month_end = date.today().month
    else:
      year_end = int(to[:4])
      month_end = int(to[4:])

    year_start = int(fr[:4])
    month_start = int(fr[4:])

    # print "from: %(year)4d-%(month)02d" % { "year": year_start, "month": month_start }
    # print "to: %(year)4d-%(month)02d" % { "year": year_end, "month": month_end }

    for y in range(year_start, year_end+1):
      m_start = month_start if (y == year_start) else 1
      m_end = month_end if (y == year_end) else 12

      for m in range(m_start, m_end+1):

        url_params = {
          "url": base_url,
          "year": y,
          "month": m,
          "title": self.title
        }

        month_url = "%(url)s/%(year)4d%(month)02d/%(title)s" % url_params
        # print month_url
        r = requests.get(month_url).json()
        results.append(r["daily_views"])

    return results


  def get_links(self):
    """
    Retrieve the content from the current revision and extract the list of
    hyperlinks (`<a>` tags) from its content.

    Returns
    -------
    links : list
      list of links as parsed HTML. The full <a> representation is returned and
      ready for further extraction
    """
    content = self.get_content()
    content = BeautifulSoup(content, 'html.parser')

    links = content.find_all('a')

    return links

  def get_links_title(self):
    """
    Retrieve content of a page, extract the links and return only the titles. In
    the wikipedia context, title attributes correspond to title of pages.

    todo: make the use of `self.title` more coherent

    See Also
    --------
    get_links

    Returns
    -------
      links : list
        list of titles extracted from the `title="..."` attribute of `<a>` tags
    """
    links = []

    links = self.get_links()
    links = map(lambda x: x.get("title"), links)

    links = list(set(links))
    links = [ l for l in links if l != None ]

    return links