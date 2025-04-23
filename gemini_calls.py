# from google import genai
import google.generativeai as genai
from google.generativeai import configure, GenerativeModel, upload_file
from pathlib import Path
import os
from dotenv import load_dotenv
import pdf_tools


def news_summary(date):
  #load api key
  load_dotenv()
  genai.configure(api_key=os.getenv('api_key'))  
  
  #load transcript 
  news_transcript_path = Path(r'data\process_files\news_transcript.txt')
  
  #load and setup prompt
  news_rule_path = Path(r"data\process_files\news_rules.txt")
  with open(news_rule_path, 'r', encoding='utf-8') as f:
      rules = f.read()

  prompt = rules

  print("Generating notes for news....")

  #setup model
  model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # ✅

  #generate response
  response = model.generate_content([
    news_transcript_path.read_text(encoding='utf-8'),
    prompt
  ])

  print("Generated")

  #load output file
  news_mdfile_path = Path(r"data\process_files\news_result.md")
  open(news_mdfile_path, "w").close()

  print("Saving notes...")

  #save response onto output file
  with open(news_mdfile_path, 'w', encoding='utf-8') as f:
      f.write(response.text)

  print("Saved")
  pdf_tools.md_to_pdf(date,r"data\process_files\news_result.md","News Bulletin")

#------------------------------------------------------------------------------------------------------

def get_index(path):
  #load api key
  load_dotenv()
  genai.configure(api_key=os.getenv('api_key'))  
  
  #load prompt
  index_rule_path = Path(r"data\process_files\book_index_rules.txt")
  with open(index_rule_path, 'r', encoding='utf-8') as f:
      rules = f.read()
  
  #load upload file
  book_path = Path(path)
  uploaded_file = upload_file(path=book_path)    

  #load model
  model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # ✅
  
  print("Generating book index.")

  #generate response
  response = model.generate_content([
    uploaded_file, rules
  ])

  print("Generated.")

  #format response
  raw_output = response.text
  start = raw_output.find('[')
  end = raw_output.find(']')

  if start != -1 and end != -1:
      cleaned = raw_output[start:end+1]

  #load output file
  book_index_path = Path(r"data\process_files\book_index.json")
  open(book_index_path, "w").close()

  #save response onto output file
  with open(book_index_path, 'w', encoding='utf-8') as f:
      f.write(cleaned)

  print("Saved book index onto book_index.json")
 
#------------------------------------------------------------------------------------------------------
 
def book_summary():
  #load api key
  load_dotenv()
  genai.configure(api_key=os.getenv('api_key'))
  
  #load document
  document_path = Path(r"data\process_files\ocr_out.txt") 
  
  #load prompt
  book_rule_path = Path(r"data\process_files\book_rules.txt")
  with open(book_rule_path, 'r', encoding='utf-8') as f:
      rules = f.read()
  
  prompt = rules

  print("Generating notes for book....")

  #setup model
  model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # ✅

  #generate response
  response = model.generate_content([
    document_path.read_text(encoding='utf-8'),
    prompt
  ])

  print("Generated")
  
  #load output file
  book_mdfile_path = Path(r"data\process_files\book_result.md")
  open(book_mdfile_path, "w").close()

  print("Saving notes...")

  #save response onto output file
  with open(book_mdfile_path, 'w', encoding='utf-8') as f:
    f.write(response.text)
      
  with open(book_mdfile_path, 'r', encoding='utf-8') as f:
    title = f.readline().strip()
    title = title.lstrip('# ')
    date = ''
    

  print("Saved")
  pdf_tools.md_to_pdf(date,r"data\process_files\book_result.md",title)

#------------------------------------------------------------------------------------------------------
   
def summary_mode():
  import get_transcript
  import ocr
  print("Choose your source:")
  print("1) Youtube Notes\n2) Book Notes")
  mode = int(input("\nEnter your choice: "))
  match mode:
      case 1:
          get_transcript.summary_runner()
      case 2:
          ocr.summary_runner()
      case _:
          print("Invalid input. Enter a valid choice.")
          summary_mode()
  
#------------------------------------------------------------------------------------------------------
  
  
  
