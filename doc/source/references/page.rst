**************
wikipedia page
**************

Overview
========
.. currentmodule:: wekeypedia.wikipedia.page
.. autofunction:: WikipediaPage


Create a page handler
---------------------

.. autosummary::
   :toctree: generated/

   WikipediaPage.__init__
   WikipediaPage.fetch_info

Retrieving current content and parts
------------------------------------

.. autosummary::
   :toctree: generated/

   WikipediaPage.get_content
   WikipediaPage.get_links
   WikipediaPage.get_links_title
   WikipediaPage.get_langlinks
   WikipediaPage.get_pageviews

Retrieving revisions and diff
-----------------------------

.. autosummary::
   :toctree: generated/

   WikipediaPage.get_revisions_list
   WikipediaPage.get_diff
   WikipediaPage.get_diff_full


.. .. autoclass:: wekeypedia.wikipedia.page.WikipediaPage
..    :members:

helpers
=======

.. autofunction:: wekeypedia.wikipedia.page.url2title
.. autofunction:: wekeypedia.wikipedia.page.url2lang
