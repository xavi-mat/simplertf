# simplertf
Simple RTF creator.

Python module to create simple rtf documents.
Main 'Rtf' class defines objects where add paragraphs, footnotes, and text with
different formatting options. Properties of paper size and margins are also
supported.
By Xavimat.

## TODO
(I'm currently trying a `simplefodt` creator because rtf was too limited. Leaving this here in case anyone finds it useful.)
* Font Table, Color Table, Stylesheet.
  * Customizable outside the Rtf class, and added later to it.
  * Default font tables, color tables and stylesheets.
* Info about languages and language codes.
  * Table of info about languages.
  * For example, `Style.lang = "Italian"` will set automatically to 1040.
* Customizable Footnote options.

(All this is currently possible, but only inside the Rtf class, and you'll need to know the codes and variable names.)

## Simple example

```python
import simplertf
r = simplertf.RTF("My Document Title")
r.author = "Myself"
r.set_layout("A4")
r.par("This text starts a paragraph.")
r.text(" This text continues the paragraph, note the space before 'This'.")
r.note("The text of a footnote.", anchor="*")
r.par("A new paragraph begins. Former note and paragraph are automatically closed.")
r.note("This is the text of the second footnote.")
r.text(" I'm adding text to the second footnote.")
r.close_note()
r.text(" Now I'm adding text to the second paragraph. I had to close the note manually.")
r.create("File name")
```
