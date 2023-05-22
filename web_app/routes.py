from web_app import app
from flask import render_template, request, jsonify
from ANS.ANS_rescaling import ans_encoder_rescaling,ans_decoder_rescaling
from ANS.ANS_no_rescaling import ans_decoder_no_rescaling, ans_encoder_no_rescaling
from ANS.tANS import tans_decode, tans_encode
from ANS.uANS import uans_decode, uans_encode

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/uans/encode', methods=["POST"])
def uANS_encode():
    input_data = request.get_json()['input']
    encoded_output = uans_encode(input_data)
    return jsonify(output=str(encoded_output))

@app.route('/uans/decode', methods=["POST"])
def uANS_decode():
    input_data = request.get_json()['input']
    decoded_output = uans_decode(input_data)
    return jsonify(output=str(decoded_output))

@app.route('/ransws/encode', methods=["POST"])
def rANSws_encode():
    input_data = request.get_json()['input']
    encoded_output = ans_encoder_rescaling(input_data)
    return jsonify(output=str(encoded_output))

@app.route('/ransws/decode', methods=["POST"])
def rANSws_decode():
    input_data = request.get_json()['input']
    decoded_output = ans_decoder_rescaling(input_data)
    return jsonify(output=str(decoded_output))

@app.route('/ranswos/encode', methods=["POST"])
def rANSwos_encode():
    input_data = request.get_json()['input']
    encoded_output = ans_encoder_no_rescaling(input_data)
    return jsonify(output=str(encoded_output))

@app.route('/ranswos/decode', methods=["POST"])
def rANSwos_decode():
    input_data = request.get_json()['input']
    decoded_output = ans_decoder_no_rescaling(input_data)
    return jsonify(output=str(decoded_output))

@app.route('/tans/encode', methods=["POST"])
def tANS_encode():
    input_data = request.get_json()['input']
    encoded_output = tans_encode(input_data)
    return jsonify(output=str(encoded_output))

@app.route('/tans/decode', methods=["POST"])
def tANS_decode():
    input_data = request.get_json()['input']
    decoded_output = tans_decode(input_data)
    return jsonify(output=str(decoded_output))


