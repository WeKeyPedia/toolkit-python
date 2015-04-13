from wekeypedia import WikipediaPage
from collections import defaultdict

def test_diff():
  page = WikipediaPage("Pi")
  diff = page.get_diff()

  assert len(diff) > 0

def test_diff_full():
  page = WikipediaPage("Pi")
  diff = page.get_diff_full()

  assert "query" in diff

def test_extraction():
  page = WikipediaPage("Pi")
  diff = page.get_diff()

  plusminus = page.extract_plusminus(diff)

  assert "added" in plusminus
  assert "deleted" in plusminus
  assert len(plusminus["added"]) > 0 or len(plusminus["deleted"]) > 0

def test_count_stems():
  page = WikipediaPage("Pi")
  diff = page.get_diff()

  inflections = defaultdict(dict)

  plusminus = page.extract_plusminus(diff)

  added = page.count_stems(plusminus["added"], inflections)
  deleted = page.count_stems(plusminus["deleted"], inflections)

  assert len(added) > 0 or len(deleted) > 0
  assert len(inflections) > 0