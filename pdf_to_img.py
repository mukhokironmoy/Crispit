import fitz
from pathlib import Path
import os

def clean_dir(folder_path):
    folder_path = Path(folder_path)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Folder Cleaned.")
    
def convert(path):
    path = Path(path)
    images = fitz.open(path)
    output_path = Path(r'data\input\imgs')
    clean_dir(output_path)
    
    for i, page in enumerate(images):
        img_name = f"img_{i+1}.jpg"
        pix = page.get_pixmap()
        pix.save(output_path/img_name)
        print(f"Convesion : Page {i+1} done")
    print("\n\nConversion successfull")    
    

convert('data\input\pdfs\Somnath Sharma.pdf')





