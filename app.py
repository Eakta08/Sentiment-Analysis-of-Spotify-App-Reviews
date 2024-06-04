from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import Flask, render_template, request
from afinn import Afinn

app=Flask(__name__)
    
def senti_pred(sen):
    afinn = Afinn(emoticons=True, language = 'en')
    senti_score=afinn.score(sen)
    if senti_score>0:
        return f'POSITIVE'
    elif senti_score<0:
        return f'NEGATIVE'
    else:
        return f'NEUTRAL'
    
@app.route('/',methods=['GET','POST'])

def index():
  sentiment=None
  if request.method=='POST':
    user_input=str(request.form['user_input'])
    sentiment=senti_pred(user_input)
  return render_template('index.html',sentiment=sentiment)

if __name__=='__main__':
  app.run(debug=True)