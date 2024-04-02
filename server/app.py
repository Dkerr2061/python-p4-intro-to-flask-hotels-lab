#!/usr/bin/env python3

from flask import Flask

hotels = [
    {
        "id": 1,
        "name": "Marriott"
    },
    {
        "id": 2,
        "name": "Hampton Inn"
    },
    {
        "id": 3,
        "name": "Flatiron Resort"
    }
]

app = Flask(__name__)

@app.route('/')
def index():
    number_of_hotels = len(hotels)
    return f"<h1>Welcome to the Hotels website! We have {number_of_hotels} hotels available</h1>"
    
@app.route('/hotels')
def all_hotels():
    hotel_list = [f"<li>Hotel # {hotel['id']}: {hotel['name']}</li>" for hotel in hotels]
    return f"<ul>{''.join(hotel_list)}</ul>"

@app.route('/hotels/<int:id>')
def hotel_by_id(id):
    try:
        found_id = [hotel for hotel in hotels if hotel['id'] == id][0]
        return f"<h1>Hotel # {found_id['id']}: {found_id['name']}</h1>"
    except:
        return "<h1>Error: Hotel Not Found!</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
