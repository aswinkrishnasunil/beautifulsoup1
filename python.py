from bs4 import BeautifulSoup

import requests
import csv


url = "https://realpython.github.io/fake-jobs/"

result = requests.get(url)	
soup = BeautifulSoup(result.content, 'lxml')

csv_file = open('cms_scraper.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['jobs','location','link'])


#for section in soup.find_all("div",class_='card-content'):

    #print(section.prettify())

    #job = section.h2.text
    #print("job=",job)
section = soup.find(id="ResultsContainer")


#pythonjobs

pjobs= section.find_all(
    "h2",string=lambda text:"python" in text.lower()
    )

pjobsele=[
    h2_element.parent.parent.parent for h2_element in pjobs

]
print(len(pjobs))

for jobs in pjobsele:
    company = jobs.find("h2",class_="title is-5")
    location = jobs.find("h3")
    links = jobs.find_all('a')[1]['href']
    print(company.text)
    print(location.text)
    print(f'apply here:- {links}\n')
    csv_writer.writerow([company.text,location.text,links])

print()



#manager
man= section.find_all(
    "h2",string=lambda text:"manager" in text.lower()
    )

manjobsele=[

    h2_elements.parent.parent.parent for h2_elements in man
]
print(len(man))

for mans in manjobsele:
    companys = mans.find("h2",class_="title is-5")
    locations = mans.find("h3")
    linkss = mans.find_all('a')[1]['href']
    print(companys.text)
    print(locations.text)
    print(f"apply here:- {linkss}\n")

    print()


    
    csv_writer.writerow([companys.text,locations.text,linkss])

csv_file.close()

    
    



    #company = section.h3.text
    #print("company=",company)

    #location = section.find("p",class_="location")
    #print("location=",location.text.strip())

    #para = section.p.text
    #print(para) 

    #alink = section.find('a',class_="button button-elevated button-tertiary-neutral cta ")['href']
    #applelink = f'www.apple.com{alink}'
    #print(applelink)

    #print()