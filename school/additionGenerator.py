import random
import time
from tabulate import tabulate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

# Function to generate a random number between 1 and 20
def generate_random_number(limit=20):
    return random.randint(1, limit)

# Function to create the data for the table
def create_table_data(rows, columns):
    data = []
    for _ in range(rows):
        row = []
        for col in range(columns):
            if col % 2 == 0:
                num1 = generate_random_number()
                num2 = generate_random_number()
                while num1 + num2 > 20:
                    num1 = generate_random_number()
                    num2 = generate_random_number()
                row.append(f"{num1} + {num2}")
            else:
                row.append('')
        data.append(row)
    return data

# Create the table data with 27 rows and 6 columns
table_data = create_table_data(27, 6)

# Get the current Unix timestamp
current_timestamp = int(time.time())

# Create a PDF file with the table and timestamp
pdf_file = f"table_{current_timestamp}.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)
table = Table(table_data, colWidths=60, rowHeights=20)
table.setStyle([('GRID', (0, 0), (-1, -1), 0.5, (0, 0, 0, 1))])
story = []
story.append(table)
doc.build(story)

print(f"Table saved as '{pdf_file}'")

