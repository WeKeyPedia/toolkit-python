from wekeypedia.wikipedia.page import WikipediaPage

# def test_fetch():
#   page = WikipediaPage("unit testing")

#   assert page.problem == None

# def test_ambiguity():
#   page = WikipediaPage("transformation")

#   assert page.problem == "ambiguity"

# def test_no_match():
#   page = WikipediaPage("utin testgni")

#   assert page.problem == "no match"

def test_links():
  page = WikipediaPage("unit testing")
  links = page.get_links()

  assert len(links) > 0

def test_instanciation():
  page = WikipediaPage("Pi")

  assert page.title == "Pi"

def test_direct_api():
  page = WikipediaPage()

  r = page.fetch_info("unit testing")

  assert "-1" not in r["query"]["pages"]

def test_direct_api_no_match():
  page = WikipediaPage()

  r = page.fetch_info("bleepbloopzerg")

  # print r

  assert "-1" in r["query"]["pages"]

def test_api_revisions_without_content():
  page = WikipediaPage("Taran Killam")

  revisions = page.get_revisions_list()

  assert len(revisions) > 500

def test_api_get_specific_revision():
  page = WikipediaPage("Taran Killam")

  revisions = page.get_revisions_list()

  revision = page.get_content(revisions[42]["revid"])

  print(revision)

  assert len(revision) > 0


def test_api_langlinks():
  page = WikipediaPage("Jeu de go", lang="fr")
  langlinks = page.get_langlinks()

  print(langlinks)

  assert len(langlinks) > 10

def test_diff():
  page = WikipediaPage("Pi")
  diff = page.get_diff()

  assert len(diff) > 0

def test_diff_full():
  page = WikipediaPage("Pi")
  diff = page.get_diff_full()

  assert "query" in diff

def test_pageviews():
  page = WikipediaPage("Pi")
  pageviews = page.get_pageviews(fr="201501")

  assert len(pageviews) > 0