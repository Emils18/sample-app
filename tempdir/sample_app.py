from flask import Flask, request

sample = Flask(__name__)

@sample.route("/")
def main():
    return f"<h1>You are calling me from {request.remote_addr}</h1>"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, threaded=False, processes=1)