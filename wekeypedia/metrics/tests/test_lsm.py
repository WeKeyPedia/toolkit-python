import wekeypedia

from bs4 import BeautifulSoup

def page2text(pagename):
  page = wekeypedia.WikipediaPage(pagename)
  content = page.get_revision()

  txt = BeautifulSoup(content, "html.parser")
  txt = txt.get_text()
  txt = txt.replace("[edit]","")

  return txt

def test_raw():

  raw_categories = wekeypedia.lsm.extract_categories_raw(page2text("Pi"))

  for k in raw_categories.keys():
    if k != "total words":
      assert len(raw_categories[k]) > 0

def test_percentage():
  raw_categories = wekeypedia.lsm.extract_categories(page2text("Pi"))

  for k in raw_categories.keys():
    if k != "total words":
      assert 0 < raw_categories[k] < 1

def test_compare():
  comparison = wekeypedia.lsm.compare(page2text("Pi"), page2text("Triangle"))

  for k in comparison.keys():
    if k != "total words":
      assert 0 < comparison[k] < 1
