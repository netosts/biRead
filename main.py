from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Frame
import re
from text import text


# This is the text that will be formatted
# to change the text, go to text.py and change it there
text = text

# Create a new PDF file
ask = str(input("Nome do arquivo: ")).strip()
pdf_file = f"{ask}.pdf"
c = canvas.Canvas('C:/Users/netos/OneDrive/Documentos/Readable PDF files/'+pdf_file, pagesize=letter)

# Define the paragraph style for the normal text
normal_style = ParagraphStyle(name='Normal', fontName='Courier', fontSize=12)

# Set the margins and dimensions of the frame to fit the page
x, y = 0, 0
width, height = letter[0], letter[1]
frame = Frame(x, y, width, height, showBoundary=0)

# Create a new paragraph object and add it to the frame
lines = text.splitlines()

formatted_text = ''
for line in lines:
    if line.strip():
        words = re.findall(r'\S+|\s+', line)
        for l in range(len(words)):
            if words[l].isspace():
                formatted_text += words[l]
            else:
                match = re.match(r'^(\d+)(\D.*)', words[l])
                if match:
                    # word starts with a number, split it into two parts
                    number = match.group(1)
                    word = match.group(2)
                    if len(word) == 1:
                        index_to_bold = 1
                    else:
                        index_to_bold = len(word) // 2
                    formatted_word = f"<font size='7'>{number}</font><b>{word[:index_to_bold]}</b>{word[index_to_bold:]}"
                else:
                    # word doesn't start with a number
                    index_to_bold = len(words[l]) // 2
                    formatted_word = ''
                    for i, letter in enumerate(words[l]):
                        if i < index_to_bold:
                            formatted_word += '<b>' + letter + '</b>'
                        elif len(words[l]) == 1:
                            formatted_word += '<b>' + letter + '</b>'
                        else:
                            formatted_word += letter
                formatted_text += formatted_word
        formatted_text += '<br/>'

paragraph = Paragraph(formatted_text, normal_style)
frame.addFromList([paragraph], c)

# Save the PDF file and close the canvas
c.save()
