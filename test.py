from math import sqrt
from pytube import YouTube
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
from youtube_transcript_api import YouTubeTranscriptApi
import json as json
import os
import translators as ts
import scrapetube

# url = "https://www.youtube.com/watch?v=-_JzRklw9j8&ab_channel=assimalhakeem"

# transcript = ""

# try:
#         srt = YouTubeTranscriptApi.list_transcripts(url[32:len(url)])

#         for script in srt:
#                 srt = script.translate('ja').fetch()

#         for line in srt:
#                 transcript+=line['text']

# except:
#         transcript = "エラー"
#         pass

# 
# # print(transcript)
# bad_words = ("assim al hakeem", "- assim al hakeem","-assim al hakeem","Assim al hakeem","- Assim al hakeem", "assim", "- assim","-assim", "Assim")
# title = "What are the halal jobs a woman can work in, in Islam? - Assim al hakeem"
# bad_chars = ("\ ","/",":","*","?","<", ">" ,"|","-")

# for charbad in bad_chars:
#         for chartest in title:
#             title = title.replace(charbad," ")
# found_bad_word = next((word for word in bad_words if word in title), None)

# for bad_word in bad_words:
#       if bad_word in title:
#             print(bad_word)
#             title = title.replace(bad_word, "")
#             break;

# title = title.rstrip()
# title+="?"
# print(title)
# filename = f"{title}.mp4"

# # -*- coding: utf-8 -*-
# from pytube import YouTube

# vid = "https://youtu.be/Ak4KxwQ9yDc"

# yt = YouTube(vid)
# print(yt.length)

# audio_file = YouTube(url).streams.filter(only_audio=True).firsfilename)


# test = "Can men use rose gold items like pen, keychains etc\ - assim al hakeem"

# bad_chars = ("\ ","/",":","*","?","<", ">" ,"|")

# for charbad in bad_chars:
#     for charstest in test:
#         test = test.replace(charbad," ")t().download(filename=
# print(test)


# try:
#     print(3/0)
# except ZeroDivisionError:
#         try:
#                 print(sqrt(-2))
#         except:
#                 print("ok")


# channel = scrapetube.get_channel("UCbwFrxI0u_5vi9wwD_Ni97g")

# ctr = 0
# ctr_for_manual = 0
# for video in channel:
#         tslist = YouTubeTranscriptApi.list_transcripts(video['videoId'])
#         ctr+=1
#         for transcript in tslist:
#                 try:
#                         test = transcript.is_generated
#                         if test == False:
#                                 ctr_for_manual+=1
#                                 print(video['videoId'],transcript.language_inde)
#                 except:
#                         print("failed")
#                         pass
#         print(str(ctr) + " " + str(ctr_for_manual))

srt = YouTubeTranscriptApi.list_transcripts("Euv70pmSROE")

for script in srt:
        if(script.is_generated==False):
                srt = script.translate('en').fetch()

transcript_text = ""
for line in srt:
        transcript_text+=line['text']
print(transcript_text)