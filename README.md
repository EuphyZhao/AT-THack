Cloud-Proj1
===========
cloud first project

AWS account:
Username: yz2605@columbia.edu
pin: 19910816



[Jinja2]
http://jinja.pocoo.org/docs/

[Flask]
http://flask.pocoo.org/docs/quickstart/

[CloudFront]
http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html

[CloudFront - web Distributions]


[CloudFront - RTMP Distributions]
used for video streams
attention:
******
When an end user streams your media file, the media player begins to play the content of the file while the file is still being downloaded from CloudFront. The media file is not stored locally on the end user's system.
******

********
bug -- solved : upload html file to webserver, JWPlayer's security requirement
********
videos can't be played if html file is stored at local enviroment.
RTMP distributions & JWplayer requires that the html file is stored on aws s3/cloudfront

[RDS]
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html

AWS_RDS Connection info
Hostname: cloud-rds-cxhzyf.cxhauxbpbcmb.us-east-1.rds.amazonaws.com
Port: 3306
Username: ebroot
Password: ZHAOyufei816

mysql -h cloud-rds-cxhzyf.cxhauxbpbcmb.us-east-1.rds.amazonaws.com -P 3306 -u ebroot -p

[RDS - API]
http://docs.pythonboto.org/en/latest/rds_tut.html

[Flask-SQLAlchemy]
https://pythonhosted.org/Flask-SQLAlchemy/quickstart.html#quickstart

[Upload file to server]
http://runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python

[JM Player Account]
username: yfzhao123@gmail.com
pw: 19910816

JW Player Tools
[Cloud-Hosted Player Code]
<script src="http://jwpsrv.com/library/yTXcPKOlEeO34yIACrqE1A.js"></script>

[Self-Hosted Player License Key]
8uUBzbKU8nI0kurJ78lnqKCMAVeyJRJgU+/DOw==

To embed JW player to website
	<!-- For cloud-host JW Player-->
	<script src="http://jwpsrv.com/library/yTXcPKOlEeO34yIACrqE1A.js"></script>
	<!-- For self-hosted JW Player -->
	<script type="text/javascript" src="{{url_for('static', filename='jwplayer.js')}}"></script>
	<script type="text/javascript">jwplayer.key="GEf1CHwM8wS4qcxBlIIssJWje9iCn+3fzsfugA==";</script>

[Elastic Beanstalk]
$ export PATH=$PATH:<path to unzipped EB CLI package>/eb/linux/python2.7/

[JW Player bug - support for mobile browser]
bug info:	unable to play video on mobile browser using RTMP distribution
solution:	use web distribution instead, add url of web distribution to playlist
relevant info:
http://www.longtailvideo.com/support/forums/jw-player/setup-issues-and-embedding/33351/error-loading-player-no-playable-sources-found/

available url for mobile browser:
{file: "http://d2uztetpwnry1z.cloudfront.net/VIDEO_NAME"}

[RTMP file format limit]
RTMP supports video in MP4 and FLV and audio in AAC and MP3. 
JWPlayer only support mp4

[EB deply bug]
ERROR	Your WSGIPath refers to a file that does not exist.
need to configure environment for EB
refer:
http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers.html


[Facebook login]
install Flask-Social: pip install Flask-Social
install facebook sdk: pip install http://github.com/pythonforfacebook/facebook-sdk/tarball/master