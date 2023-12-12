from pytube import YouTube
import scrapetube
from pymongo import MongoClient
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
from youtube_transcript_api import YouTubeTranscriptApi
import langid
import youtube_transcript_api 





client = MongoClient('localhost', 27017)
db = client['cardbase'] 
videodb = client['videos']
urldbb = client['urls']
urlcollection = urldbb['url']
videocollection = db['videos']
collection = db['cards']
laymancollection = db['layman']
laymanurldb = urldbb['laymanurl']

VIDEO_LIMIT_IN_SECONDS = 400



channel = scrapetube.get_channel("UCbwFrxI0u_5vi9wwD_Ni97g")


ctr_all_iterated = 0
ctr_is_valid_added = 0
for video in channel:
    url = "https://www.youtube.com/watch?v="+str(video['videoId'])
    embed = "https://www.youtube.com/embed/"+str(video['videoId'])
    session = HTMLSession()                                                                             
    yt = YouTube(url)
    length = yt.length
    resp = session.get(url)
    soup = bs(resp.html.html, "html.parser")
    title = soup.find("meta", itemprop="name")['content']
    title_lang = langid.classify(title)[0]

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video['videoId'])
        isValid = None
        for currtranscript in transcript_list:
            
            if currtranscript.is_generated==False and currtranscript.language_code=="en" and title_lang=="en" and ("😂" not in title):
                    isValid = True
                    break;
    except youtube_transcript_api._errors.TranscriptsDisabled: 
            pass
   
    if (length<=VIDEO_LIMIT_IN_SECONDS and length>=30) and isValid==True:
        ctr_is_valid_added+=1
        url_data = {
        'url': url,
        'embed':embed,
        'title':title,
        'cardID':ctr_is_valid_added
        }
        laymanurldb.insert_one(url_data)

    ctr_all_iterated+=1

print("THIS IS ALL VALID ADDED, OTHER IS NOT: " + str(ctr_is_valid_added))

print(ctr_all_iterated)


# CODE TO UPDATE/ADD FIELDS TO PREXISTING DATA IN DATABASE
# urls = urlcollection.find()
# for oneurl in urls:
#     currurl = oneurl['url']                           
#     vidID = currurl[32:len(currurl)]
#     embed = "https://www.youtube.com/embed/" + vidID
#     filter = { 'url' : currurl }
#     urlembed = { "$set" : { 'embedurl': embed } }
#     urlcollection.update_one(filter,urlembed)
    

    