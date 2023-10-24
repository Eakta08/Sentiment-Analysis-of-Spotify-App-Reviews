from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import Flask, render_template, request

app=Flask(__name__)

def senti_pred(sen):
    sentiments = SentimentIntensityAnalyzer()
    d=sentiments.polarity_scores(sen)
    del d['compound']
    if max(d, key=lambda key: d[key])=='pos':
        return 'POSITIVE'
    elif max(d, key=lambda key: d[key])=='neg':
        return 'NEGATIVE'
    else:
        return 'NEUTRAL'
    
@app.route('/',methods=['GET','POST'])

def index():
  sentiment=None
  if request.method=='POST':
    user_input=str(request.form['user_input'])
    sentiment=senti_pred(user_input)

  return render_template('index.html',sentiment=sentiment)

if __name__=='__main__':
  app.run(debug=True)