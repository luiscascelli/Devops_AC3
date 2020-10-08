import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def nprimos():
    p = [1, 2]
    i = 3
    while len(p) < 100:
        primo = True
        for j in p[1:]:
            if i % j == 0:
                primo = False
                break
        if primo:
            p.append(i)
        i += 1
    listToStr = ' '.join(map(str, p))
    return listToStr


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
