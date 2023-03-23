[PT-BR]
O objetivo desse programa é utilizar um novo método de leitura chamado "leitura biônica". A leitura biônica serve pra diminuir o estresse e fadiga da leitura e proporcionar uma leitura mais rápida.
O programa vai transformar qualquer texto normal em um "texto biônico", fazendo com que a primeira metade de cada palavra seja destacada em negrito.

Pra utilizar esse programa, basta ir em "the_text.py" e colar o texto na variável "txt" como docstring. Depois é só rodar o programa e escolher o nome do arquivo. O arquivo PDF vai ser criado na pasta do programa.
Caso deseje mudar a formatação das letras, é possível utilizar Courier ou Helvetica (não recomendo Times-Roman). Basta alterar esse pedaço do código → normal_style = ParagraphStyle(name='Normal', fontName='Courier', fontSize=10, leading=18). Em "fontName='Courier'", você pode alterar para Helvetica ou Times-Roman.

Esse código tem um único problema, se um paragrafo do texto colocado for MUITO grande, ele vai ser ignorado e não vai aparecer no arquivo PDF.
A única forma que encontrei de consertar esse problema foi fazendo uma gambiarra, fazendo o texto ser formatado em uma font size bem pequena pra encaixar no tamanho da página.
Ex: normal_style = ParagraphStyle(name='Normal', fontName='Courier', fontSize=2, leading=6), perceba o tamanho da fontSize e o leading(espaçamento).
Depois disso eu edito o tamanho da letra no word e fica tudo show de bola. Mas isso é péssimo pra um usuário final por exemplo.

-------------------------------------------------------------------------------------------------------------------------------------------------

[EN-US]
This program was maid to use a new type of reading called "bionic reading". It consists in decrease the stress and fatigue of reading and increase the speed which we read.
The program will receive any text and transform it into a "bionic text", making the first half of the word highlighted in bold.

To use this program, just go to "the_text.py" and paste the text in the variable "txt" as a docstring. Then you just need to run the program and choose the name of the archive (Nome do arquivo). The PDF file will appear in the program's directory.
If you want to change the letters formatation you can change this piece of code: normal_style = ParagraphStyle(name='Normal', fontName='Courier', fontSize=10, leading=18). "fontName='Courier'", you can change it to Helvetica or Times-Roman(which i don't recommend).

This code has only one problem, if the paragraph of the inputed text is TOO BIG, it will be ignored and will not appear in the PDF file. The only way i found to make a quick fix to this problem was by decreasing the font size and then editing it in Microsoft Word afterward.
Ex: normal_style = ParagraphStyle(name='Normal', fontName='Courier', fontSize=2, leading=6), you can see the fontSize is just so little and the spacing(leading) also is too small.