from worker import store_revisions

for page_url in open("/data/sources/wicrimea-seeds.extended.txt", "r"):
  print page_url.strip()
  store_revisions.delay(page_url.strip())