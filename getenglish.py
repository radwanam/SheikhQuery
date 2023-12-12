from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import translators as ts
import re
import json as json
import whisper
import pandas as pd
import os
import openai
import translators
import youtube_transcript_api

openai.api_key = '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'
bad_words = ("Sheikh Assim Al Hakeem","assim alhakeem","assim al hakeem", "- assim al hakeem","-assim al hakeem","Assim al hakeem","- Assim al hakeem", "assim", "- assim","-assim", "Assim","JAL")
bad_chars = ("\ ","/",":","*","?","<", ">" ,"|","-")

class FatwaCard:
  def __init__(self,url,uncleanedtitle):
      self.url = url
      self.title = None
      self.filename=None
      self.transcript_text = None
      self.video_summary = None
      self.betastatus = False
      self.id = 0
      self.author = "Assim Al Hakeem"
      self.uncleanedtitle= uncleanedtitle
      self.isQuestion = False
    
  def set_title_and_filename(self):
    #   code to get title from web
    #   session = HTMLSession()
    #   resp = session.get(self.url)
    #   soup = bs(resp.html.html, "html.parser")
    #   uncleanedtitle = soup.find("meta", itemprop="name")['content']

      title = self.cleaup_title(self.uncleanedtitle)          
      self.filename = f"{title}.mp4"
      if "?" in self.uncleanedtitle:
          title+="?"
          self.isQuestion = True
          
      self.title = title

  def set_transcript(self):

    try:
      srt = YouTubeTranscriptApi.list_transcripts(self.url[32:len(self.url)])
      srt = srt.find_manually_created_transcript(['en'])

      for script in srt:
            if(script.is_generated==False):
                srt = script.find_manually_created_transcript(['en']).fetch()

      transcript_text = ""
      for line in srt:
                transcript_text+=line['text']
      self.transcript_text = transcript_text
    except youtube_transcript_api._errors.TranscriptsDisabled:
        try:    
          audio_file = YouTube(self.url).streams.filter(only_audio=True).first().download(filename=self.filename)
          model = whisper.load_model("tiny")
          result = model.transcribe(self.filename, language="en", fp16=False, verbose=True)
          transcript_text = result["text"]
          self.transcript_text = transcript_text
          self.remove_video_from_server()
          self.betastatus = True
        except:
            self.transcript_text = "Error"
            self.betastatus = False

  def cleaup_title(self,title): 
      for charbad in bad_chars:
          for chartest in title:
              title = title.replace(charbad,"")

      for bad_word in bad_words:
        if bad_word in title:
              title = title.replace(bad_word, "")
              break;
      if "JAL" in title:
          title = title.replace("JAL","")

      title = title.rstrip()
      return title

#   def set_summary(self):
#       completion = openai.ChatCompletion.create(
#           model="gpt-3.5-turbo",
#           messages=[
#               {"role": "user", "content": f"create a summarization of this text, do it without commenting on the text. write the text as if the summarized version is the text itself: {self.transcript_text}. FYI: the title of this video is {self.filename}, do NOT include the filename in the summary, it is just for you. Please do not make up your own words, only restating from the article. This summary is for the end-user, do not make it shabby"}
#           ]
#       )

#       video_summary = completion.choices[0].message.content
#       self.video_summary = video_summary
#       # with open(f'{title}.txt', 'w') as f:
#       #     f.write(transcript_text)

#       return video_summary
  
  def remove_video_from_server(self):
      os.remove(self.filename)

  def set_cardID(self,ID):
      self.id = ID
  def get_title_and_filename(self):
      return self.title,self.filename
  def get_transcript(self):
      return self.transcript_text
  def get_summary(self):
      return self.video_summary
  def get_betastatus(self):
      return self.betastatus
  def get_cardID(self):
      return self.id