Overview
======
I created a flask server in python that both serves webpages and handles the API call. It serves the html page and video page statically.
The API call takes one argument, a twitter screenname in the endpoint /api/getlabels.

Webpage
======
The webpage is a simple angular app. It takes a screenanme and created a video and labels it on the backend via an AJAX call. The labels are returned asynchonously to the page, but synchronously on the server. These are then displayed, and the video file is reloaded from the server and set to play.

Overall, it works okay.
