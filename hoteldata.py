import requests
import json
# location search
# location = input("Enter the destination : ")
#
# url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
#
# querystring = {"locale":"en-gb","name":location}
#
headers = {
	"X-RapidAPI-Key": "a71fb91a78msh2b907940678c168p1c4174jsn9d851e261b05",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# location_data = json.loads(response.text)
# dest_type = location_data[0]["dest_type"]
# dest_id = location_data[0] ["dest_id"]


# hotel search


url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

# check_in = input("Enter check in date (yyyy-mm-dd): ")
# check_out = input("Enter check out date (yyyy-mm-dd): ")
# adults_number = input("Enter number of adults :")
# room_number = input("Enter room number :")
# children = input("Enter number of children :")
# children_ages = input("Enter ages of children, separated by commas :")

#querystring = {"checkout_date":check_out,"units":"metric","dest_id":dest_id,"dest_type":dest_type,"locale":"en-gb","adults_number":adults_number,"order_by":"review_score","filter_by_currency":"EUR","checkin_date":check_in,"room_number":room_number,"children_number":children,"page_number":"0","children_ages":children_ages,"categories_filter_ids":"class::2,class::4,free_cancellation::1","include_adjacency":"true"}

querystring = {"checkout_date":"2022-11-15","units":"metric","dest_id":"-126693","dest_type":"city","locale":"en-gb","adults_number":"2","order_by":"review_score","filter_by_currency":"EUR","checkin_date":"2022-11-11","room_number":"1","children_number":"1","page_number":"0","children_ages":"5,0","categories_filter_ids":"class::2,class::4,free_cancellation::1","include_adjacency":"true"}

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
first_hotel =data["result"][0]

hotel_name = first_hotel["hotel_name"]
address = first_hotel["address"]
rating_score = first_hotel["review_score"]
distance_center = first_hotel["distance"]
hotel_ranking = first_hotel["class"]
check_in_time = first_hotel["checkin"]
room_rate_night = first_hotel["composite_price_breakdown"]["product_price_breakdowns"][0]
total_price = first_hotel["min_total_price"]
district = first_hotel["district"]
check_out_time = first_hotel["checkout"]
country = first_hotel["country_trans"]
print(hotel_name, address)
print("rating",rating_score)
print(distance_center)
print(hotel_ranking)
print(room_rate_night)
print(total_price)
print(district)
print(country)





# for k,v in first_hotel.items():
# 	print(k,"#",v)












