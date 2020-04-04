#!/usr/bin/env python3

import simplertf

r = simplertf.RTF("My Document Title", verbose=True)

r.author = "Myself"
r.set_layout("A4")  # The same result using r.layout = "A4"

r.par("This text starts a paragraph.")
r.text(" This text continues the paragraph, note the space before 'This'.")
r.note("The text of a footnote.", anchor="*")

r.par("A new paragraph begins. Former note and paragraph are automatically closed.")
r.note("This is the text of the second footnote.")
r.text(" I'm adding text to the second footnote.")
r.close_note()
r.text(" Now I'm adding text to the second paragraph. I had to close the note manually.")

r.create("File name")
