from invokes import invoke_http
from os import environ

purchase_request_URL = environ.get('purchase_request_URL') or input("Enter Book service URL: ")  

# invoke book microservice to get all books
results = invoke_http(purchase_request_URL, method='GET')

print( type(results) )
print()
print( results )

