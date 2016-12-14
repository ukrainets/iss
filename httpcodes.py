import requests

r = requests.get("http://api.open-notify.org/iss-now.json?")
a = r.status_code
"""
def HttpCodeToText():
    if a == 200:
        ConStatus = "200 - Connection is OK!"
    elif a == 400:
        ConStatus = "400 - Bad Request.\n(Please check your request code for correctness.)"
    elif a == 404:
        ConStatus == "404 - Not found.\n(The server has not found anything matching the Request-URI.)"
    elif a == 500:
        ConStatus == "500 - Internal Server Error.\n(The server encountered an unexpected condition which prevented it from fulfilling the request.)"
    else:
        ConStatus = "Uncnown HTTP status code.\n(http status code doesn't match our records.)"
    print(ConStatus)
"""
if a == 200:
    ConStatus = "200 - Connection is OK!"
elif a == 400:
    ConStatus = "400 - Bad Request.\n(Please check your request code for correctness.)"
elif a == 404:
    ConStatus == "404 - Not found.\n(The server has not found anything matching the Request-URI.)"
elif a == 500:
    ConStatus == "500 - Internal Server Error.\n(The server encountered an unexpected condition which prevented it from fulfilling the request.)"
else:
    ConStatus = "Uncnown HTTP status code.\n(http status code doesn't match our records.)"
print(ConStatus)


"""
if a == 200:
    print("200 - Connection is OK!")    
else:
    print("Something went wrong\n  o_O  ")



    if weight > 120:
    print('Sorry, we can not take a suitcase that heavy.')
elif weight > 50:
    print('There is a $25 charge for luggage that heavy.')

__________


def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter

"""
