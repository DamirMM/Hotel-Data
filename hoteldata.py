import requests
import json
# location search
location = input("Enter the destination : ")

url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

querystring = {"locale":"en-gb","name":location}

headers = {
	"X-RapidAPI-Key": "a71fb91a78msh2b907940678c168p1c4174jsn9d851e261b05",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
location_data = json.loads(response.text)
dest_type = location_data[0]["dest_type"]
dest_id = location_data[0] ["dest_id"]


# hotel search


url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

check_in = input("Enter check in date (yyyy-mm-dd): ")
check_out = input("Enter check out date (yyyy-mm-dd): ")
adults_number = input("Enter number of adults :")
room_number = input("Enter room number :")
children = input("Enter number of children :")
children_ages = input("Enter ages of children, separated by commas :")


querystring = {"checkout_date":check_out,"units":"metric","dest_id":dest_id,"dest_type":dest_type,"locale":"en-gb","adults_number":adults_number,"order_by":"review_score","filter_by_currency":"EUR","checkin_date":check_in,"room_number":room_number,"children_number":children,"page_number":"0","children_ages":children_ages,"categories_filter_ids":"class::2,class::4,free_cancellation::1","include_adjacency":"true"}

#querystring = {"checkout_date":"2022-11-20","units":"metric","dest_id":"-126693","dest_type":"city","locale":"en-gb","adults_number":"2","order_by":"review_score","filter_by_currency":"EUR","checkin_date":"2022-11-17","room_number":"1","children_number":"1","page_number":"0","children_ages":"5,0","categories_filter_ids":"class::2,class::4,free_cancellation::1","include_adjacency":"true"}

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
#print(data)
for i in range(0,5):
	hotel = data["result"][i]
	hotel_name = hotel["hotel_name"]
	address = hotel["address"]
	rating_score = hotel["review_score"]
	distance_center = hotel["distance"]
	hotel_ranking = hotel["class"]
	check_in_time = hotel["checkin"]
	room_rate_night = hotel["composite_price_breakdown"]["product_price_breakdowns"][0]
	if 'strikethrough_amount_per_night' in room_rate_night.keys():
		room_rate_night = round(room_rate_night['strikethrough_amount_per_night']["value"])
	total_price = hotel["min_total_price"]
	district = hotel["district"]
	check_out_time = hotel["checkout"]
	country = hotel["country_trans"]
	print(i)
	print(hotel_name, address)
	print("rating :",rating_score)
	print("distance:", distance_center)
	print("ranking : ", hotel_ranking)
	print("room_rate :", room_rate_night)
	print("total:",total_price)
	print(district)
	print(country)





# for k,v in hotel.items():
# 	print(k,"#",v)












