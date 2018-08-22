#!/usr/bin/python3
"""places_amenities"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.amenity import Amenity
from datetime import datetime
import uuid
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    @app_views.route('/places/<place_id>/amenities', methods=['GET'])
    @app_views.route('/places/<place_id>/amenities/', methods=['GET'])
    def list_amenities_of_place(place_id):
        ''' Retrieves a list of all Amenity objects of a Place '''
        all_places = storage.all("Place").values()
        all_amenities = storage.all("Amenity").values()
        place_obj = [obj.to_dict() for obj in all_places if obj.id == place_id]
        if place_obj == []:
            abort(404)
        list_amenities = [obj.to_dict() for obj in all_amenities
                          if place_id == obj.place_id]
        return jsonify(list_amenities)

    @app_views.route('/places/<place_id>/amenities', methods=['POST'])
    def create_place_amenity(place_id):
        '''Creates a Amenity'''
        if not request.get_json():
            abort(400, 'Not a JSON')
        if 'user_id' not in request.get_json():
            abort(400, 'Missing user_id')
        user_id = request.json['user_id']
        if 'text' not in request.get_json():
            abort(400, 'Missing text')
        all_places = storage.all("Place").values()
        place_obj = [obj.to_dict() for obj in all_places if obj.id == place_id]
        if place_obj == []:
            abort(404)
        all_users = storage.all("User").values()
        user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
        if user_obj == []:
            abort(404)
        amenities = []
        new_amenity = Amenity(text=request.json['text'], place_id=place_id,
                              user_id=user_id)
        storage.new(new_amenity)
        storage.save()
        amenities.append(new_amenity.to_dict())
        return jsonify(amenities[0]), 201

    @app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
    def delete_place_amenity(amenity_id):
        '''Deletes a Amenity object'''
        all_amenities = storage.all("Amenity").values()
        amenity_obj = [obj.to_dict() for obj in all_amenities
                       if obj.id == amenity_id]
        if amenity_obj == []:
            abort(404)
        amenity_obj.remove(amenity_obj[0])
        for obj in all_amenities:
            if obj.id == amenity_id:
                storage.delete(obj)
                storage.save()
        return jsonify({}), 200

else:
    @app_views.route('/places/<place_id>/amenities', methods=['GET'])
    @app_views.route('/places/<place_id>/amenities/', methods=['GET'])
    def list_amenities_of_place(place_id):
        ''' Retrieves a list of all Amenity objects of a Place '''
        all_places = storage.all("Place").values()
        place_obj = [obj.to_dict() for obj in all_places
                     if obj.id == place_id]
        if place_obj == []:
            abort(404)
        all_amenities = storage.all("Amenity").values()
        list_amenities = [obj.to_dict() for obj in all_amenities
                          if place_id == obj.place_id]
        return jsonify(list_amenities)

    @app_views.route('/places/<place_id>/amenities', methods=['POST'])
    def create_place_amenity(place_id):
        '''Creates a Amenity'''
        if not request.get_json():
            abort(400, 'Not a JSON')
        if 'name' not in request.get_json():
            abort(400, 'Missing name')
        all_places = storage.all("Place").values()
        place_obj = [obj.to_dict() for obj in all_places
                     if obj.id == place_id]
        if place_obj == []:
            abort(404)
        all_users = storage.all("User").values()
        amenities = []
        new_amenity = Amenity(name=request.json['name'])
        for obj in all_places:
            if obj.id == place_id:
                obj.amenity_ids.append(new_amenity.id)
        storage.new(new_amenity)
        storage.save()
        amenities.append(new_amenity.to_dict())
        return jsonify(amenities[0]), 201

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['DELETE'])
    def delete_place_amenity(place_id, amenity_id):
        '''Deletes a Amenity object'''
        all_amenities = storage.all("Amenity").values()
        all_places = storage.all("Place").values()
        amenity_obj = [obj.to_dict() for obj in all_amenities
                       if obj.id == amenity_id]
        place_obj = [obj.to_dict() for obj in all_places
                     if obj.id == place_id]
        if amenity_obj == [] or place_obj == []:
            abort(404)
        amenity_obj.remove(amenity_obj[0])
        for obj in all_places:
            print(obj.amenity_ids)
            if obj.id == place_id:
                if amenity_id in obj.amenity_ids:
                    storage.delete(obj)
                    storage.save()
                else:
                    print("about to abort")
                    abort(404)
        return jsonify({}), 200


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_place_amenity(amenity_id):
    '''Retrieves a Amenity object '''
    all_amenities = storage.all("Amenity").values()
    amenity_obj = [obj.to_dict() for obj in all_amenities
                   if obj.id == amenity_id]
    if amenity_obj == []:
        abort(404)
    return jsonify(amenity_obj[0])


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def updates_place_amenity(amenity_id):
    '''Updates a Amenity object'''
    all_amenities = storage.all("Amenity").values()
    amenity_obj = [obj.to_dict() for obj in all_amenities
                   if obj.id == amenity_id]
    if amenity_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'text' in request.get_json():
        amenity_obj[0]['text'] = request.json['text']
        for obj in all_amenities:
            if obj.id == amenity_id:
                obj.text = request.json['text']
        storage.save()
    return jsonify(amenity_obj[0]), 200
