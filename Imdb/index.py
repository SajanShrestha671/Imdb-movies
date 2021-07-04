'''
from flask import Flask, render_template
from flask import request
from bs4 import BeautifulSoup
#import urllib.request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
    number = request.form['inputNumber']
    getResponse = request.get('https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count='+ number)
    parsed_html= BeautifulSoup(getResponse.content,'html5lib')
    return render_template("result.html", parsed_html = parsed_html,  count= 1)
if __name__ == '__main__':
   app.run()


'''   
from flask import Flask, render_template
from flask import request
from bs4 import BeautifulSoup
import urllib.request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def result():
    number = request.form['inputNumber']
    url = "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+number
    webUrl = urllib.request.urlopen(url)
    data = webUrl.read()
    
    parsed_html = BeautifulSoup(data,"html.parser")
    return render_template("result.html", parsed_html = parsed_html, count=1)
    
if __name__ == "__main__":
    app.run()