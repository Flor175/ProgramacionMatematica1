from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Command
from pylatex.utils import  NoEscape

class MyDocument(Document):
    def __init__(self):
        super().__init__()

        self.preamble.append(Command('title', 'Awesome Title'))
        self.preamble.append(Command('date', NoEscape(r'\today')))
        self.append(NoEscape(r'\maketitle'))
    
    def fill_document(self):
        """Add a section, a subsection and some text to the document."""
        with self.create(Section('A section')):
            geometry_options = { "margin": "2.54cm", "includeheadfoot": True}

            with self.create(Tabular('rc|cl')) as table:
                table.add_hline()
                table.add_row((1, 2, 3, 4))
                table.add_hline(1, 2)
                table.add_empty_row()
                table.add_row((4, 5, 6, 7))


            with self.create(TikZ()):
                plot_options = 'height=4cm, width=6cm, grid=major'
                with doc.create(Axis(options=plot_options)) as plot:
                    plot.append(Plot(name='model', func='-x^5 - 242')) 
if __name__ == '__main__':

    doc = MyDocument()
    doc.fill_document()
    doc.generate_pdf('Reporte', clean_tex=False)
    tex = doc.dumps()