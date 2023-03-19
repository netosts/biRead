from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from text import text2


# This is the text that will be formatted
# to change the text, go to text.py and change it there
text = text2

# Create a new PDF file
ask = str(input("Nome do arquivo: ")).strip()
pdf_file = f"{ask}.pdf"
c = canvas.Canvas('C:/Users/netos/OneDrive/Documentos/Readable PDF files/'+pdf_file, pagesize=letter)

# Define the paragraph style for the text
normal_style = ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=2, leading=22, splitLongWords=False)

# Set the margins and dimensions of the frame to fit the page
x, y = 1*inch, 0.8*inch
width, height = letter[0]-2.2*inch, letter[1]-1.5*inch
frame = Frame(x, y, width, height, showBoundary=0)


# Define a function to create a formatted paragraph
def create_paragraph(text):
    # Create a new paragraph object and add it to the frame
    lines = text.splitlines()

    formatted_text = ''
    for line in lines:
        if line.strip():

            words = line.split()
            for l in range(len(words)):
                # Bionic bold each word
                index_to_bold = len(words[l]) // 2
                formatted_word = ''
                for i, letter in enumerate(words[l]):
                    if letter.isalpha(): # check if letter is a word character
                        if i < index_to_bold:
                            formatted_word += '<b>' + letter + '</b>'
                        elif len(words[l]) == 1:
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
    paragraph = Paragraph(create_paragraph(p), normal_style)

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
