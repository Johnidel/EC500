import twitter
import json
import urllib.request
import os

with open("keys.dat") as f:
	keys = f.read().split()
api = twitter.Api(consumer_key= keys[0],
			consumer_secret=keys[1],
			access_token_key=keys[2],
			access_token_secret=keys[3])

res = api.GetUserTimeline(screen_name="dannygarcia95", count=200, trim_user=True, exclude_replies=True)
images = []
for tweet in res:
	js = tweet._json["entities"]
	if "media" in js.keys():
		for media in js["media"]:
			if media["media_url"][-3:] == "jpg":
				images.append(media["media_url"])

for i in range(len(images)):
	urllib.request.urlretrieve(images[i], "tmp_" + str(i).zfill(4) + ".jpg")

for i in range(len(images)):
	os.remove("tmp_" + str(i).zfill(4) + ".jpg")

