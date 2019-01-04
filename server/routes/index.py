'''
    The RESTful style api server
'''
from flask import render_template
from flask import Flask, request, redirect, jsonify, send_from_directory
from server import app
import os
import json

imagePath = 'D:/Vis/PCPVIs/labelTool/server/data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/images", methods=['GET'])
def get_image():
    imageList = []

    for root, dirs, files in os.walk(imagePath, topdown=False):
        print(root)
        for name in files:
            imageList.append(name)

    print(imageList)

    return jsonify(imageList)

@app.route("/api/image/<imageId>", methods=['GET'])
def getImage(imageId):
    return send_from_directory(imagePath, imageId)

@app.route("/api/saveResult", methods=['POST'])
def saveResult():
    data = request.json.get('rs')

    # save json
    with open('./server/result/label.json', 'w') as f:
        json.dump(data, f)

    # save a .txt for each image
    for i, val in enumerate(data):
        print(val)
        _id = val['imageId'].split('.')[0]
        filename = './server/result/' + _id + '.txt'
        with open(filename, 'w') as f:
            for pcpidx, pcp in enumerate(val['labels']):
                for j in range(int(pcp['axisNum']) - 1):
                    cwidth = pcp['width'] * 1.0 / (int(pcp['axisNum']) - 1)
                    cheight = pcp['height'] * 1.0
                    cx = pcp['x'] + (j * cwidth) + (cwidth * 0.5)
                    cy = pcp['y'] + (cheight * 0.5)
                    f.write('0 ' + str(cx/val['imageWidth']) + ' ' + str(cy/val['imageHeight']) + ' ' 
                        + str(cwidth/val['imageWidth']) + ' ' + str(cheight/val['imageHeight']) + '\n')

    return 'success'

