from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def Bye():
	print("This is API_2, I will fulfill your request by calling API_1")
#	return {"message" : "hey there you pinged me, you can call me a home page" },200 #OK_MSG
	return "Doomsday" 	

@app.route("/rqsts" ,methods=['POST'])
def createObject():	
	response = "hey Objects plzz create an object"
	print(response)
	print("final response : ")
	r = requests.post('http://localhost:5000/objects')
	return r.text	


@app.route("/rqsts" ,methods=['GET'])
def getAllObjects():
	response = "hey Objects get your mates"	
	print(response)
	print("final response : ")
	r = requests.get('http://localhost:5000/objects')
	return r.text


@app.route("/rqsts" ,methods=['PUT'])
def updateObject():
	response = "hey Objects update my object"
	print(response)
	print("final response : ")
	r = requests.put('http://localhost:5000/objects')
	return r.text	

@app.route("/rqsts" ,methods=['DELETE'])
def deleteObject():
	response = "hey objects delete him"
	print(response)
	print("final response : ")
	r = requests.delete('http://localhost:5000/objects')
	return r.text	

@app.route("/rqsts/<string:post_id>" ,methods=['DELETE'])
def deleteObjectbyID(post_id):
	response = "delete this Object by id: " + str(post_id) + " do it asap"
	print(response)
	print("final response : ")
	r = requests.delete('http://localhost:5000/objects/<string:post_id>')
	return r.text

@app.route("/rqsts/<string:post_id>" ,methods=['PUT'])
def updateObjectbyID(post_id):
	response = "update this Object by id: " + str(post_id) + " do it asap"
	print(response)
	print("final response : ")
	r = requests.put('http://localhost:5000/objects/<string:post_id>')
	return r.text

@app.route("/rqsts/<string:post_id>" ,methods=['GET'])
def getObjectbyID(post_id):
	response = "get this Object by id: " + str(post_id) + " do it asap"
	print(response)
	print("final response : ")
	r = requests.get('http://localhost:5000/objects/<string:post_id>')
	return r.text

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

