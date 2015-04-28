from setuptools import setup, find_packages

setup(
  name = 'wekeypedia',
#  packages = ['wekeypedia'], # this must be the same as the name above
  packages = find_packages(exclude=["test*"]), # this must be the same as the name above
  version = '0.1.5',
  description = 'toolkit to build datasets around wikipedia pages and to compute extra metrics',
  author = 'tam kien duong',
  author_email = 'tk@deveha.com',
  url = 'https://github.com/wekeypedia/toolkit-python', # use the URL to the github repo
  download_url = 'https://github.com/WeKeyPedia/toolkit-python/archive/0.1.5.tar.gz', # I'll explain this in a second
  keywords = ['wikipedia', 'information retrieval', 'api', "data"], # arbitrary keywords
  classifiers = [],
  install_requires=["nltk", "networkx", "requests", "mwparserfromhell", "colorama", "beautifulsoup4", "numpy"],
)
