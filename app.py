from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return str(s)

s=11

def main():
    s=10
    return None


if __name__ == '__main__':
    main()
