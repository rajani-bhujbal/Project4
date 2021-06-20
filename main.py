from flask import Flask

app4 = Flask(__name__)

@app4.route('/',methods=['Post','Get'])
def index():
    return" This is my second project"

if __name__ == "__main__":
    app4.run(debug=True)