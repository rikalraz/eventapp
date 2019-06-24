from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'myriadevent'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/myriadevent'
#app.config['MONGO_URI'] = 'mongodb+srv://rikal:flask@flaskcluster-2btlm.mongodb.net/myriadevent?retryWrites=true&w=majority'


client = MongoClient("mongodb+srv://rikal:flask@flaskcluster-2btlm.mongodb.net/myriadevent?retryWrites=true&w=majority")
db = client.myriadevent


#mongo = MongoClient()
CORS(app)

@app.route('/v1/api/events', methods=['GET'])
def get_all_events():
    events = db.events
    result = []
    for field in events.find():
        result.append({'_id': str(field['_id']), 'title': field['title'], 'datetime': field['datetime'], 'venue':field['venue'], 'description':field['description'], 'venue_url':field['venue_url'], 'signup_code':field['signup_code']})
    return jsonify(result)


@app.route('/v1/api/events', methods=['POST'])
def add_event():
    events = db.events
    try:
        data = request.get_json()
        title = data['title']
        description = data['description']  
        datetime = data['datetime']
        venue = data['venue']
        venueurl = data['venue_url']
        signup_code = data['signup_code']
	
        if title and description and datetime and venue:
            event_id = events.insert({'title': title, 'description': description, 'datetime': datetime, 'venue':venue, 'venue_url': venueurl, 'signup_code': signup_code})
            new_event = events.find_one({'_id': event_id})

            result = {'_id':str(new_event['_id']), 'title': new_event['title'], 'description': new_event['description'], 'datetime': new_event['datetime'], 'venue':new_event['venue'], 'venue_url': new_event['venue_url'], 'signup_code': new_event['signup_code']}
            return jsonify({'message' : 'Event created successfully', 'data': result})
        else:
            return jsonify({"message": "Invalid values", 'data':{}})
			
    except (ValueError, KeyError, TypeError):
        # Not valid information, bail out and return an error
        return jsonify({"message": "Error!", 'data':{}})
		

@app.route('/v1/api/events/<id>', methods=['PUT'])
def update_events(id):
    events = db.events
    try:
        data = request.get_json()
        title = data['title']
        description = data['description']  
        datetime = data['datetime']
        venue = data['venue']
        venueurl = data['venue_url']
        signup_code = data['signup_code']
	
        if title and description and datetime and venue:
            events.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'title': title, 'description': description, 'datetime': datetime, 'venue':venue, 'venue_url': venueurl, 'signup_code': signup_code}})
            new_event = events.find_one({'_id': ObjectId(id)})

            result = {'_id':str(new_event['_id']), 'title': new_event['title'], 'description': new_event['description'], 'datetime': new_event['datetime'], 'venue':new_event['venue'], 'venue_url': new_event['venue_url'], 'signup_code': new_event['signup_code']}
            return jsonify({'message' : 'Event updated successfully', 'data': result})
        else:
            return jsonify({"message": "Invalid values", 'data':{}})
			
    except (ValueError, KeyError, TypeError):
        return jsonify({"message": "Error!", 'data':{}})
		
		
@app.route('/v1/api/events/<id>', methods=['DELETE'])
def delete_event(id):
    events = db.events
    response = events.delete_one({'_id': ObjectId(id)})

    if response.deleted_count == 1:
        result = {'message': 'Event deleted'}
    else:
        result = {'message': 'No record found'}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)