from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from the_text import txt


# This is the text that will be formatted
# to change the text, go to text.py and change it there
text = txt

# Create a new PDF file
ask = str(input("Nome do arquivo: ")).strip()
pdf_file = f"{ask}.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

# Define the paragraph style for the text
normal_style = ParagraphStyle(name='Normal', fontName='Courier', fontSize=10, leading=18)

# Set the margins and dimensions of the frame to fit the page
x, y = 1*inch, 0.8*inch
width, height = letter[0]-2.2*inch, letter[1]-1.5*inch
frame = Frame(x, y, width, height, showBoundary=0)


# Define a function to create a formatted text
def bionic_text(text):
    # Split text in paragraphs
    lines = text.splitlines()
    indent = '&nbsp;&nbsp;&nbsp;'

    formatted_text = ''
    for line in lines:
        if line.strip():
            formatted_text += indent*2 # indent first line of each paragraph
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
