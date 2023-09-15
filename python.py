# This Python code is a web scraping script that extracts job listings from a website and stores them in a CSV (Comma-Separated Values) file.
# Here's a breakdown of the code along with some documentation:
# This script is designed to scrape job listings from the specified URL.

# - Import Necessary Libraries:
from bs4 import BeautifulSoup           # For parsing HTML content
import requests                         # For making HTTP requests to the website
import csv                              # For working with CSV files

# - Define the url of the website

url = "https://realpython.github.io/fake-jobs/"

# - Make an HTTP Request and Parse the HTML:

result = requests.get(url)	
soup = BeautifulSoup(result.content, 'lxml')  
# This code sends an HTTP GET request to the URL and uses BeautifulSoup to parse the HTML content of the response.

# - Create a CSV File for Storing Data:

csv_file = open('cms_scraper.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['jobs','location','link'])
# Here, a CSV file named 'cms_scraper.csv' is created, and a CSV writer is initialized with column headers: 'jobs', 'location', and 'link'.

# - Find the Section with Job Listings:
section = soup.find(id="ResultsContainer")
# This line locates the HTML element with the ID "ResultsContainer," which typically contains the job listings.


# - Scrape Job Listings with "Python" in the Title:

pjobs= section.find_all(
    "h2",string=lambda text:"python" in text.lower()
    )
# This code finds all "h2" elements whose text contains the word "python" (case-insensitive) within the "ResultsContainer" section.

pjobsele=[
    h2_element.parent.parent.parent for h2_element in pjobs  

]  # contains the three levels of parent elements for each "h2" element in the pjob list.
# This is often done to capture more context around the found elements, 
# such as additional information related to the job listings that might be in higher-level HTML elements.
print(len(pjobs))

# - Extract and Print Python Job Details:

for jobs in pjobsele:
    company = jobs.find("h2",class_="title is-5")
    location = jobs.find("h3")
    links = jobs.find_all('a')[1]['href']

# Print job details
    
    print(company.text)
    print(location.text)
    print(f'apply here:- {links}\n')

# Write job details to the CSV file    
    csv_writer.writerow([company.text,location.text,links])

# This loop iterates through the Python job listings, extracts job title, location, and link details,
#  prints them to the console, and writes them to the CSV file.

print()



# - Repeat the Process for "Manager" Jobs:
man= section.find_all(
    "h2",string=lambda text:"manager" in text.lower()   #The lambda function is used as a filter to perform this case-insensitive check.
    )

# This code finds all "h2" elements containing the word "manager" (case-insensitive) within the "ResultsContainer" section.

manjobsele=[

    h2_elements.parent.parent.parent for h2_elements in man
]
 # contains the three levels of parent elements for each "h2" element in the man list.
# This is often done to capture more context around the found elements, 
# such as additional information related to the job listings that might be in higher-level HTML elements.

print(len(man))

for mans in manjobsele:
    companys = mans.find("h2",class_="title is-5")
    locations = mans.find("h3")
    linkss = mans.find_all('a')[1]['href']

# Print manager job details

    print(companys.text)
    print(locations.text)
    print(f"apply here:- {linkss}\n")

    print()

# Write manager job details to the CSV file
    
    csv_writer.writerow([companys.text,locations.text,linkss])

# This loop iterates through the manager job listings, extracts job title, location, and link details,
#  prints them to the console, and writes them to the CSV file.

# - Close the CSV File:
csv_file.close()  # This line closes the CSV file once all data has been written.

# In summary, this code scrapes job listings from a website,
# filters them based on keywords ("python" and "manager"), extracts relevant information,
# prints it to the console, and saves it to a CSV file for further analysis or use.    
    



  