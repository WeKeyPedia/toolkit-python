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
- network modelling

contents:
---------
.. toctree::
  :maxdepth: 2
  
  references/page
  references/user

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