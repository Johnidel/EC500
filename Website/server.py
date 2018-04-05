from flask import Flask, jsonify, request, current_app, send_from_directory
import twitter_to_movie as t2m
from pymongo import MongoClient
import datetime

app = Flask(__name__, static_url_path='')

@app.route("/", methods=["GET"])
def send_index():
	return send_from_directory('', 'index.html')

@app.route("/output.mp4", methods=["GET"])
def send_html():
	return send_from_directory('', "output.mp4")

@app.route("/api/histo", methods=["GET"])
def get_histo():
	client = MongoClient()
	db = client["db"]
	users = db["twitter"]
	cursor = users.find({})
	labels = []
	for document in cursor:
		if "phrases" in document.keys():

			for ele in document["phrases"]:
				labels += ele.split(">")
	histd = {}
	for label in labels:
		if label in histd.keys():
			histd[label] += 1
		else:	
			histd[label] = 1

	li = []
	for key in histd.keys():
		li.append([key, histd[key]])
	li = sorted(li, key=lambda x: x[1])[::-1]

	li2 = []
	for key in histd.keys():
		li2.append({"label": key, "y": histd[key]})
	li2 = sorted(li2, key=lambda x: x["y"])[::-1]

	return jsonify(dict(histo=histd, arr=li, ss=li2))

@app.route("/api/getlabels", methods=["GET"])
def get_labels():
	try:
		name = request.args.get("name", None)
		if name is None:
			return jsonify({"error": "No screenname specified"})
		else:
			print(name)
			labels, images = t2m.get_twitter_media_analysis(name, 
													count=200, 
													exclude_replies=True, 
													delete_movie=False)
			phrases = []
			for lab in labels:
				[phrases.append(x[0]) for x in lab["labels"]]

			client = MongoClient()
			db = client["db"]
			users = db["twitter"]
			users.insert_one(dict(handle=name, num_images=len(images), images=images, phrases=phrases, labels=labels, time=datetime.datetime.now().strftime("%Y/%m/%d %H:%M")))
			client.close()
			return jsonify(labels)
	except Exception as e:
		return jsonify({"error":str(e)})

if __name__ == "__main__":
	app.run(host="localhost", use_reloader=False, threaded=True, port=3000)