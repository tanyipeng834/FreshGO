from invokes import invoke_http
from os import environ

profile_URL = environ.get('profileURL') or input("Enter Profile service URL: ")  

print("1. Wait for Profile service to be up.")
# invoke profile microservice to get all id
results = invoke_http(profile_URL, method='GET')

count = 1
MAX_TRIES = 100
while results["code"] in range(500,600) and count < MAX_TRIES:
    count = count + 1
    print(str(count) + ". Wait for Book service to be up.")
    # invoke book microservice to get all books
    results = invoke_http(profile_URL, method='GET')
print()

if count >= MAX_TRIES:
    print("Cannot connect to Book service")
    print()
    print( results )
    exit

print( type(results) )
print()
print( results )

# invoke book microservice to create a book
isbn = '9213213213213'
book_details = { "availability": 5, "price": 213.00, "title": "ESD" }
create_results = invoke_http(
        profile_URL + "/" + isbn, method='POST', 
        json=book_details
    )

print()
print( create_results )
