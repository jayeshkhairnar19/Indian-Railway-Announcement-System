import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS




def textToSpeech(text, filename):
    mytext = str(text)
    myobj = gTTS(text=mytext, lang='hi', slow=True)
    myobj.save(filename)
    
def texttoSpeech(text, filename):
    mytext = str(text)
    myobj = gTTS(text=mytext, lang='en', slow=True)
    myobj.save(filename)    

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate kripya dhyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

    # 12 - Generate May I have your attention please train no
    start = 19000
    finish = 23600
    audioProcessed = audio[start:finish]
    audioProcessed.export("12_en.mp3", format="mp3")

    # 13 is train no and name

    # 14 - Generate from
    start = 30500
    finish = 31200
    audioProcessed = audio[start:finish]
    audioProcessed.export("14_en.mp3", format="mp3")

    # 15 is from-city

    # 16 - Generate to
    start = 31500
    finish = 32800
    audioProcessed = audio[start:finish]
    audioProcessed.export("16_en.mp3", format="mp3")

    # 17 is to-city

    # 18 - Generate via
    start = 33500
    finish = 34600
    audioProcessed = audio[start:finish]
    audioProcessed.export("18_en.mp3", format="mp3")

    # 19 is via-city

    # 20 - Generate is arriving shortly on platform no
    start = 36300
    finish = 40600
    audioProcessed = audio[start:finish]
    audioProcessed.export("20_en.mp3", format="mp3")

    # 21 is platform number

    # 22 - Generate music
    start = 41000
    finish = 42000
    audioProcessed = audio[start:finish]
    audioProcessed.export("22_en.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6 - Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        # 13 is train no and name
        texttoSpeech(item['train_no'] + " " + item['train_name'], '13_en.mp3')

        # 15 is from-city
        texttoSpeech(item['from'], '15_en.mp3')

        # 17 is to-city
        texttoSpeech(item['to'], '17_en.mp3')

        # 19 is via-city
        texttoSpeech(item['via'], '19_en.mp3')

        # 21 is platform number
        texttoSpeech(item['platform'], '21_en.mp3')

        
        audios = [f"{i}_hindi.mp3" for i in range(1,12)] + [f"{i}_en.mp3" for i in range(12,23)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
    

