from flask import Flask, request, jsonify
import requests
import random
import string
import os

app = Flask(__name__)

@app.route("/getcode")
def generateCode():
    code = ""
    code1 = ""
    code2 = ""
    code3 = ""
    code4 = ""
    for _ in range(8):
        code1 = code1 + random.choice(string.ascii_letters + string.digits)
        code2 = code2 + random.choice(string.ascii_letters + string.digits)
        code3 = code3 + random.choice(string.ascii_letters + string.digits)
        code4 = code4 + random.choice(string.ascii_letters + string.digits)
        code = f"{code1}-{code2}-{code3}-{code4}"

    return jsonify({
        "code": f"{code}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
