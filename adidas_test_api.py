import  requests,jsonpath, json

def get_available_pets(dog_name = "Ronnie"):
    
    list_of_names = []
    get_url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    response = requests.get(get_url)
    json_response = json.loads(response.text)
    #json_response #this is a list
    list_of_names = []
    for i in json_response:
        list_of_names.append(i["name"])
    #list_of_names = [i['name'] for i in json_response]
    #print(list_of_names)

    
    for i in list_of_names:
        if (i == dog_name):
            Dog = dog_name
    
    assert  Dog == dog_name
    print("Assertion is passed")

# Adding a record

post_url = "https://petstore.swagger.io/v2/pet"
json_input = '{"id": 98689798,"category": {"id": 1,"name": "Dog"},"name": "monkey","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}'
req_json = json.loads(json_input)
print((req_json))
response_post = requests.post(post_url,req_json)
#print(response_post.content)
#assert response_post.status_code == 200
get_available_pets(dog_name="sheru")




