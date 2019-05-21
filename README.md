# Python-Flask
Flask is a web framework which clients make requests to.
#from flask import request
The Flask request object contains the data that the client (eg a browser) has sent to your app - ie the URL parameters, any POST data, etc.
#import requests
The requests library is for your app to make HTTP request to other sites, usually APIs. 
It makes an outgoing request and returns the response from the external site.

Note:HTTP works as a request-response protocol between a client and server. To access incoming request data, you can use the global request object.
Flask parses incoming request data for you and gives you access to it through that global object. Internally Flask makes sure that you always get the correct data 
for the active thread if you are in a multithreaded environment. 
Some examples of how to get request data: request.form, request.args.get, request.files

Objective:
api_1.py make an api which include these functions: 
	post: create a file
	get: retrieving a file.
	get_by_id: accesing a file based on the source_id. 
	put: upload a file
	put_by_id: upload a file on the source_id
	delete_by_id: remove the item present on the source_id
  
api_2: call the above functions present on api_1 by using api_2

finalApi: In this api we call an api which is used on a webserver.
Note: While Testing the working of your api on postman do make sure you add Authentication, content-type and body.
1. Authentication and Authorization
Authentication: Proving correct identity
Authorization: Allowing a certain action
Authorization checks whether a user is allowed to perform an action or has access to some functionality. For example, having the permission 
to get data and post data is a part of authorization. Web API uses authorization filters to implement authorization.

2. Content-type: application/json
Content-type: application/json; charset=utf-8 designates the content to be in JSON format, encoded in the UTF-8 character encoding.
HTTP headers tell the recipient that what kind of content they're dealing with.

3. BODY part of postman
{   
  "cmd":["environment","argument", "option_1", "value_option_1", "option_2", "value_option_2", "bool_value"],
  "id": "function_id"
}
example:
{
	"cmd":["python3", "index.py", "--png_path", "python-practice-app/test.png", "--bucket", "indshine-test"],
	"id": "40ec015f-ecbf-4ab5-92be-8c8f2b98b94b"
}
