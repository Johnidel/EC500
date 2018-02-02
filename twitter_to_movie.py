import twitter
import json
import urllib.request
import os
import subprocess

with open("keys.dat") as f:
	keys = f.read().split()
api = twitter.Api(consumer_key= keys[0],
			consumer_secret=keys[1],
			access_token_key=keys[2],
			access_token_secret=keys[3])

res = api.GetUserTimeline(screen_name="Omz2007", count=200, trim_user=True, exclude_replies=True)
images = []
for tweet in res:
	js = tweet._json["entities"]
	if "media" in js.keys():
		for media in js["media"]:
			if media["media_url"][-3:] == "jpg":
				images.append(media["media_url"])

for i in range(len(images)):
	urllib.request.urlretrieve(images[i], "tmp_{}.jpg".format(str(i).zfill(4)))

for i in range(len(images)):

	subprocess.call(('''ffmpeg -loop 1 -i tmp_{}.jpg -c:a libfdk_aac -ar 44100 -ac 2 -vf "scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)',                                  pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -b:v 10M -pix_fmt yuv420p -r 30 -shortest -avoid_negative_ts make_zero -fflags +genpts -t 1 tmp_{}.mp4''').format(str(i).zfill(4) , str(i).zfill(4)),
		cwd=os.path.dirname(os.path.realpath(__file__)), shell=True, env=dict(os.environ, PATH="C:/Users/johnidel/Downloads/ffmpeg-20180201-b1af0e2-win64-static/ffmpeg-20180201-b1af0e2-win64-static/bin"))

with open("tmp_files.txt", "w") as f:
	for i in range(len(images)):
		f.write("file 'tmp_{}.mp4'\n".format(str(i).zfill(4)))


subprocess.call("ffmpeg -f concat -i tmp_files.txt output.mp4",
	cwd=os.path.dirname(os.path.realpath(__file__)),
	shell=True,
	env=dict(os.environ, PATH="C:/Users/johnidel/Downloads/ffmpeg-20180201-b1af0e2-win64-static/ffmpeg-20180201-b1af0e2-win64-static/bin"))
		

for i in range(len(images)):
	os.remove("tmp_{}.jpg".format(str(i).zfill(4)))
	os.remove("tmp_{}.mp4".format(str(i).zfill(4)))
