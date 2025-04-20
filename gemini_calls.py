# from google import genai
import google.generativeai as genai
from google.generativeai import configure, GenerativeModel, upload_file
from pathlib import Path
import os
from dotenv import load_dotenv
import pdf_tools
import json

def news_summary(date):
  load_dotenv()
  genai.configure(api_key=os.getenv('api_key'))  # ✅ Correct way

  news_transcript_path = Path(r'data\process_files\news_transcript.txt')
  news_rule_path = Path(r"data\process_files\news_rules.txt")

  with open(news_rule_path, 'r', encoding='utf-8') as f:
      rules = f.read()

  prompt = rules

  print("Generating notes....")

  model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # ✅

  response = model.generate_content([
    news_transcript_path.read_text(encoding='utf-8'),
    prompt
  ])

  print("Generated")

  news_mdfile_path = Path(r"data\process_files\news_result.md")
  open(news_mdfile_path, "w").close()

  print("Saving notes...")

  with open(news_mdfile_path, 'w', encoding='utf-8') as f:
      f.write(response.text)

  print("Saved")
  pdf_tools.md_to_pdf(date)


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

  raw_output = response.text
  start = raw_output.find('[')
  end = raw_output.find(']')

  if start != -1 and end != -1:
      cleaned = raw_output[start:end+1]

  book_index_path = Path(r"data\process_files\book_index.json")
  open(book_index_path, "w").close()

  with open(book_index_path, 'w', encoding='utf-8') as f:
      f.write(cleaned)

  print("Saved book index onto book_index.json")
  
# def news_summary(date):
#   load_dotenv()

#   client = genai.Client(api_key=os.getenv('api_key'))

  
#   news_transcript_path = Path(r'data\process_files\news_transcript.txt')
#   news_rule_path = Path(r"data\process_files\news_rules.txt")

#   with open(news_rule_path, 'r', encoding='utf-8') as f:
#     rules = f.read()
    
#   prompt = rules

#   print("Generating notes....")

#   response = client.models.generate_content(
#     model="gemini-1.5-flash",
#     contents=[
#         types.Part.from_bytes(
#           data=news_transcript_path.read_bytes(),
#           mime_type='text/plain',
#         ),
#         prompt])

#   print("Generated")
  
#   news_mdfile_path = Path(r"data\process_files\news_result.md")

#   open(news_mdfile_path, "w").close()

#   print("Saving notes...")     

#   with open(news_mdfile_path, 'w', encoding='utf-8') as f:
#       f.write(response.text)
      
#   print("Saved")
#   pdf_tools.md_to_pdf(date)
    
# def get_index(path):
#   #load the api
#   load_dotenv()
#   client = genai.Client(api_key=os.getenv('api_key'))
  
#   #setup paths that will be used for the api call
#   book_path = Path(path)                                                  #path of book that we want the index for
#   index_rule_path = Path(r"data\process_files\book_index_rules.txt")      #path for prompt
  
#   #setup the prompt
#   with open(index_rule_path, 'r', encoding='utf-8') as f:
#     rules = f.read()
    
#   prompt = rules
  
#   print("Generating book index.")
  
#   #make the call
#   response = client.models.generate_content(
#     model="gemini-1.5-flash",
#     contents=[
#         types.Part.from_bytes(
#             data=book_path.read_bytes(),
#             mime_type='application/pdf',
#         ),
#         prompt  
#     ]
# )



  
#   print("Generated.")
  
#   #clean the output
#   raw_output = response.text
#   start = raw_output.find('[')
#   end = raw_output.find(']')
  
#   if start!=-1 and end !=-1:
#     cleaned = raw_output[start:end+1]
  
#   #prep the output file
#   book_index_path = Path(r"data\process_files\book_index.json")  
#   open(book_index_path, "w").close()                              #clears the file if it has any old content
  
#   #write onto output file
#   with open(book_index_path, 'w', encoding='utf-8') as f:
#       f.write(cleaned)
  
#   print("Saved book index onto book_index.json")
