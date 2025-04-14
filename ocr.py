import cv2
from pathlib import Path
from PIL import Image
import pytesseract
from glob import glob
img_path_list = []

def set_list():
    img_path = []
    i=0
    src = Path(r'data\imgs')
    fallback_img = Path(r"data\fallback\fallback.jpg")  
                
    for filename in src.glob('*.*'):        
        if Path(filename).is_dir():
            continue
        
        img_path = Path(filename)
        img_path_list.append(img_path)
        
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
    
def inverted():
    for idx,path in enumerate(img_path_list):
        img = cv2.imread(str(path))
        inverted_image = cv2.bitwise_not(img)
        inverted_image = thick_font(inverted_image)
        cv2.imwrite("temp/temp.jpg", inverted_image)
        temp = Path("temp/temp.jpg")
        generate(temp, idx)

    
def normal():
    for idx,path in enumerate(img_path_list):
        img = cv2.imread(str(path))
        normal = thick_font(img)
        cv2.imwrite("temp/temp.jpg", normal)
        temp = Path("temp/temp.jpg")
        generate(temp, idx)



if __name__ == '__main__':
    print("Enter the mode: ")
    print("1) Normal \t2)Inverted \n")
    mode = int(input())
    
    set_list()
    open("data/result.txt", "w").close()
    
    match mode:
        case 1:
            normal()
        case 2:
            inverted()
    
    # set_list()
    
    
    
    
    
    
    
    
        
            
    
    
    
    
    
            
    
        
      
        