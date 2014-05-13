import mwparserfromhell as mw

class Mediawiki:
  def __init__(self, txt=""):
    self.text = self.parse(txt)

  def parse(self,txt):
    return mw.parse(txt)


  def get_headings(self):
    return self.text.filter_headings()

  def get_blocks(self):
    sections = []

    nodes = self.text.get_sections(include_lead=True, flat=True)

    for n in nodes:
      section = []

      node = mw.parse(n)

      print ""

      start_at = 1

      if len(node.filter_headings())>0:
        print node.filter_headings()[0].title
        section.append( len( node.filter_headings()[0].title ) )
      else:
        section.append(0)
        start_at = 0

      stripped_text = node.strip_code()

      paragraphs = stripped_text.split("\n\n")[start_at:]

      for p in paragraphs:
        for w in p.split(" "):
          section.append(len(w))

        section.append(0)

      # print section
      sections.append(section)

    return sections