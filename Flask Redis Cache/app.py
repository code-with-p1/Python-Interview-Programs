from flask import Flask, request, jsonify
import redis
import time

app = Flask(__name__)

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def expensive_operation(param):
    # Simulate a time-consuming operation
    time.sleep(5)
    return f"Result of {param}"

@app.route('/compute', methods=['GET'])
def compute():
    param = request.args.get('param')
    if not param:
        return jsonify({"error": "Parameter 'param' is required"}), 400
    
    # Check if the result is cached
    cached_result = redis_client.get(param)
    if cached_result:
        return jsonify({"result": cached_result, "cached": True})
    
    # Perform the expensive operation
    result = expensive_operation(param)
    
    # Cache the result with an expiration time (e.g., 10 minutes)
    redis_client.setex(param, 600, result)
    
    return jsonify({"result": result, "cached": False})

if __name__ == '__main__':
    app.run(debug=True)
