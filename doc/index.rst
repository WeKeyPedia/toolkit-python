.. wekeypedia documentation master file, created by
   sphinx-quickstart on Fri Apr  3 14:47:15 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

WeKeyPedia python toolkit documentation
=======================================

The wekeypedia python toolkit is a set of class and helpers that have been written during the overall `wekeypedia project <http://wekeypedia.net>`_.

Its main features are :

- data retrieval from the wikipedia API and third party (statistics, semantic web, etc)
- statistics about pages and users

 - bots (coming with 0.2)
 - page and paragraph difficulty measures (coming with 0.2)

- network modelling

 - hyperlink network (coming with 0.2)
 - page-editor bi-partite network (coming with 0.2)
 - page-word bi-partite network (coming with 0.3)

- reading maps (coming next)
- adaptative reading model (coming next)

contents:
---------
.. toctree::
  :maxdepth: 2
  
  references/information_retrieval

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