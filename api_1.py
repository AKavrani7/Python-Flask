from flask import Flask , url_for , redirect, request

app = Flask(__name__)


@app.route("/")
def hello():
	print("This is API_1 or service provider of API_2")
#	return {"message" : "hey there you pinged me, you can call me a home page" },200 #OK_MSG
	return "hello world" 	

@app.route("/objects" ,methods=['POST'])
def createObject():
	response = "CreateObject Request Recieved"
	print(response)
	return response	


@app.route("/objects" ,methods=['GET'])
def getAllObjects():
	response = "GetAllObjects Request Recieved"
	print(response)
	return response	


@app.route("/objects" ,methods=['PUT'])
def updateObject():
	response = "UpdateObject Request Recieved"
	print(response)
	return response	

@app.route("/objects" ,methods=['DELETE'])
def deleteObject():
	response = "deleteteObject Request Recieved"
	print(response)
	return response	

@app.route("/objects/<string:post_id>" ,methods=['DELETE'])
def deleteObjectbyID(post_id):
	response = "deleteteObject by id: " + str(post_id) + " Request Recieved"
	print(response)
	return response	

@app.route("/objects/<string:post_id>" ,methods=['PUT'])
def updateObjectbyID(post_id):
	response = "updateObject by id: " + str(post_id) + " Request Recieved"
	print(response)
	return response

@app.route("/objects/<string:post_id>" ,methods=['GET'])
def getObjectbyID(post_id):
	response = "getObject by id: " + str(post_id) + " Request Recieved"
	print(response)
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

