# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:23:46 2021

@author: shanmukh
"""
from __future__ import division, print_function
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from flask import Flask,render_template,request


filepath = os.path.join(os.getcwd(),"files")
vocab_text = list(pd.read_csv(os.path.join(filepath,"vocab_text.csv"))["vocab"])
char2idx_text = {u:i for i,u in enumerate(vocab_text)}
idx2char_text = np.array(list(vocab_text))

vocab_line = list(pd.read_csv(os.path.join(filepath,"vocab_line.csv"))["vocab"])
char2idx_line = {u:i for i,u in enumerate(vocab_line)}
idx2char_line = np.array(list(vocab_line))

text_model = tf.keras.models.load_model(os.path.join(filepath,"generate_text.h5"))
line_model = tf.keras.models.load_model(os.path.join(filepath,"generate_lines.h5"))

def generate_text(model, start_string,words_count):
    num_generate = words_count
    try:
        input_eval = char2idx_text[start_string.lower()]
    except:
        input_eval = 0
    input_eval = tf.expand_dims(input_eval, 0)
    text_generated = []
    temperature = 1.0
    model.reset_states()
    for i in range(num_generate):
        predictions = model.predict(input_eval)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char_text[predicted_id])
    return (start_string +" "+ ' '.join(text_generated))



def generate_lines(model, first_line,lines_count):
    num_generate = lines_count
    try:
        input_eval = char2idx_line[first_line]
    except:
        input_eval = 5
    input_eval = tf.expand_dims(input_eval, 0)
    lines_generated = []
    lines_generated.append(first_line)
    temperature = 1.0
    model.reset_states()
    for i in range(num_generate):
        predictions = model.predict(input_eval)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
        input_eval = tf.expand_dims([predicted_id], 0)
        lines_generated.append(idx2char_line[np.array(input_eval)[0][0]])
    return lines_generated

def create_song(name,wordcount,firstline,linecount):
    song_raw = generate_text(text_model,name,wordcount)
    words_per_line = generate_lines(line_model,firstline,linecount)
    lines = [int(i) for i in words_per_line]
    song_words = song_raw.split(" ")
    count=0
    final_song = ""
    for i in lines:
        for j in range(i):
            count+=1
            if count> len(song_words):
                break
            final_song = final_song+ " "
            final_song= final_song+ song_words[count-1]
        final_song+="\n"
    
    return final_song
    
app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      startword = request.form["name"]
      wordcount = int(request.form["wordcount"])
      linecount = int(request.form["linecount"])
      firstline = int(request.form["firstline"])
      final_song = ""
      final_song += f"You entered: \n \tstart word: {startword} \n \tNumber of words: {wordcount} \n \tNumber of lines: {linecount} \n \tNumber of words in first line: {firstline} \n"
      final_song += "\n ---------------------------FINAL SONG---------------------------  \n\n"
      final_song += create_song(startword,wordcount,firstline,linecount)
      return render_template("index.html",final_song = final_song,)
   else:
      return render_template("index.html",final_song = "Give proper input to see the magic song")


if __name__ == '__main__':
   app.run(debug = True)
    
    
    
    
    
    
    
    
    
    