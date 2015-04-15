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


Retrieving revisions
--------------------

.. autosummary::
   :toctree: generated/

   WikipediaPage.get_revision
   WikipediaPage.get_revisions_list
   WikipediaPage.get_current

Extracting parts
----------------

.. autosummary::
   :toctree: generated/

   WikipediaPage.get_links
   WikipediaPage.get_links_title
   WikipediaPage.get_langlinks
   WikipediaPage.get_pageviews

Extracting editors
------------------

.. autosummary::
   :toctree: generated/

   WikipediaPage.get_editors

Retrieving and parsing diff
---------------------------

.. code-block:: json

  {
    "comment": "/* Overview */",
    "timestamp": "2007-01-11T19:06:02Z",
    "revid": 100042918,
    "anon": "",
    "user": "129.24.51.153",
    "parentid": 100036516,
    "diff": {
      "to": 100042918,
      "*": "<tr>\n  <td colspan=\"2\" class=\"diff-lineno\">Line 21:</td>\n  <td colspan=\"2\" class=\"diff-lineno\">Line 21:</td>\n</tr>\n<tr>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"></td>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"></td>\n</tr>\n<tr>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"><div>In ordinary use, ''love'' usually refers to interpersonal love, an experience felt by a person for another person. Love often involves caring for or identifying with a person or thing, including oneself (cf. [[narcissism]]).In this use, love is actually the greatest proportion on selfishness, in that one only wants one thing, and that is for another being to be happy, and the one in love will do anything to fulfill this wish. This case however, does not necessarily end in marriage, because another may make the loved one happier, meaning the lover will give the other up.</div></td>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"><div>In ordinary use, ''love'' usually refers to interpersonal love, an experience felt by a person for another person. Love often involves caring for or identifying with a person or thing, including oneself (cf. [[narcissism]]).In this use, love is actually the greatest proportion on selfishness, in that one only wants one thing, and that is for another being to be happy, and the one in love will do anything to fulfill this wish. This case however, does not necessarily end in marriage, because another may make the loved one happier, meaning the lover will give the other up.</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)[[User:129.24.51.153|129.24.51.153]] 19:06, 11 January 2007 (UTC)</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>See \"Love is the Real Thing\" on the web addresses below[[User:129.24.51.153|129.24.51.153]]</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>* </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>[[User:129.24.51.153|129.24.51.153]]NEWS FLASH[[User:129.24.51.153|129.24.51.153]] </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>WASHINGTON (AP)---\"Using anti-depressants Increases the risk of </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>Suicidal thoughts and behavior among young people\"---12/06/2006 </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)~~ </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>* </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div> </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>Please help volunteer effort to save our impulsive youths: TeenAnswers is for Everyone!</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)19:06, 11 January 2007 (UTC)~</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>http://groups.google.com/group/TeenAnswers</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>http://groups.google.com/group/answers-for-teens</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>http://groups.yahoo.com/group/TeenAnswers</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>http://groups.yahoo.com/group/answers-for-teens</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>[All \"groups\": 5 permanent, proven monographs &amp; no chat!] </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>*</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>[[User:129.24.51.153|129.24.51.153]]Ending suicide/impulsive depression/self-injury is NOW possible!</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>It works, even though you might not agree, but other people's lives</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>are more important than Anyone's subjective opinion![[User:129.24.51.153|129.24.51.153]]</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>*</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>http://s2.excoboard.com/exco/index.php?boardid=24582</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>http://CaptainChurch.proboards57.com</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>http://b4.boards2go.com/boards/board.cgi?user=ChurchCaptain</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>http://www.bev.net/users/homepages/JamesSorrell</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>*</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>sorrell.james@gmail.com</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>*</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>WASHINGTON - Teens increasingly are getting high with legal drugs like painkillers and mood stimulants, and they're turning to cough syrup as well, says a government survey released Thursday. </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>The annual study by the National Institute on Drug Abuse, conducted by the University of Michigan, showed mixed results in the nation's longtime campaign against teen drug abuse.</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>It found that while fewer teens overall drank alcohol or used illegal drugs in the last year, a small but growing number were popping prescription painkillers like OxyContin and Vicodin and stimulants like </div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>Ritalin.</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>As many as one in every 14 high school seniors said they used cold medicine \"fairly recently\" to get high, the study found.</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>It was the first year that the government tracked the frequency of teens who reported getting high from over-the-counter medicine for coughs and colds.</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"></td>\n</tr>\n<tr>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"></td>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"></td>\n</tr>\n<tr>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"><div>The very existence of love is itself subject to debate. Some categorically reject the notion as false or meaningless. Others call it a recently-invented abstraction, sometimes dating the \"invention\" to courtly Europe during or after the middle ages, although this is contradicted by the sizable body of ancient love poetry.&lt;ref&gt;[http://www.TrueOpenLove.org/reference/AncientLovePoetry.html Ancient Love Poetry] - TrueOpenLove.org&lt;/ref&gt; Others maintain that love really exists, and is not an abstraction, but is undefinable, being an essence which is [[spirituality|spiritual]] or [[metaphysics|metaphysical]] in nature. Some psychologists maintain that love is the action of lending one's \"boundary\" or \"[[self-esteem]]\" to another. Others attempt to define love by applying the definition to everyday life.</div></td>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"><div>The very existence of love is itself subject to debate. Some categorically reject the notion as false or meaningless. Others call it a recently-invented abstraction, sometimes dating the \"invention\" to courtly Europe during or after the middle ages, although this is contradicted by the sizable body of ancient love poetry.&lt;ref&gt;[http://www.TrueOpenLove.org/reference/AncientLovePoetry.html Ancient Love Poetry] - TrueOpenLove.org&lt;/ref&gt; Others maintain that love really exists, and is not an abstraction, but is undefinable, being an essence which is [[spirituality|spiritual]] or [[metaphysics|metaphysical]] in nature. Some psychologists maintain that love is the action of lending one's \"boundary\" or \"[[self-esteem]]\" to another. Others attempt to define love by applying the definition to everyday life.</div></td>\n</tr>\n\n<!-- diff cache key enwiki:diff:version:1.11a:oldid:100036516:newid:100042918 -->\n",
      "from": 100036516
    }
  }

.. autosummary::
   :toctree: generated/

   WikipediaPage.get_diff
   WikipediaPage.get_diff_full
   WikipediaPage.extract_plusminus
   WikipediaPage.count_stems


Page views
----------

.. autosummary::
   :toctree: generated/

   WikipediaPage.get_pageviews

helpers
=======

.. autofunction:: wekeypedia.wikipedia.page.url2title
.. autofunction:: wekeypedia.wikipedia.page.url2lang
