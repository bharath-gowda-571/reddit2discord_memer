
import praw
import urllib.request
from drive_main import uploadFile

folder_id="1lytmkGRIOCrJu2L-K1QtYoLMiW-fKZrd"

reddit=praw.Reddit(user_agent="u/BestBotEver07",
					client_id="iTOCEsn4WdxSqA",client_secret="qWR0vD-DoXBtMNnVtaWh0wtuud0",
					username="BestBotEver07",password="anything")

subreddit=reddit.subreddit("memes+meme+wholesomememes")

def get_hot_memes(): 
	
	lis_of_memes=[]
	for submission in subreddit.hot(limit=3):
		# print(submission.url)
		
		file_name=submission.url.split("/")[-1]

		if submission.url.endswith(".png"):
			# downloads the image
			urllib.request.urlretrieve(submission.url,file_name)
			# uploads it to google drive 
			# uploadFile(file_name,file_name,"image/png",folder_id)
			lis_of_memes.append((str(submission),submission.url,file_name))

		elif submission.url.endswith(".jpg"):
			urllib.request.urlretrieve(submission.url,file_name)
			# uploadFile(file_name,file_name,"image/jpeg",folder_id)
			lis_of_memes.append((str(submission),submission.url,file_name))

	return lis_of_memes

