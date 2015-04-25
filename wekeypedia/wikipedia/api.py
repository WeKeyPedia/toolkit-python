# -*- coding: utf-8 -*-
import requests

class api:
  """
  Parameters
  ----------
  lang : string, optional
  """

  def __init__(self, lang="en"):
    self.lang = lang
    self.url = "http://%s.wikipedia.org/w/api.php" % (self.lang)

  def get(self, query):
    """
    Parameters
    ----------
    query : dict

    Returns
    -------
    result : dict
    """
    r = requests.get(self.url, params=query)

    try:
      result = r.json()
    except ValueError:
      print self.url
      print query
      exit()


    return result
