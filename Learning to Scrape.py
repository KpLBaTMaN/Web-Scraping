from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://webscraper.io/test-sites/e-commerce/allinone').text
soup = BeautifulSoup(source, 'lxml')

#File open and write
csv_file = open('E-commerce_Information.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Description', 'Price'])


#All content - find section
content = soup.find('div', class_="col-md-9")

#Row in the content - Find row of content
row = content.find('div', class_="row")

#item = row.find('div', class_="caption")
#Searches all items for list
for item in row.find_all('div', class_="caption"):
    #single item
    title = item.find('a', class_="title").text
    description = item.find('p', class_="description").text
    price = item.find('h4', class_="pull-right price").text

    print(title)
    print(description)
    print(price)

    csv_writer.writerow([title, description, price]) #writes to file

csv_file.close() #close file - important



#Notes
#match = soup.find('div', class_="col-sm-4 col-lg-4 col-md-4")
#price = soup.find('h4', class_="pull-right price")

#match = soup.title
#print(match)

#match = soup.find('div', class_='mySlides')

#match2 = soup.find('div', class_='w3-container')
#print(match2)