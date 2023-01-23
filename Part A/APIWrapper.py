# TODO: Implement Flask Interface 



from flask import Flask, request

app = Flask(__name__)



@app.route('/')

def hello_world():
    return "<h1> Hello WOrld wow</h1>"

@app.route("/topics", methods=["POST", "GET"])
def topics():
    print(request.method)
    if request.method == "POST":
        dict = request.get_json()
        print(dict['topic_name'])
        # TODO : Interact with logging queue and return valid response 
        
        return "test", 205
    
    else:
		# TODO : Return topic list
        return {"topics" : ["banana", "guava", "apple"]}

@app.route("/consumer/register", methods=["POST"])
def register_consumer():
	dict = request.get_json()
	print(dict['topic'])
	# if topic exists send consumer id
	return {"status" : "success",
			"consumer_id" : 1234}
	# else return error
	# return {"status"  : "failure",
	# 		  "message" : "topic not found"}

@app.route("/producer/register", methods=["POST"])
def register_producer():
	dict = request.get_json()
	print(dict['topic'])
	# if topic exists send consumer id
	return {"status" : "success"}
	# else return error
	# return {"status"  : "failure",
	# 		  "message" : "topic not found"}


@app.route("/producer/produce", methods=["POST"])
def enque():
	dict = request.get_json()
	print(dict['topic'])
	# if topic exists send consumer id
	return {"status" : "success"}
	# else return error
	# return {"status"  : "failure",
	# 		  "message" : "topic not found"}

@app.route("/consumer/consume", methods=["POST"])
def deque():
	dict = request.get_json()
	print(dict['topic'])
	# if topic exists send consumer id
	return {"status" : "success"}
	# else return error
	# return {"status"  : "failure",
	# 		  "message" : "topic not found"}

@app.route("/size", methods=["GET"])
def size():
	dict = request.get_json()
	print(dict['topic'])
	# if topic exists send consumer id
	return {"status" : "success"}
	# else return error
	# return {"status"  : "failure",
	# 		  "message" : "topic not found"}

if __name__ == '__main__':
    app.run(debug=True)