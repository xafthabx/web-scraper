import urllib2
import csv
import re
from bs4 import BeautifulSoup

# https://www.artgallery.nsw.gov.au/collection/works/?page=1
# https://www.artgallery.nsw.gov.au/collection/works/?page=543
# https://www.artgallery.nsw.gov.au/collection/works/
#https://www.artgallery.nsw.gov.au/collection/works/50.2014/

base_target_link = 'https://www.artgallery.nsw.gov.au/collection/works/?page='

output_file = open('list-of-works.csv', 'w')
print >> output_file, "artist name,title,country,year,ref,url"

bad_links = []

for i in range(1, 544):
    target_link = base_target_link + str(i)
    #target_link = base_target_link + '2'
    print target_link

    page = urllib2.urlopen(target_link)
    soup = BeautifulSoup(page, 'html.parser')

    page_result = soup.find_all('div', attrs={'class': 'result'})

    all_works = ["artist_name, piece_title, work_credit, piece_ref, piece_url, page_number"]
    
    for result in page_result:
        artist_name = result.find('span', attrs={'class': 'artist'}).text.encode('utf-8').strip()
        piece_title = result.find('span', attrs={'class': 'title'}).text.encode('utf-8').strip()
        piece_ref = result.find('span', attrs={'class': 'meta'}).text.encode('utf-8').strip()
        piece_href = result.find('a')['href'].encode('utf-8')
        piece_url = 'https://www.artgallery.nsw.gov.au' + piece_href
        ###go to each work page
        try:
            page2 = urllib2.urlopen(piece_url)
        except:
            page2 = ''
            bad_links.append(piece_url)

        soup2 = BeautifulSoup(page2, 'html.parser')
        try:
            work_origin_raw = soup2.find('div', attrs={'class': 'artist'}).p.text.encode('utf-8').strip()
            work_origin = re.sub ('\s+', ' ', work_origin_raw)
        except:
            work_origin = "NOT FOUND"

        try:
            piece_year = soup2.find('article', attrs={'class': 'collection_work'}).find('div', attrs={'class': 'hero'}).find('div', attrs={'class': 'left'}).find('div').p.get_text(strip=True, separator=" ").encode('utf-8').strip()
        except:
            piece_year = "NOT FOUND"
        
        try:
            work_credit_raw = soup2.find('div', attrs={'class': 'credit'}).p.text.encode('utf-8').strip()
            work_credit = re.sub ('\s+', ' ', work_credit_raw)
        except:
            work_credit = "NOT FOUND"

        work = "\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",{5}, {6}, {7}".format(artist_name, piece_title, work_origin, piece_year, work_credit, piece_ref, piece_url, i)
        all_works.append(work)
        print work
        print >> output_file, work

    print all_works
output_file.close()

thefile = open('bad_links.txt', 'w')
for item in bad_links:
      thefile.write("%s\n" % item)

thefile.close()
