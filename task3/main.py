from flask import Flask, request
from math import gcd

app = Flask(__name__)

def lcm(x, y):
    return x * y // gcd(x, y)

@app.route("/izbagambetov_dias_gmail_com")
def lcm_endpoint():
    try:
        x = request.args.get("x", "")
        y = request.args.get("y", "")

        if not x.isdigit() or not y.isdigit():
            return "NaN", 200, {"Content-Type": "text/plain"}

        x = int(x)
        y = int(y)

        result = lcm(x, y) if (x != 0 and y != 0) else 0
        return str(result), 200, {"Content-Type": "text/plain"}

    except Exception:
        return "NaN", 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)