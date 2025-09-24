# Importing the neccesary library 
import os
import gdown as gd    # this library is use to access file from google drive
from dotenv import load_dotenv as ld


ld()
# accessing the envirnmental variable 
data1 = os.getenv('file1')
data2 = os.getenv('file2')
data3 = os.getenv('file3')

def movie(file_id, output_name):
    try:
        url =f"https://drive.google.com/uc?id={file_id}"
        gd.download(url, output=output_name, quiet=False)
        print(f'data downloaded successfully from {url}')

    except Exception as e:
        print(f"An error occurred: {e}")

movie(data1, "data_movie_lens.csv")
movie(data2, "item_movie_lens.csv")
movie(data3, "user_movie_lens.csv")
