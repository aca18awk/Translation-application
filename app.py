
from flask import Flask, render_template,request
import os

app = Flask(__name__)

@app.route("/")
def say_hello():
    language=["Azerbaijan","Malayalam","Albanian","Maltese","Amharic","Macedonian","Arabic","Marathi","Armenian",
    "Mongolian","German","Polish","Spanish","Chinese","French","Scottish","Korean","Esperanto","Sundanese","Persian"]
    background=["#9932CC","black","#00CED1","#9932CC","#B22222","#696969","#4B0082","#20B2AA","#800000","#800080",
                "#C71585","#FF4500","#DA70D6","#BC8F8F","#4682B4","#9ACD32","#4682B4","#708090","#DB7093","#6B8E23"]
    font=["#48D1CC","#FFC0CB","#FFDEAD","#FAF0E6","#FFA07A","#FFB6C1","#FAFAD2","#FFFACD","#FFF0F5","#F0E68C",
            "#F0FFF0","#ADFF2F","#FFD700","#FF00FF","#00CED1","#E9967A","#BDB76B","#00FFFF","#7FFF00","#7FFFD4"]
    return render_template("hello.html",language=language,font=font,background=background,x=0)

if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)
