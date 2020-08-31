import json
import os

from flask import jsonify, Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def validation():
    review = request.get_json()
    print("Json Object \n")
    print(json.dumps(review, indent=4))
    labels = review['request']['object']['metadata']['labels']

    response = {}
    msg = None

    if 'imparator' not in list(labels):
        msg = "Every Pod requires imparator label"
        response["allowed"] = False
    else:
        response["allowed"] = True

    status = {
        "metadata": {},
        "message": msg
    }
    response["status"] = status
    review["response"] = response
    return jsonify(review), 200


if __name__ == '__main__':
    context = (
        os.environ.get("WEBHOOK_CERT", '/tls/tls.crt'),
        os.environ.get("WEBHOOK_KEY", '/tls/tls.key')
    )
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
