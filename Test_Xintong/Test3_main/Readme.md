## Test3

Test final work

replace:
> subprocess.call(('''ffmpeg -loop 1 -i tmp_{}.jpg -c:a libfdk_aac -ar 44100 -ac 2 -vf "scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)',                                  pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -b:v 10M -pix_fmt yuv420p -r 30 -shortest -avoid_negative_ts make_zero -fflags +genpts -t 1 tmp_{}.mp4''').format(str(i).zfill(4) , str(i).zfill(4)),
			 	cwd=os.path.dirname(os.path.realpath(__file__)), shell=True, env=dict(os.environ, PATH="/Users/yt.hao/Desktop/BU/Study/EC500C1/CodeReview/EC500-master/Test_Xintong/Test2_urls_to_movie/ffmpeg-3.4.2"))

by 

> os.system(('''ffmpeg -loop 1 -i tmp_{}.jpg -c:a libfdk_aac -ar 44100 -ac 2 -vf "scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)', pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -b:v 10M -pix_fmt yuv420p -r 30 -shortest -avoid_negative_ts make_zero -fflags +genpts -t 1 tmp_{}.mp4''').format(str(i).zfill(4) , str(i).zfill(4)))


- [x] Get all the images and convert into vedio
- [x] Concatenate all the videos together and make a output.mp4
- [x] Remove all the template files

  <img src="https://github.com/Johnidel/EC500/blob/CodeReview/Test_Xintong/Test3_main/WX20180221-155304.png" />
  
- [x] Print all the labels of images in the video, with detaied categories.
- [x] Error handle

  <img src="https://github.com/Johnidel/EC500/blob/CodeReview/Test_Xintong/Test3_main/WX20180221-155351.png" />

### Strength
- Unique structure and elegant codes
- High efficiency by usingn multiple tools
- Detailed explanations and notations (Really appreciate for that)


### Suggestion
- [ ] ffmpeg issue
- [ ] Split the labels in different lines to make them more readable
- [ ] Try to write the labels into videos
