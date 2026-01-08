# Client Tracker App

## Tracks clients and allows the user to: 
* ### Edit  
* ### View 
* ### Delete 
* ### Add  
* ### Search 
* ### Quit 

## Introduction 
This code's purpose is to allow the user (targeted at small businesses) to easily track any clients they have and to be able to be able to store 
their client's information into a csv file.<br><br>
A client typically has these values assigned to them. 
* Day: (Expected to only have one occurrence e.g "06/01/2026" should only occur once in the whole date key) 
* Number of Hours: (Should only be in numerical formats) 
* Student: (Can be any name, it could even be alphanumerical) 
* Notes: (A short note about the client is expected)

## Installation 
- Works with python 3.12 +   
- Open command terminal in virtual environment and paste the following
```
pip install -r requirements.txt
```


## Example of a database values 
```python 
database = {"Date":['06/01/2026'], "Hours":[12.0],"Student":['James'], "Notes":["A good listener"]}
``` 
- Date: The date the user met with the client 
- Hours: The number of hours the user conversed with the client on that day 
- Student: The name of the student they conversed with  
- Notes: Any general short notes the user has on the client 

## Enforcement for certain columns 
- ### Dates 
    - The code only allows dates to be added in the format DD/MM/YYYY 
    - Only dates that actually exists can be added
      - (e.g 29/02/2026 can't be added because it's not an actual date, 2026 isn't a leap year) 
    - The date must be separated by " / " if not invalid date format is raised 
<br></br>  
    - <b> Subtle Limitation </b> 
    - There is nothing to stop the user from adding multiple instances of the same date to the csv file 
      - Hence, if they try to search for a certain date, and it occurs multiple times, only the last occurrence is returned

- ### Hours 
    - The code only allows numeric values to be stored in this column 
<br></br>  
    - <b> Subtle Limitation </b> 
    - Values tend to shuffle between being float and integer values in the duration program and stored in csv file as float
      - This may cause problems further down the road of development 

- ### Student & Notes
    - Doesn't currently have any enforcement  
<br>
    - <b> Subtle Limitation </b> 
    - If a student is named something such as an escape character 
    - It could cause unwanted formatting in output when displaying the csv file

```python 
student = "\n" 
notes = "\t"
```

## How main functions in the code work 
- ### Edit  
  - The user selects a date, and it allows them to edit all values for given date (they can even change the current date)
- ### View  
  - The user views all the dates in the csv file along with their associated values
- ### Delete  
  - The user removes a date and all values associated with the date entry from the database
- ### Add  
  - The user adds a date and all the associated values to the database
- ### Search  
  - The user searches for an entry in the database by using any of the columns as a searchable parameter
- ### Quit  
  - Terminates the program 

## Plans for future development
Plans are in the works to make this a GUI in the foreseeable future.
<br>Contact me at https://www.linkedin.com/in/othniel-amos-02531b3a5/ 

## Learning and personal experience 
Another reason why I wanted to make this app is to challenge myself and prompt myself to learn how to find answer to problems 
encountered when coding (like consulting StackOverflow and Reddit for dictionary problems). 




