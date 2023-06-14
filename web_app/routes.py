from web_app import app, cache
from flask import render_template, request, jsonify
from ANS.rANS import rans_decoder, rans_encoder
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


@app.route('/rans/encode', methods=["POST"])
def rANSwos_encode():
    input_data = request.get_json()['input']
    encoded_output = rans_encoder(input_data)
    return jsonify(output=str(encoded_output))


@app.route('/rans/decode', methods=["POST"])
def rANSwos_decode():
    input_data = request.get_json()['input']
    decoded_output = rans_decoder(input_data)
    return jsonify(output=str(decoded_output))


@app.route('/tans/encode', methods=["POST"])
def tANS_encode():
    input_data = request.get_json()['input']
    encoded_output, symbol_occurrences = tans_encode(input_data)
    cache.set('symbols', symbol_occurrences)
    return jsonify(output=str(encoded_output))


@app.route('/tans/decode', methods=["POST"])
def tANS_decode():
    input_data = request.get_json()['input']
    decoded_output = tans_decode(input_data, cache.get('symbols'))
    return jsonify(output=str(decoded_output))
