import cv2
from pathlib import Path
from PIL import Image
import pytesseract
from glob import glob
import numpy as np
from pdf_to_img import convert_to_img
import re

img_path_list = []

def set_list():
    img_path = []
    i=0
    src = Path(r'data\input\imgs')
    fallback_img = Path(r"data\fallback\fallback.jpg")
    
    # def extract_number(path):
    #     match = re.search(r'(\d+)',path.name)
    #     return int(match.group()) if match else -1
                
    for filename in src.glob('*.*'):        
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

def generate(path, idx):
    img = Image.open(path)
    ocr_result = pytesseract.image_to_string(img)
    print(f"Generated result for img{idx}.") 
    with open("data/result.txt", "a", encoding="utf-8") as f:
                f.write(f"Page {idx} \n\n")
                f.write(ocr_result)
                f.write("\n\n\n\n")
    print(f"Stored result for img{idx}.\n")
    
# def inverted():
#     for idx,path in enumerate(img_path_list):
#         img = cv2.imread(str(path))
#         inverted_image = cv2.bitwise_not(img)
#         inverted_image = thick_font(inverted_image)
#         cv2.imwrite("temp/temp.jpg", inverted_image)
#         temp = Path("temp/temp.jpg")
#         generate(temp, idx)

def inverted(img,idx):          
    inverted_image = cv2.bitwise_not(img)
    inverted_image = thick_font(inverted_image)
    cv2.imwrite("temp/temp.jpg", inverted_image)
    temp = Path("temp/temp.jpg")
    generate(temp, idx)
    
# def normal():
#     for idx,path in enumerate(img_path_list):
#         img = cv2.imread(str(path))
#         normal = thick_font(img)
#         cv2.imwrite("temp/temp.jpg", normal)
#         temp = Path("temp/temp.jpg")
#         generate(temp, idx)

def normal(img,idx):       
    normal = thick_font(img)
    cv2.imwrite("temp/temp.jpg", normal)
    temp = Path("temp/temp.jpg")
    generate(temp, idx)

def is_inverted(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mean_brightness = np.mean(gray)
    return mean_brightness < 127

def process():
    for idx,path in enumerate(img_path_list):
        img = cv2.imread(str(path))
        
        if is_inverted(img):
            inverted(img,idx)
        else:
            normal(img)
    

if __name__ == '__main__':
    print("Enter the mode: ")
    print("1) PDF \t2) Image (batch) \n")
    mode = int(input())
    open("data/result.txt", "w").close()
    
    match mode:
        case 1:
            print("Enter the path for the pdf: ")
            pdf_path = input()
            convert_to_img(pdf_path)
            set_list()
            process()
                        
        case 2:
            set_list()
            process()
    
    # set_list()
    
    
    
    
    
    
    
    
        
            
    
    
    
    
    
            
    
        
      
        