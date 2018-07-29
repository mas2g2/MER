from cnn_major import predict_emotion
from keras.preprocessing import image as img
import sys,json,os
import numpy as np
from PIL import Image
from sentiment_analysis import append_audio
sys.path.insert(0,"DeepSentiment/Code/StandAlone")
from Controller import main
from pydub import AudioSegment
import re
try:
    image = sys.argv[1]
    image = img.load_img(image,target_size=(48,48))
    image = img.img_to_array(image)
    image = np.expand_dims(image,axis=0)
    prediction = predict_emotion(image) 
    # do stuff
    image_data = ' "image_file" : "'+sys.argv[1]+'", "facial_expression" : "'+str(prediction)+'"'
      
    try:
        audio_file = sys.argv[2]
        if audio_file.endswith(".wav") == False:
            print("Not a wav file")
            file_split = os.path.splitext(audio_file)
            file_extension = file_split[1] 
            file_format = file_extension[1:]
            print(audio_file)
            raw_file = AudioSegment.from_file(audio_file,format=file_format)
            raw_file.export(file_split[0]+".wav",format="wav")
            wav_file = file_split[0] + ".wav"
	    audio_file = wav_file
        else:
            print("This is a wav file")
        audio = []
        audio.append(audio_file)
        sentiment = []
        sentiment = append_audio(audio_file)
        sentiment_analysis = ""

        if sentiment[0] == 'pos':
            sentiment_analysis = 'positive'
        else:
            sentiment_analysis = 'negative'
        audio_feature_sentiment = main(audio_file,False)
        #print(audio_feature_sentiment)
        afs = str(audio_feature_sentiment)

        afs = re.findall(r'{(.*?):',afs)
        afs = str(afs[0])
        afs = afs.replace("'",'"')
        #afs = afs.replace('u"','"')
        print(afs)
        audio_data = ' "audio_file" : '+'"'+sys.argv[2]+'", "sentiment" : "'+str(sentiment_analysis)+'", "audio_feature_analysis" : '+afs+', '
    except IndexError:
        print("No audio file")
        audio_data = ""
except IOError:
    try:
        image_data = " "
        audio_file = sys.argv[1]
        if audio_file.endswith(".wav") == False:
            print("Not a wav file")
            file_split = os.path.splitext(audio_file)
            file_extension = file_split[1]
            file_format = file_extension[1:]
            print(audio_file)
            raw_file = AudioSegment.from_file(audio_file,format=file_format)
            raw_file.export(file_split[0]+".wav",format="wav")
            wav_file = file_split[0] + ".wav"
            print(wav_file)
            audio_file = wav_file
        else:
            print("This is a wav file")
        audio = []
        audio.append(audio_file)
        sentiment = []
        sentiment = append_audio(audio_file)
        sentiment_analysis = ""


        if sentiment[0] == 'pos':
            sentiment_analysis = 'positive'
        else:
            sentiment_analysis = 'negative'
        audio_feature_sentiment = main(audio_file,False)
        #print(audio_feature_sentiment)
        afs = str(audio_feature_sentiment)
        afs = re.findall(r'{(.*?):',afs)
        afs = str(afs[0])
        afs = afs.replace("'",'"')
        audio_data = ' "audio_file" : '+'"'+sys.argv[1]+'", "sentiment" : "'+str(sentiment_analysis)+'", "audio_feature_analysis" : '+afs+' '
    except:
        print("IOError: Invalid file, file must be audio file or image file")
        audio_data = " "
result = '{ '+audio_data+image_data+' }'
print("Result: "+result)
