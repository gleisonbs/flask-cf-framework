def request(request, _id=""):
    print(f"Request {_id}: {request.method} {request.path} {request.get_json(silent=True)}")

def response(response, _id=""):
    print(f"Response {_id}: {response[1]} {response[0]} {response[2]}")