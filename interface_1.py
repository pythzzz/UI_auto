from flask import Flask
app=Flask(__name__)
@app.route("/test/")
def aaatest():
    return "hello world123"

if __name__=='__main__':
    app.run(host='127.0.0.1',port=8082)