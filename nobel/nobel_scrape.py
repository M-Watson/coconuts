import requests
from bs4 import BeautifulSoup as bs

phys_prize_list_url = "https://www.nobelprize.org/prizes/lists/all-nobel-prizes-in-physics/"

page_request = requests.get(phys_prize_list_url)

page_request_content = page_request.content
page_request_text = page_request.text
with open("dump.txt",'w') as f:
	f.write(page_request_text)


soup = bs(page_request_text)
all_divs = soup.findAll('div')
div_by_year = soup.findAll('div', {"class": "by_year"})

for div in div_by_year:
	with open("dumpdiv.txt",'a') as f:
		output = str(div) + '\n'
		f.write(output)



print("done")
