import urllib2
import csv
import re
from bs4 import BeautifulSoup

# https://www.artgallery.nsw.gov.au/collection/works/?page=1
# https://www.artgallery.nsw.gov.au/collection/works/?page=543
# https://www.artgallery.nsw.gov.au/collection/works/

piece_url = 'https://www.artgallery.nsw.gov.au/collection/works/477.1979/'
page = urllib2.urlopen(piece_url)
soup = BeautifulSoup(page, 'html.parser')

piece_url_2 = 'https://www.artgallery.nsw.gov.au/collection/works/168.1981/'
page_2 = urllib2.urlopen(piece_url_2)
soup_2 = BeautifulSoup(page_2, 'html.parser')

work_detail = soup.find('div', attrs={'id': 'details'})
location = re.sub ('\s+', ' ', work_detail.p.text.strip())

work_origin_raw = soup2.find('div', attrs={'class': 'artist'}).p.text.strip()
work_origin = re.sub ('\s+', ' ', work_origin_raw)






#https://www.artgallery.nsw.gov.au/collection/works/168.1981/

page = urllib2.urlopen(piece_url)
soup = BeautifulSoup(page, 'html.parser')
work_title = soup.find('h1', attrs={'class': 'title'}).text.strip()
work_dated = soup.find('article', attrs={'class': 'collection_work'}).find('div', attrs={'class': 'hero'}).find('div', attrs={'class': 'left'}).find('div').p.get_text(strip=True, separator=" - ")
work_country = 

Title 
Year Made (this should be with the title)
Artist name
Accession number
Country artist is from 
Url

So for that page it would be:

Shield
Early 20th Century
Unknown artist
477.1979
(There’s no country but usually has it)
https://www.artgallery.nsw.gov.au/collection/works/477.1979/

<article class='collection_work'>

	<div class='hero'>
		<div class='left'>
			<div>
				<hr />
				<h6>Title</h6>
				<h1 class="title">
					Shield
				</h1>
				
        			<div>
        				<p>
        					early 20th century<br/>collected circa 1972
        				</p>
        			</div>
        		



















for i in range(543):
    target_link = base_target_link + str(i)
    #target_link = base_target_link + '2'
    print target_link

    page = urllib2.urlopen(target_link)
    soup = BeautifulSoup(page, 'html.parser')

    page_result = soup.find_all('div', attrs={'class': 'result'})

    all_works = ["artist_name, piece_title, piece_ref, piece_url"]
    output_file = open('list-of-works.csv', 'w')
    print >> output_file, "artist_name, piece_title, piece_ref, piece_url"


    for result in page_result:
        artist_name = result.find('span', attrs={'class': 'artist'}).text.encode('utf-8').strip()
        piece_title = result.find('span', attrs={'class': 'title'}).text.encode('utf-8').strip()
        piece_ref = result.find('span', attrs={'class': 'meta'}).text.encode('utf-8').strip()
        piece_href = result.find('a')['href'].encode('utf-8')
        piece_url = 'https://www.artgallery.nsw.gov.au' + piece_href
        work = "\"{0}\",\"{1}\", {2}, {3}".format(artist_name, piece_title, piece_ref, piece_url)
        all_works.append(work)
        #print >> output_file, work

    print all_works
    output_file.close()

    with open("Output.csv","wb") as Output_csv:
        for work_again in all_works:
            CSVWriter = csv.writer(Output_csv)
            CSVWriter.writerow(work_again)
    





# artist_name = (soup.find('span', attrs={'class': 'artist'})).text.strip()
# print artist_name

# piece_title = (soup.find('span', attrs={'class': 'title'})).text.strip()
# print piece_title

# piece_ref = (soup.find('span', attrs={'class': 'meta'})).text.strip()
# print piece_ref
# work = "{0}, {1}, {2}".format (artist_name, piece_title, piece_ref)
# #all_works.append(", %s, %s" % artist_name % piece_ref % piece_ref)
# all_works.append(work)
# print all_works

# for element in soup.find_all(text=re.compile("artist")):
#     print element    
#     #print(element.get_text())

# a = soup.find_all('span', attrs={'class': 'artist'})




# for detail in response.xpath("//div[@class='detail-all-text']/b"):
#     name = detail.xpath("text()").extract()[0]
#     value = detail.xpath("following-sibling::text()")[0]

#     print name, value


# for detail in page.xpath("//div[@class='result']/b"):
#     name = detail.xpath("text()").extract()[0]
#     value = detail.xpath("following-sibling::text()")[0]

#     print name, value

