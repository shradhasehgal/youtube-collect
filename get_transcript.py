from youtube_transcript_api import YouTubeTranscriptApi

try:
    transcript = YouTubeTranscriptApi.get_transcript('OKe7q1nUFgE', languages=['en', 'hi'])
    print(transcript)

except:
    print("Error in retrieving transcript")