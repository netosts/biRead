from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from the_text import text2


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


# Define a function to create a formatted text with a list of words
def bionic_text(text):
    # Split text in paragraphs
    lines = text.splitlines()
    indent = '&nbsp;&nbsp;&nbsp;'

    formatted_text = list()
    for line in lines:
        if line.strip():
            # split paragraphs in words to format it
            words = line.split()
            for l in range(len(words)):
                # Bionic bold each word
                index_to_bold = len(words[l]) // 2
                formatted_word = ''
                for i, letter in enumerate(words[l]):
                    if letter.isalpha():  # check if letter is a word character
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
                if l == 0:  # indent the first line of each paragraph
                    formatted_text.append(indent*4 + formatted_word + ' ')
                elif l == (len(words) - 1):  # break line at the end of paragraph
                    formatted_text.append(formatted_word + '<br/>')
                else:
                    formatted_text.append(formatted_word + ' ')
    return formatted_text  # return the list of words


# Iterate through the words and add them to the canvas
words = bionic_text(text).split()
for w in words:
    # Create a new paragraph object and add it to the frame
    paragraph = Paragraph(w, normal_style)

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
