# -*- coding: utf-8 -*-
"""
@author: RiditaAli
"""

"""
https://www.kdnuggets.com/convert-python-dict-to-json-a-tutorial-for-beginners
"""

"""
### Convert Python Dict to JSON: A Tutorial for Beginners with FEW tweaks ###
"""

#Libraries
import json
from datetime import datetime

#A dictionary dataset
books = [
	{
    	"title": "The Ethnic Cleansing of Palestine",
    	"author": "Ilan Pape",
    	"publication_year": 2007,
    	"best sellers rank in Amazon Books": "9362"
	},
	{
    	"title": "The Hundred Years' War on Palestine",
    	"author": "Rashid Khalidi",
    	"publication_year": 2021,
    	"best sellers rank in Amazon Books": "508957"
	},
	{
    	"title": "Beyond Chutzpah",
    	"author": "Norman G. Finkelstein",
    	"publication_year": 2008,
    	"best sellers rank in Amazon Books": "82939"
	}
]

#Convert dictionary to JSON string
json_string = json.dumps(books, indent = 4)
print(json_string)

"""
### Converting a Nested Python Dictionary to a JSON String ###
"""

#A dictionary dataset
books = [
	{
    	"title": "The Ethnic Cleansing of Palestine",
    	"author": "Ilan Pape",
    	"publication_year": 2007,
    	"best sellers rank in Amazon Books": "9362",
        "reviews": [
            {"user": "John Pilger", "comment": "bravest, principled, incisive historian"},
            {"user": "Ghada Karmi", "comment": "groundbreaking research"}
            ]
	},
	{
    	"title": "The Hundred Years' War on Palestine",
    	"author": "Rashid Khalidi",
    	"publication_year": 2021,
    	"best sellers rank in Amazon Books": "508957",
        "reviews": [
            {"user": "Carole", "comment": "superb and timely book"},
            {"user": "	Jan", "comment": "real story hidden behind an iron curtain of lies"}
            ]
	},
	{
    	"title": "Beyond Chutzpah",
    	"author": "Norman G. Finkelstein",
    	"publication_year": 2008,
    	"best sellers rank in Amazon Books": "82939",
        "reviews": [
            {"user": "Duncan Macfarlane", "comment": "myth busting backed up by solid evidence"},
            {"user": "David Flack", "comment": "informative read"}
            ]
	}
]

#Convert dictionary to JSON string
json_string = json.dumps(books, indent = 4)
print(json_string)

"""
### Sorting Keys When Converting a Python Dictionary to JSON ###
"""

person = {
	"name": "John Doe",
	"age": 31,
	"email": "john@example.com",
	"address": {
    	"city": "Manchester",
    	"zipcode": "10001",
    	"street": "123 Rusholme Street"
	}
}

# Convert dictionary to a JSON string with sorted keys
json_string = json.dumps(person, sort_keys=True, indent=4)
#the keys are sorted in alphabetical order | if sort_keys=False, not sorting will occur
print(json_string)

"""
### Handling Non-Serializable Data ###
"""

###Erroneous example

"""
data = {
	"event": "Meeting",
	"date": datetime.now()
}

# Converting dictionary to JSON

#if we write like before then we'll run into error when running the code below.
#json_string = json.dumps(data, indent=2)
#Object of type datetime is not JSON serializable.
"""

### *To avoid ERRORS* ###

###Two things need to happen.
#Define a serialize_datetime function that converts datetime objects to ISO 8601 format using the isoformat() method.
#When calling json.dumps(), we set the default parameter to the serialize_datetime function.

#Define a custome serialisation function for datetime objects
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

data = {
	"event": "Meeting",
	"date": datetime.now()
}

# Convert dictionary to JSON 
# with custom serialisation for datetime
json_string = json.dumps(data, default=serialize_datetime, indent=2)
print(json_string)



