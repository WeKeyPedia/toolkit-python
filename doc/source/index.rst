.. wekeypedia documentation master file, created by
   sphinx-quickstart on Fri Apr  3 14:47:15 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

WeKeyPedia python toolkit documentation
=======================================

The wekeypedia python toolkit is a set of class and helpers that have been
written during the overall `wekeypedia project <http://wekeypedia.net>`_. It
main purpose is to give back some shortcuts to the science community. We hope
this work will help future data scientist and web scrappers make them win some
time about the tedious part of the work, be able to spend more time on the
more fun parts and conduct studies with wikipedia materials.

Its main features are :

- data retrieval from the wikipedia API and 3rd party (statistics, semantic web, etc)
- information extraction of API contents
- network modeling of graph structures included in pages architecture
- computation of various metrics (readibility, convergence, lsm, etc)
- generation of reading maps based on a recommandation system

contents:
---------
.. toctree::
  :maxdepth: 2

  references/information_retrieval
  references/metrics

installation (with virtual env)
-------------------------------

.. code-block:: shell

  $ virtualenv e/py --no-site-packages
  $ source e/py/bin/activate
  (py)$ pip install wekeypedia

todo list:
----------

.. todolist::


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
