import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/background_process_test')
def background_process_test():
    os.system('cp -RT /mnt/user/appdata/swag/www/grcwebdev /mnt/user/appdata/swag/www/grcweb')
    return("nothing")

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))