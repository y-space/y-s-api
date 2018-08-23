
from flask import Flask, jsonify
from flask_cors import CORS

import json
from random import sample

app = Flask(__name__)
CORS(app)

with open('y-s-datasets/exoplanets/exoplanets.json') as f:
    exoplanets = json.load(f)

with open('y-s-datasets/messier/messier.json') as f:
    messier = json.load(f)

@app.route('/exoplanets', methods=['GET'])
def get_exoplanets():
    return jsonify({
        'name': 'Exoplanets Catalog',
        'source': 'http://exoplanet.eu/catalog/'
      })
@app.route('/exoplanets/rand/<int:n>', methods=['GET'])
def get_exoplanets_rand(n):
    r = sample(exoplanets.keys(), n)
    return jsonify(r)
@app.route('/exoplanets/id/<string:pl_name>', methods=['GET'])
def get_planet_by_id(pl_name):
    if pl_name.lower() in exoplanets:
      return jsonify(exoplanets[pl_name.lower()])
    else:
      return jsonify({ 'error': 'Object not found.' })
@app.route('/exoplanets/hostname/<string:hs_name>', methods=['GET'])
def get_exoplanets_by_hostname(hs_name):
    res = []
    for p in exoplanets.values():
        if p['pl_hostname'] == hs_name:
            res.append(p)
    return jsonify(res)

@app.route('/messier', methods=['GET'])
def get_messier():
    return jsonify({
        'name': 'Messier Catalog',
        'source': 'FIXME'
      })
@app.route('/messier/rand/<int:n>', methods=['GET'])
def get_messier_rand(n):
    r = sample(messier.keys(), n)
    return jsonify(r)
@app.route('/messier/id/<string:m_name>', methods=['GET'])
def get_messier_by_id(m_name):
    if m_name.lower() in messier:
      return jsonify(messier[m_name.lower()])
    else:
      return jsonify({ 'error': 'Object not found.' })

if __name__ == '__main__':
    app.run(port=7799, debug=True)

