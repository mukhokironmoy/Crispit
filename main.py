import gemini_calls
import ocr
from timer import time_it
from pdf_tools import clean_dir


if __name__ == "__main__":
    print("WELCOME TO CRISPIT!")
    print("-------------------")
    print("What would you like to do?")
    print("1) Make notes  \n2) Get OCR text")
    mode = int(input("\nEnter your choice: "))
    
    clean_dir(r"data\output")
    
    match mode:
        case 1:
            time_it(gemini_calls.summary_mode)
            
        case 2:
            time_it(ocr.ocr_mode)

            
            
    