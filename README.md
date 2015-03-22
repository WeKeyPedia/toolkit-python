WeKeyPedia python toolkit [![Build Status](https://travis-ci.org/WeKeyPedia/toolkit-python.svg?branch=master)](https://travis-ci.org/WeKeyPedia/toolkit-python) [![Coverage Status](https://coveralls.io/repos/WeKeyPedia/toolkit-python/badge.png?branch=master)](https://coveralls.io/r/WeKeyPedia/toolkit-python?branch=master)
===================

## examples and macros

You can explore the different current usages of the library by getting a look at the current we are using to build various datasets.

- [retrieve_wikipedia_network.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/retrieve_wikipedia_network.py)
  - takes a file with a list of wikipedia pages
  - retrieve the hyperlinks network
  - store them in networkx format
- **WIP** [analysis-data.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/analysis-data.py)
  - take a pre-existing dataset and fetch page contents, revision logs and page view statistics
  - this script is used to produce the data for our [data science python notebooks](https://github.com/WeKeyPedia/notebooks). It is mainly an explorary work to find new metrics
- [convert2blocks.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/convert2blocks.py)
  - takes a pre-existing file based dataset and produce blocks representations for the [synchronology](https://github.com/WeKeyPedia/synchronology) data visualization
- [wicrimea.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/wicrimea.py)
  - fetch contents and data for the analysis of wikipedia pages involved in the current events about Crimea, Ukrain and Russia
- **WIP** [slopes-sample.py](https://github.com/WeKeyPedia/toolkit-python/blob/master/slopes-sample.py)
  - produce the dataset for [the ski slopes UI prototype](https://github.com/WeKeyPedia/slopes-builder)

## basic tasks

provide a list of keywords and get the network structure from wikipedia

```
$ python retrieve_wikipedia_network.py yourdata.txt
```

fetch a list of urls from the [wekeypedia API](https://github.com/WeKeyPedia/api), get info from Wikipedia API and push it back to the wekeypedia API. last part has to be done.

```
$ python complete_info.py
```

## using virtualenv

```
$ virtualenv e/py --no-site-packages
$ source e/py/bin/activate
(py)$ pip install -r requirements.txt
```

## workers and distributed mode

The toolkit provide a worker/client mode in order to use the scripts across a computing grid. To use that architecture, you will need to install [celery](http://celeryproject.org).

- how to connect to the right broker -> rabbitmq
- how to connect to datasets -> mongodb

usages of env variables.

### start a worker

```
celery -A worker worker
```

### use the client

```
python client.py <command>
```
