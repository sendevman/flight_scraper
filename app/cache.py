import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

def cache_flight_data(key, data):
    r.set(key, json.dumps(data))

def get_cached_flight_data(key):
    data = r.get(key)
    return json.loads(data) if data else None