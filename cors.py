def cors(response, code):
    return response, code, { "Access-Control-Allow-Origin": "*"}

def preflight():
    return "", 204, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600"
    }