
# ISS API
# 
import requests

r = requests.get("http://api.open-notify.org/iss-now.json?")

q = input("ISS API, what is you question about?: ")
if q == "connection":
    print("ISS API conection status is:", r.status_code)

else:
	print("Connection status is: ", r.status_code, "\n" "All ISS API data: \n", r.text)

#print(r.status_code, "\n", r.text)