# import libraries (you may add additional imports but you may not have to)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from zipfile import ZipFile
from urllib.request import Request, urlopen, urlretrieve
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Get project files
if not os.path.exists("book-crossings.zip"):
    url = "https://cdn.freecodecamp.org/project-data/books/book-crossings.zip"
    req = Request(
        url=url, 
        headers={"User-Agent": "Mozilla/5.0"}
    )

    webpage = urlopen(req)

    with open("book-crossings.zip","wb") as output:
        output.write(webpage.read())

    with ZipFile("book-crossings.zip", "r") as zFile:
        zFile.extractall()

books_filename = "BX-Books.csv"
ratings_filename = "BX-Book-Ratings.csv"
users_filename = "BX-Users.csv"

# Import csv data into dataframes
df_books = pd.read_csv(
    books_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=["isbn", "title", "author"],
    usecols=["isbn", "title", "author"],
    dtype={"isbn": "str", "title": "str", "author": "str"})

df_ratings = pd.read_csv(
    ratings_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=["user", "isbn", "rating"],
    usecols=["user", "isbn", "rating"],
    dtype={"user": "int32", "isbn": "str", "rating": "float32"})

df_users = pd.read_csv(
    ratings_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=["user", "isbn", "rating"],
    usecols=["user", "isbn", "rating"],
    dtype={"user": "int32", "isbn": "str", "rating": "float32"})

# Filtering dataframes