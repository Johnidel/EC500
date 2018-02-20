from flask import Flask, jsonify, request, current_app, send_from_directory
import APIEXERCISE

app = Flask(__name__, static_url_path='')

@app.route("/", methods=["GET"])
def send_index():
	return send_from_directory('', 'index.html')

@app.route("/output.mp4", methods=["GET"])
def send_html():
	return send_from_directory('', path + ".mp4")

@app.route("/api/getlabels", methods=["GET"])
def get_labels():
	try:
		name = request.args.get("name", None)
		if name is None:
			return jsonify({"error": "No screenname specified"})
		else:
			print(name)
			labels = APIEXERCISE.to_movie(name)
			return jsonify(labels)
	except Exception as e:
		return jsonify({"error":str(e)})

if __name__ == "__main__":
	app.run(host="localhost", use_reloader=False, threaded=True, port=3000)