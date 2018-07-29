7/27/2018
Email : mileshshah@gmail.com


Program name: MER (Multimodal Emotion Recognition) 

- This software prodives emotion recognition data from three modalities which are: facial expression recognition,
speech-text sentiment analysis, and audio feature extraction analysis

- The facial expression recognition was a pretrained module that takes an image of a user's face and analyses the face of the user 
to identify the user's current expression. The training accuracy achieved after training this module was 65.45%. This 
module was trained on a kaggle dataset for their facial expression recognition challenge.

- The speech-text sentiment analysis module takes an audio file that will consist of a user expressing an emotion 
through speech and will analyze what the user says to determine whether the user is conveying either a poositive 
or a negative sentiment. This module achieved a training accuracy of 82 %. 

- The audio feature extraction analysis module will analyze the user's tone in the audio file to determine the sentiment 
of the user. We did not get any information about the training accuracy, but we will provide the URL for the module.

- To run this program you will need to open a terminal annd execute the followin command:
"python mer.py <--image file--> <--audio file-->"

- This command will perform an emotion recognition analysis on an image of someone's face or an audio file of a voice recording
, the following commands can be executed as well with this program.

"python mer.py <--image file-->"
"python mer.py <--audio file-->"

To run this program you must install the following python packages:

- Keras 2.0
- Tensorflow
- Numpy
- json
- Pillow
- pydub
The facial expression recognition module and training datasets from the following URL was used for this software:
 https://github.com/jrishabh96/Facial-Expression-Recognition 
 https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data
The module that was used in this program for audio feature analysis used code from repository:
 https://github.com/vyassu/DeepSentiment
In this program wee also include a node.js file that can extract the emotion data from the 
python file am can save it in a string variable tht can be stored as a JSON object^
To run node.js file, the user will run command:
"node get-mer-data.js <--image file-->" or "node get-mer-data.js <--audio file-->"
or "node get-mer-data.js <--image file--> <--audio file-->"
