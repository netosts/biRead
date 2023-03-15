from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from the_text import txt
import re


# This is the text that will be formatted
# to change the text, go to the_text.py and change it there
text = txt

# Create a new PDF file
file_name = str(input("Nome do arquivo: ")).strip()
pdf_file = f"{file_name}.pdf"
c = canvas.Canvas('C:/Users/netos/OneDrive/Documentos/Readable PDF files/'+pdf_file, pagesize=letter)

# Define the paragraph style for the text
normal_style = ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12, leading=18, splitLongWords=False)

# Set the margins and dimensions of the frame to fit the page
x, y = 1*inch, 0.8*inch
width, height = letter[0]-2.2*inch, letter[1]-1.5*inch
frame = Frame(x, y, width, height, showBoundary=0)


# Define a function to create a formatted text
def bionic_text(text):
    # Split text in paragraphs
    lines = text.splitlines()

    formatted_text = ''
    for line in lines:
        if line.strip():
            words = re.findall(r'\S+|\s+', line) # separate the words in each paragraph
            for l in range(len(words)):
                if words[l].isspace():
                    formatted_text += words[l]
                else:
                    match = re.match(r'^(\d+)(\D.*)', words[l])
                    if match:
                        # word starts with a number, split it into two parts
                        # format the numbers and words separately
                        number = match.group(1)
                        word = match.group(2)
                        index_to_bold = len(word) // 2
                        if len(word) == 1:
                            formatted_word = f"<sup><font size='8'>{number}</font></sup> <b>{word}</b>"
                        else:
                            formatted_word = f"<sup><font size='8'>{number}</font></sup> <b>{word[:index_to_bold]}</b>{word[index_to_bold:]}"
                    else:
                        # word doesn't start with a number
                        index_to_bold = len(words[l]) // 2
                        formatted_word = ''
                        for i, letter in enumerate(words[l]):
                            if letter.isalpha():
                                if i < index_to_bold:
                                    formatted_word += '<b>' + letter + '</b>'
                                elif len(words[l]) == 1:
                                    formatted_word += '<b>' + letter + '</b>'
                                elif words[l][0] in '“' and i == 1:
                                    formatted_word += '<b>' + letter + '</b>'
                                else:
                                    formatted_word += letter
                            else:
                                formatted_word += letter
                    formatted_text += formatted_word + ' '
            formatted_text += '<br/>'
    return formatted_text


# Split the text into paragraphs
paragraphs = text.split('\n')

# Iterate through the paragraphs and add them to the canvas
for p in paragraphs:
    # Create a new paragraph object and add it to the frame
    paragraph = Paragraph(bionic_text(p), normal_style)

    # Check if the paragraph fits in the current frame
    if frame.add(paragraph, c):
        # The paragraph fits, so continue to the next paragraph
        continue
    else:
        # The paragraph doesn't fit, so create a new page and add the paragraph to it
        c.showPage()
        frame = Frame(x, y, width, height, showBoundary=0)
        frame.add(paragraph, c)

# Save the PDF file and close the canvas
c.save()
