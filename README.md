WeKeyPedia python toolkit [![Build Status](https://travis-ci.org/WeKeyPedia/toolkit-python.svg?branch=master)](https://travis-ci.org/WeKeyPedia/toolkit-python) [![Coverage Status](https://coveralls.io/repos/WeKeyPedia/toolkit-python/badge.svg?branch=master)](https://coveralls.io/r/WeKeyPedia/toolkit-python?branch=master)
===================

- [Documentation](http://toolkit-python.readthedocs.org/)

## installation

### using virtualenv

The pypi distribution is updated on important releases. During the development
phase, this is approximatively every week.

```
$ mkdir e
$ virtualenv e/py
$ source e/py/bin/activate
(py)$ pip install wekeypedia
(py)$ python -m nltk.downloader punkt wordnet maxent_treebank_pos_tagger
```

### using development version

If you need to get a up-to-last-second-update version, you might want to use the
github master version. This is highly unstable. You both get work in progress
features, their bugs and their bugfixes in realtime.

```
$ mkdir e
$ virtualenv e/py
$ source e/py/bin/activate
(py)$ pip install https://github.com/wekeypedia/toolkit-python/archive/master.zip
(py)$ python -m nltk.downloader punkt wordnet maxent_treebank_pos_tagger
```


## usage

### get the current content of a page

```python
import wekeypedia

p = wekeypedia.WikipediaPage("Pi")
content = p.get_revision()

print content
```

### parse diff result

```python
diff = p.get_diff()
plusminus = p.extract_plusminus(diff)

p.print_plusminus_overview(plusminus)
```

### count stems of a page

```python
print p.count_stems([ content ])
```


## examples and macros

You can explore the different current usages of the library by getting a look at the current we are using to build various datasets.

- [retrieve_wikipedia_network.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/examples/retrieve_wikipedia_network.py)
  - takes a file with a list of wikipedia pages
  - retrieve the hyperlinks network
  - store them in networkx format
- **WIP** [analysis-data.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/examples/analysis-data.py)
  - take a pre-existing dataset and fetch page contents, revision logs and page view statistics
  - this script is used to produce the data for our [data science python notebooks](https://github.com/WeKeyPedia/notebooks). It is mainly an explorary work to find new metrics
- [convert2blocks.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/examples/convert2blocks.py)
  - takes a pre-existing file based dataset and produce blocks representations for the [synchronology](https://github.com/WeKeyPedia/synchronology) data visualization
- [wicrimea.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/wicrimea.py)
  - fetch contents and data for the analysis of wikipedia pages involved in the current events about Crimea, Ukrain and Russia
- **WIP** [slopes-sample.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/examples/slopes-sample.py)
  - produce the dataset for [the ski slopes UI prototype](https://github.com/WeKeyPedia/slopes-builder)

## using virtualenv

```
$ virtualenv e/py --no-site-packages
$ source e/py/bin/activate
(py)$ pip install -r requirements.txt
```
