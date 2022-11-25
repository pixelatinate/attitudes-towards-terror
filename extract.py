import sys
from tika import parser

filename = 'articles/2021 Article.pdf'

# Parse the PDF
parsedPDF = parser.from_file(filename)

# Extract the text content from the parsed PDF
pdf = parsedPDF["content"]

# Convert double newlines into single newlines
pdf = pdf.replace('\n\n', '\n')

#####################################
# Do something with the PDF
#####################################
sys.stdout = open('articles/2021.txt', 'w')
print (pdf)