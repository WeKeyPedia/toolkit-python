WeKeyPedia python toolkit [![Build Status](https://travis-ci.org/WeKeyPedia/toolkit-python.svg?branch=master)](https://travis-ci.org/WeKeyPedia/toolkit-python) [![Coverage Status](https://coveralls.io/repos/WeKeyPedia/toolkit-python/badge.png?branch=master)](https://coveralls.io/r/WeKeyPedia/toolkit-python?branch=master)
===================

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
