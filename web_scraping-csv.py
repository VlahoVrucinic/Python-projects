import requests
import bs4
import csv


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
titles = []
# tu se naslovi stavljaju u praznu listu

for n in range(1,51):
    
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    book = soup.select('.product_pod')

    
    for book in books:
        titles.append(book.select('a')[1]['title'])

# tu se otvara csv file i to se sve prepisuje u njega

header = ['Title']

file = open('titles.csv','w+', newline = '')

with file:
    write = csv.writer(file, delimiter = ',')
    write.writerow(header)
    write.writerows([x.split(',') for x in titles]) 