
from flask import Flask, jsonify
from flask_cors import CORS

import json
from random import sample
from astropy.io import fits

app = Flask(__name__)
CORS(app)

with open('y-s-datasets/exoplanets/exoplanets.json') as f:
    exoplanets = json.load(f)

with open('y-s-datasets/exoplanets/exoplanets-stats.json') as f:
    exoplanets_stats = json.load(f)

with open('y-s-datasets/messier/messier.json') as f:
    messier = json.load(f)

with open('y-s-datasets/tess/tess.json') as f:
    tess = json.load(f)

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
@app.route('/exoplanets/list', methods=['GET'])
def get_exoplanets_list():
    r = list(exoplanets.keys())
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
@app.route('/exoplanets/stats', methods=['GET'])
def get_exoplanets_stats():
    return jsonify(exoplanets_stats)

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
@app.route('/messier/list', methods=['GET'])
def get_messier_list():
    r = list(messier.keys())
    return jsonify(r)
@app.route('/messier/id/<string:m_name>', methods=['GET'])
def get_messier_by_id(m_name):
    if m_name.lower() in messier:
      return jsonify(messier[m_name.lower()])
    else:
      return jsonify({ 'error': 'Object not found.' })

@app.route('/tess', methods=['GET'])
def get_tess():
    return jsonify({
        'name': 'TESS Catalog',
        'source': 'https://archive.stsci.edu/tess/'
      })
@app.route('/tess/id/<string:ticid>', methods=['GET'])
def get_tess_by_id(ticid):
    if ticid in tess:
      return jsonify(tess[ticid])
    else:
      return jsonify({ 'error': 'Object not found.' })
@app.route('/tess/full/<string:ticid>', methods=['GET'])
def get_tess_full_by_id(ticid):
    if ticid in tess:
      obj = tess[ticid]
      hdul = fits.open(obj['url'])
      record = hdul[1].data
      data = {}
      for c in record.columns.names:
          data[c] = record[c].tolist()
      obj['data'] = data
      return jsonify(tess[ticid])
    else:
      return jsonify({ 'error': 'Object not found.' })

@app.route('/', methods=['GET'])
def _root():
  return('http://api.y-space-pw')

if __name__ == '__main__':
    app.run(port=7799, debug=True)

