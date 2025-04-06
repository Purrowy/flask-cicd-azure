from flask import Flask, request, render_template, request, jsonify
import os

app = Flask(__name__)
locations = []

@app.route('/')
def hello_world():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    return render_template('index.html', api_key=api_key)

@app.route('/add_pin', methods=['POST'])
def add_pin():
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    if lat and lng:
        locations.append({'lat': lat, 'lng': lng})
        return jsonify({'status': 'success', 'locations': locations})
    return jsonify({'status': 'error'}), 400

@app.route('/add_location', methods=['POST'])
def add_location():
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    address = data.get('address', 'Unknown')
    city = data.get('city', 'Unknown')
    place_name = data.get('placeName', 'Unknown')

    if lat is not None and lng is not None:
        locations.append({
            'lat': lat,
            'lng': lng,
            'address': address,
            'city': city,
            'placeName': place_name
        })
        return jsonify({'status': 'success', 'locations': locations})
    return jsonify({'status': 'error'}), 400


@app.route('/get_locations', methods=['GET'])
def get_locations():
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)