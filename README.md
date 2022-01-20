# Song-Generation-App
Generates lyrics with given constraints.

# [Go to the app :)](https://song-generation.herokuapp.com/)
**may take few minutes to load**

<img src = "https://github.com/shanmukh05/Song-Generation-WebApp/blob/main/static/images/demo.png" width="600" height = "350">

# Details of Files present in Repository
- #### dataset
    - The datset folder consists of .txt files which contains lyrics of some of the singers.\
    - The fromat of the txt file is <br> 
     -Song Name-\
     Lyrics\
    -Song Name-\
     Lyrics
    - Dataset is uploaded on kaggle : [Song Generation](https://www.kaggle.com/shanmukh05/songgeneration)
    - All the data is collected manually from web.
- #### files
    - vocab_text.csv
       - contains vocabulary extracted from songs.
    - vocab_line.csv
       - contains unique count of words in line of song.
    - generate_lines.h5
       - model to generate list of number of words per line in a song.
    - generate_text.csv.h5 (Due to memory constraint, I didn't upload this file. You can get this file here from my [Kaggle Notebook](https://www.kaggle.com/shanmukh05/song-generation-with-rnn/output))
 - #### static
    - all CSS,JS files are present here in their respective folders.
 - #### templates
    - HTML files are present.
 - app.py : python file
 - Procfile : needed for Heroku to know what commands it need to run.
 - requirements.txt : to specify the libraries needed to install to Heroku.
 - runtime.txt : to specify specific version of python.


# Details of Project

**Song Generator** is web-app deployed on Heroku.

- ## Model Training
   - First the lyrics file(.txt) is preprocessed to get required inputs (No of songs,song as list,No of words....) 
   - NLTK wordnetlemmatizer is also used in preprocessing. To know more about NLTK toolkit visit [NLTK](https://www.nltk.org/).
   - In the first model the preprocessed data is taken and given to model which gives a continuous words present in the required song as output. 
   - The same preprocessed data is taken and given to second model which gives a list of "Number of words" present in a line as output. 
   - Finally the outputs of the 2 models is taken and the final song is produced as per the given length and lines of song. 
   - I used the Tensorflow(2.3.0) ML library to do this task.To know more about TensorFlow library visit [TensorFlow](https://www.tensorflow.org/). 
   - Output lyrics are obtained by giving a starting word in first model and starting number of word per line in second model.
   - More details are in my [kaggle notebook](https://www.kaggle.com/shanmukh05/song-generation-with-rnn/)

- ## Frontend
     - used an online template and made changes to **HTML**,**CSS**,**JS** files.

 - ## Deployment
     - You can go through this YT playlist created by me for reference [Deploying ML model on Heroku using Flask](https://www.youtube.com/playlist?list=PL9NRL49Dq8llKW_QW510V-MgIGWhvZoOX).
     - For more details visit [Heroku](https://www.heroku.com/).

# Things I couldn't do because of memory constraint 😢(500MB)
- Using better pretrained models to get good results.
