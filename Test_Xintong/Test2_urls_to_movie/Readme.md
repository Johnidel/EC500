## Test2

Test function urls_to_movie

replace:
> subprocess.call(('''ffmpeg -loop 1 -i tmp_{}.jpg -c:a libfdk_aac -ar 44100 -ac 2 -vf "scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)',                                  pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -b:v 10M -pix_fmt yuv420p -r 30 -shortest -avoid_negative_ts make_zero -fflags +genpts -t 1 tmp_{}.mp4''').format(str(i).zfill(4) , str(i).zfill(4)),
			 	cwd=os.path.dirname(os.path.realpath(__file__)), shell=True, env=dict(os.environ, PATH="/Users/yt.hao/Desktop/BU/Study/EC500C1/CodeReview/EC500-master/Test_Xintong/Test2_urls_to_movie/ffmpeg-3.4.2"))

by 

> os.system(('''ffmpeg -loop 1 -i tmp_{}.jpg -c:a libfdk_aac -ar 44100 -ac 2 -vf "scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)', pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -b:v 10M -pix_fmt yuv420p -r 30 -shortest -avoid_negative_ts make_zero -fflags +genpts -t 1 tmp_{}.mp4''').format(str(i).zfill(4) , str(i).zfill(4)))


- [x] After this change, it could convert all the images into video
- [x] Get a txt file of list of videos
- [x] Concatenate all the videos together and make a output.mp4
- [x] Error handle

  <img src="https://github.com/Johnidel/EC500/blob/CodeReview/Test_Xintong/Test2_urls_to_movie/WX20180221-152707.png" />
