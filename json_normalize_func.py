# -*- coding: utf-8 -*-
"""
@author: RiditaAli
"""

"""
#https://www.kdnuggets.com/how-to-convert-json-data-into-a-dataframe-with-pandas
"""

"""
#How to Convert JSON Data into a DataFrame with Pandas and normalize function
"""

#A dictionary dataset

books = [
      {
    	"title": "The Ethnic Cleansing of Palestine",
    	"author": "Ilan Pape",
    	"publication_year": 2007,
    	"reviews": [
        {
            "reviewer": {
            "name": "Robert Geelan", 
            "reviewed in": "UK" 
                        },
         "rating": "5",
         "comment": "To understand the current Genocide in Gaza"
         },
            {
            "reviewer": {
            "name": "Gogol", 
            "reviewed in": "UK"
            },
    
         "rating": "4", 
         "comment": "A real eye opener"
        }       
    ]
    },
	{
    	"title": "The Hundred Years' War on Palestine",
    	"author": "Rashid Khalidi",
    	"publication_year": 2021,
        "reviews": [
        {
            "reviewer": {
            "name": "Carole", 
            "reviewed in": "Canada" 
                        },
         "rating": "5",
         "comment": "A superb and timely book"
         },
            {
            "reviewer": {
            "name": "Jan", 
            "reviewed in": "Netherlands"
            },           
         "rating": "5", 
         "comment": "The real story hidden behind an iron curtain of lies"
        }       
    ]	
	},
	{
    	"title": "Beyond Chutzpah",
    	"author": "Norman G. Finkelstein",
    	"publication_year": 2008,
    	"reviews": [
        {
            "reviewer": {
            "name": "Dr. Hartmut Heuermann", 
            "reviewed in": "Germany" 
                        },
         "rating": "5",
         "comment": "Highly Commended"
         },
            {
            "reviewer": {
            "name": "Roger Kenward", 
            "reviewed in": "UK"
            },
         "rating": "4", 
         "comment": "excellent sequel to the holocaust industry"
}]}]

#Imports
import json
import pandas as pd

#Load the JSON data

# Convert and write JSON object to file

"""
with open("books.json", "w") as outfile: 
    json.dump(books, outfile)
"""

with open('books.json', 'r') as f:
    data = json.load(f)

#Create the DataFrame using json_normalize()

df = pd.json_normalize(books,
meta=['title', 'author', 'publication_year'],
record_path='reviews',
errors='raise'
)
