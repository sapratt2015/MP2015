import requests, json
nextpage = True
url = 'http://www.brooklynmuseum.org/opencollection/api/?method=collection.search&keyword=manuscript&start_index=0&results_limit=20&require_image=true&image_results_limit=1&sort_field=relevance&api_key=31dg56cAuk&version=1&include_image_caption=false&include_item_fields=true&thumb_shape=original&max_thumb_size=96&max_image_size=384&format=json&include_html_style_block=true&start_index=20'
#Count the total number of manuscripts, then only Persian or Iranian from the group
general_manuscript = 0
focus_group = 0
while nextpage == True : 
	
	#Ask for search results from url, where terms are searched to isolate manuscript collection   
	r = requests.get(url)
	#turn into python dictionary
	data = json.loads(r.text)


	for item in data["response"]["resultset"]["items"]: 
		general_manuscript = general_manuscript+1
		#loop through each item and then through the country of origin	
		if "Persian" in str(item) or "Iranian" in str(item):
			focus_group = focus_group+1
			print (item)
	
	if "next_uri" in data["response"]["resultset"]: 
	
		url = data["response"]["resultset"]["next_uri"]
	else: 
		nextpage = False

print(general_manuscript)
print(focus_group)
