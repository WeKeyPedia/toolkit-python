from wekeypedia.wikipedia.page import WikipediaPage

def test_get_all_revisions():
  p = WikipediaPage("Michel Maffesoli")
  revisions = p.get_revisions()

  # print len(revisions)

  assert len(revisions) > 100