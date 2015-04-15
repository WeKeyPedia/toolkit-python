import wekeypedia
import random

def test_get_all_editors():
  p = wekeypedia.WikipediaPage("Triangle")

  editors = p.get_editors()

  assert len(editors) > 0

def test_get_selection_of_editors():
  p = wekeypedia.WikipediaPage("Triangle")
  
  revisions = p.get_revisions_list()
  revisions = random.sample([ r["revid"] for r in revisions ], 10)

  editors = p.get_editors(revisions)

  assert len(revisions) == 10
  assert 1 < len(editors) <= 10