from flask import Flask 
app = Flask(__name__)

@app.route('/hello',methods = ['GET'])
def hello_world():
    print(1)
    return "Hello World"

@app.route('/sumanth',methods=['GET','POST'])
def printing_message():
    return "hey how are you"

if __name__=='__main__':
    app.run(debug=True)