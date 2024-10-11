import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# Input the target job keyword
targetJob = input("Please Enter Target Job: ")

# Lists to store data
jobTitleList = []
companiesNameList = []
locationCompanyList = []
jobSkillsList = []
linksJob = []


# Make a request to the URL
page = requests.get(f"https://wuzzuf.net/search/jobs/?q={targetJob}&a=hpb")
src = page.content

# Parse the page content
soup = BeautifulSoup(src, "lxml")

# Find relevant data on the page
jobTitle = soup.find_all("h2", {"class": "css-m604qf"})
companiesName = soup.find_all("a", {"class": "css-17s97q8"})
locationCompany = soup.find_all("span", {"class": "css-5wys0k"})
jobSkills = soup.find_all("div", {"class": "css-y4udm8"})

# Loop through the results and append data to lists
for i in range(len(jobTitle)):
    # Extract job title
    jobTitleList.append(jobTitle[i].text.strip())
    
    # Extract link from the anchor tag inside job title
    jobLink = jobTitle[i].find("a")
    if jobLink and 'href' in jobLink.attrs:
        linksJob.append(jobLink.attrs['href'])
    else:
        linksJob.append(None)  # If no link is found
    
    # Extract company name
    companiesNameList.append(companiesName[i].text.strip())
    
    # Extract location
    locationCompanyList.append(locationCompany[i].text.strip())
    
    # Extract job skills
    jobSkillsList.append(jobSkills[i].text.strip())

# Prepare data for CSV export
fileList = [jobTitleList, companiesNameList, locationCompanyList, jobSkillsList, linksJob]
exported = zip_longest(*fileList)  # Unpacking for writing to CSV

# Write data to CSV file
with open('D:\\programing\\Python\\webScrping\\Jobs.csv', 'w') as outputFile:
    dicWriter = csv.writer(outputFile)
    dicWriter.writerow(["Job Title", "Company Name", "Location", "Job Skills", "Links"])
    dicWriter.writerows(exported)

print("Data has been successfully written to Jobs.csv")
