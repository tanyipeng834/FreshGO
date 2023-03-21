# test_invoke_http.py
from invokes import invoke_http

# invoke book microservice to get all books
results = invoke_http("http://localhost:5000/inventory", method='GET')
print( type(results) )
print()
print( results )

crop_details = {
    "name": "XinGaga",
    "batch": 11,
    "shell_life": "2 Years",
    "price": 2.00 ,
    "height": 5.00,
    "quantity": 3,
    "date": "2020-03-02",
    "type": "veget"
}
results = invoke_http("http://localhost:5000/inventory", method='POST', json=crop_details )
print()
print(results)