import requests, json

nextpage = True
pagenumber = 1
#Count the total number of manuscripts, then only Persian or Iranian from the group
general_manuscripts = 0
focus_group = 0
while nextpage == True : 
	#Ask for search results by using ID of collection - 3 is manuscripts - sort further by using Object ID for collection name  
	r = requests.get('http://api.thewalters.org/v1/collections/3/objects?orderBy=ObjectID&apikey=NpMwnjS9mYjQZNihW2t3m3ORtONhOHWndHFTJXArEd4Kt70i8HQIlY5JQv3OLlkU&page='+str(pagenumber))
	#turn into python dictionary
	data = json.loads(r.text)
	 
	
	if data["NextPage"] == True : 
		pagenumber = pagenumber +1
	else : 
		nextpage = False 
	
	for item in data["Items"] : 
		#loop through each item and then through the country of origin	
		general_manuscripts = general_manuscripts+1
		if "Persian" in item["Creator"] or "Iran" in item["Creator"]:
			focus_group = focus_group+1
				
			print (item["Creator"])	

			
			print (item["DateBeginYear"])
			print (item["Title"])


	
print(general_manuscripts)
print(focus_group)	
	
	
	





