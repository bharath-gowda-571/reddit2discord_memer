
import praw
import urllib.request
from drive_main import uploadFile

folder_id="1Bg-vx6On6tNudf8hi_DLXLQtrXmV96UT"

reddit=praw.Reddit(user_agent="u/BestBotEver07",
					client_id="iTOCEsn4WdxSqA",client_secret="qWR0vD-DoXBtMNnVtaWh0wtuud0",
					username="BestBotEver07",password="anything")

subreddit=reddit.subreddit("memes+meme+wholesomememes")
for submission in subreddit.hot(limit=10):
	# print(submission.url)
	file_name=submission.url.split("/")[-1]
	if submission.url.endswith(".png"):
		urllib.request.urlretrieve(submission.url,file_name)
		uploadFile(file_name,file_name,"image/png",folder_id)
	elif submission.url.endswith(".jpg"):
		urllib.request.urlretrieve(submission.url,file_name)
		uploadFile(file_name,file_name,"image/jpeg",folder_id)

