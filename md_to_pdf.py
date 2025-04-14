import markdown
from weasyprint import HTML

def convert(date):
    with open('data/result.md','r', encoding="utf-8") as f:
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

    HTML(string=html_text).write_pdf(f"data/{date} - News Bulletin.pdf")