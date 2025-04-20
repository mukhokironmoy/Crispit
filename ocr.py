import cv2
from pathlib import Path
from PIL import Image
import pytesseract
from glob import glob
import numpy as np
from pdf_to_img import convert_to_img
import re
import pdf_tools

img_path_list = []

def set_list():
    img_path = []
    i=0
    src = Path(r'data\input\imgs')
    fallback_img = Path(r"data\fallback\fallback.jpg")
    
    def extract_number(path):
        match = re.search(r'(\d+)',path.name)
        return int(match.group()) if match else -1
                
    for filename in sorted(src.glob('*.*'), key=extract_number):        
        if Path(filename).is_dir():
            continue
        
        img_path = Path(filename)
        img_path_list.append(img_path)
        
    for thing in img_path_list:
        print(thing)
        
def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return(image)

def generate_text(path, idx):
    img = Image.open(path)
    ocr_result = pytesseract.image_to_string(img)
    print(f"Generated result for img{idx}.") 
    with open("data/process_files/ocr_out.txt", "a", encoding="utf-8") as f:
                f.write(f"Page {idx} \n\n")
                f.write(ocr_result)
                f.write("\n\n\n\n")
    print(f"Stored result for img{idx}.\n")

def is_inverted(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mean_brightness = np.mean(gray)
    return mean_brightness < 127

def process():
    for idx,path in enumerate(img_path_list):
        img = cv2.imread(str(path))
        
        if is_inverted(img):
            inverted_image = cv2.bitwise_not(img)
            inverted_image = thick_font(inverted_image)
            cv2.imwrite("temp/temp.jpg", inverted_image)
            temp = Path("temp/temp.jpg")
            generate_text(temp, idx)
            # inverted(img,idx)
        else:
            normal = thick_font(img)
            cv2.imwrite("temp/temp.jpg", normal)
            temp = Path("temp/temp.jpg")
            generate_text(temp, idx)
            # normal(img,idx)
    

def runner():
    print("\nBook source: ")
    print("1) PDF with multiple chapters \n2)PDF without chapters  \n3)Batch of images   \n4)Single image")
    mode = int(input())
    open("data/process_files/ocr_out.txt", "w").close()
    
    match mode:
        case 1:
            print("Enter the path for the pdf:")
            pdf_path = input()
            pdf_tools.split_into_chapters(pdf_path)
            
            
        case 2:
            print("Enter the path for the pdf: ")
            pdf_path = input()
            convert_to_img(pdf_path)
            set_list()
            process()
                        
        case 3:
            set_list()
            process()
    


  # def inverted():
#     for idx,path in enumerate(img_path_list):
#         img = cv2.imread(str(path))
#         inverted_image = cv2.bitwise_not(img)
#         inverted_image = thick_font(inverted_image)
#         cv2.imwrite("temp/temp.jpg", inverted_image)
#         temp = Path("temp/temp.jpg")
#         generate(temp, idx)

# def inverted(img,idx):          
#     inverted_image = cv2.bitwise_not(img)
#     inverted_image = thick_font(inverted_image)
#     cv2.imwrite("temp/temp.jpg", inverted_image)
#     temp = Path("temp/temp.jpg")
#     generate_text(temp, idx)
    
# def normal():
#     for idx,path in enumerate(img_path_list):
#         img = cv2.imread(str(path))
#         normal = thick_font(img)
#         cv2.imwrite("temp/temp.jpg", normal)
#         temp = Path("temp/temp.jpg")
#         generate(temp, idx)

# def normal(img,idx):       
#     normal = thick_font(img)
#     cv2.imwrite("temp/temp.jpg", normal)
#     temp = Path("temp/temp.jpg")
#     generate_text(temp, idx)  
    
    
    
    
    
    
        
            
    
    
    
    
    
            
    
        
      
        