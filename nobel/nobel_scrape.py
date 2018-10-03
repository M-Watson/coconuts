import requests


phys_prize_list_url = "https://www.nobelprize.org/prizes/lists/all-nobel-prizes-in-physics/"

page_request = requests.get(phys_prize_list_url)

page_request_content = page_request.text
with open("dump.txt",'w') as f:
	f.write(page_request_content)

print("done")
