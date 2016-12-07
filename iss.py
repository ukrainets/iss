import requests

r = requests.get("https://api.open-notify.org/iss-now.json")
status = r.status_code

# Replasing http status code with text
if status == 200:
    ConStatus = "200 - Connection is OK!"
elif status == 400:
    ConStatus = "400 - Bad Request.\n(Please check your request code for correctness.)"
elif status == 404:
    ConStatus == "404 - Not found.\n(The server has not found anything matching the Request-URI.)"
elif status == 500:
    ConStatus == "500 - Internal Server Error.\n(The server encountered an unexpected condition which prevented it from fulfilling the request.)"
else:
    ConStatus = "Uncnown HTTP status code.\n(http status code doesn't match our records.)"

# UI
q = input('ISS API \n Type "cnnection" to see conncetion status:\n')
if q == "connection":
    print("ISS API conection status is:\n", ConStatus)
else:
	print("Ooops, you entered incorrect command \nor \nwe can't check ISS conection status at the moment")
