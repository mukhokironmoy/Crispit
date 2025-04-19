import get_transcript
import ocr

if __name__ == "__main__":
    print("1) Youtube\t2) Book")
    mode = int(input("Enter the mode:- "))
    match mode:
        case 1:
            get_transcript.runner()
        case 2:
            ocr.runner()