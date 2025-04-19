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