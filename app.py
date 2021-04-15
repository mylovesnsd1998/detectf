from flask import json
import base64
from flask import request, send_from_directory
from label_image import callapi
from flask import Flask, redirect, url_for
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import send_file
import os
# db.create_all()  # enable to create db
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
UPLOAD_FOLDER = '/tensorflow-for-poets-2/UPLOAD_FOLDER'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# api controller register account
from werkzeug.utils import secure_filename
@app.route('/api/classifi', methods=["POST"])
def custom_data():
    content = request.json
    name = content["name"]
    resp = {
        "name": "",
        "link": "",
        "code": 200
    }
    minh = callapi(name)
    resp["name"] = minh


    return app.response_class(response=json.dumps(resp),mimetype='application/json')

@cross_origin()
@app.route('/api/hello')
def downloadFile2():
    resp = {
        "name": "hello world",
        "code": 200
    }
    
    return app.response_class(response=json.dumps(resp),mimetype='application/json')

@cross_origin()
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    resp = {
        "name": "hello",
        "predict": "null",
        "code": 200
    }
    minh = True
    if minh is True:
        # resp["name"]= "Hello 4"
        # check if the post request has the file part
        if 'file' not in request.files:
            # resp["name"]= "Hello 3"
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            resp["name"]= "Hello 1"
            return redirect(request.url) 
        if file:
            resp["name"]= "Success"
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.close()
            minh = callapi(filename)
            resp["predict"] = minh
    return app.response_class(response=json.dumps(resp),mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=8000, threaded=True)
