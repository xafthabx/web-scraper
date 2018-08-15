import urllib2
from bs4 import BeautifulSoup

target_page = 'https://www.artgallery.nsw.gov.au/collection/works/'

page = urllib2.urlopen(target_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

all_works = []


artist_name = (soup.find('span', attrs={'class': 'artist'})).text.strip()
print artist_name

piece_title = (soup.find('span', attrs={'class': 'title'})).text.strip()
print piece_title

piece_ref = (soup.find('span', attrs={'class': 'meta'})).text.strip()
print piece_ref
work = "{0}, {1}, {2}".format (artist_name, piece_title, piece_ref)
#all_works.append(", %s, %s" % artist_name % piece_ref % piece_ref)
all_works.append(work)

print all_works