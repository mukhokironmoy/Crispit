import gemini_calls
import ocr


if __name__ == "__main__":
    print("WELCOME TO CRISPIT!")
    print("-------------------")
    print("What would you like to do?")
    print("1) Make notes  \n2) Get OCR text")
    mode = int(input("\nEnter your choice: "))
    
    match mode:
        case 1:
            gemini_calls.summary_mode()
        case 2:
            ocr.ocr_mode()
            
    