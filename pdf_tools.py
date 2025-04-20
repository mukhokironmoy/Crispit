import markdown
from reportlab.pdfgen import canvas
from weasyprint import HTML
from pathlib import Path
import gemini_calls
import json
from PyPDF2 import PdfReader, PdfWriter
import pdf_to_img

def md_to_pdf(date):
    with open(r'data\process_files\news_result.md','r', encoding="utf-8") as f:
        md_text = f.read()
        
    html_text = html_text = f"""
    <html>
    <head>
    <style>
    body {{
        font-family: Arial, sans-serif;
        margin: 40px;
    }}
    h1, h2, h3 {{
        color: #2c3e50;
    }}
    </style>
    </head>
    <body>
    {markdown.markdown(md_text)}
    </body>
    </html>
    """

    HTML(string=html_text).write_pdf(f"data/output/{date} - News Bulletin.pdf")
    
    
def split_into_chapters(path_of_book):
    #use gemini to create an index
    gemini_calls.get_index(path_of_book)
    
    #load the index file
    book_index_path = Path(r"data\process_files\book_index.json")
    with open(book_index_path, "r", encoding='utf-8') as f:
        chapters = json.load(f)
    
    #load the original pdf
    pdf_path = Path(path_of_book)
    reader = PdfReader(pdf_path)
    
    #output folder
    out_path = Path(r"temp\chapter_split")
    
    #create split
    for chapter in chapters:
        writer = PdfWriter()
        
        start = chapter['start_page'] - 1
        end = chapter['end_page']
        
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])
    
        chapter_title = chapter['name'].replace(":","--").replace("/","-")
        output_filename = f"temp/chapter_split/{chapter_title}.pdf"
        
        with open(output_filename, 'wb') as output_pdf:
            writer.write(output_pdf)
        
        print(f"Source split - {output_filename}.pdf")    
    
    