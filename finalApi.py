from flask import Flask, request
import json
import requests

app = Flask(__name__)


@app.route("/")
def Batman():
	print("hey there you pinged me, you can call me final API ")
#	return {"message" : "hey there you pinged me, you can call me a home page" },200 #OK_MSG
	return "I am Batman!! running on final api" 	

@app.route("/picture" ,methods=['POST'])
def hello_Lighthouse():	
	url = "https://lighthouse-api.indshine.com/api/v2/jobs"
	#you can use any other api
	print(request.headers) 
	print(request.data)
	#Initially they are empty so 2 blank lines will be printed on terminal
	r = requests.post(url, headers={'Authorization': request.headers['Authorization'], 'Content-Type': 'application/json'}, data=request.data)
	print(r.text)
	print(request.headers) 
	print(request.data)
	#respective value of header and data will be printed on different lines.
	return "Job Done"


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

