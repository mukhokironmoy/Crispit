import pdf_tools
from pathlib import Path

date=''
book_mdfile_path = Path(r"data\process_files\book_result.md")
with open(book_mdfile_path, 'r', encoding='utf-8') as f:
    title = f.readline().strip()
    title = title.lstrip('# ')
    title = f"{title}"
    date = ''
    print(repr(title))

# pdf_tools.md_to_pdf(date,book_mdfile_path,title)