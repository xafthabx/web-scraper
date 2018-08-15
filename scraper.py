import urllib2
import csv
import re
from bs4 import BeautifulSoup

# https://www.artgallery.nsw.gov.au/collection/works/?page=1
# https://www.artgallery.nsw.gov.au/collection/works/?page=543
# https://www.artgallery.nsw.gov.au/collection/works/


base_target_link = 'https://www.artgallery.nsw.gov.au/collection/works/?page='

output_file = open('list-of-works.csv', 'w')
print >> output_file, "artist name, title, ref, url"

for i in range(543):
    target_link = base_target_link + str(i)
    #target_link = base_target_link + '2'
    print target_link

    page = urllib2.urlopen(target_link)
    soup = BeautifulSoup(page, 'html.parser')

    page_result = soup.find_all('div', attrs={'class': 'result'})

    all_works = ["artist_name, piece_title, piece_ref, piece_url"]
    
    for result in page_result:
        artist_name = result.find('span', attrs={'class': 'artist'}).text.encode('utf-8').strip()
        piece_title = result.find('span', attrs={'class': 'title'}).text.encode('utf-8').strip()
        piece_ref = result.find('span', attrs={'class': 'meta'}).text.encode('utf-8').strip()
        piece_href = result.find('a')['href'].encode('utf-8')
        piece_url = 'https://www.artgallery.nsw.gov.au' + piece_href
        work = "\"{0}\",\"{1}\", {2}, {3}".format(artist_name, piece_title, piece_ref, piece_url)
        all_works.append(work)
        print >> output_file, work

    print all_works
output_file.close()