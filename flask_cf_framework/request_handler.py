class RequestHandler:
    def __init__(self):
        self.endpoints = {}

    def add(self, cls, endpoint):
        self.endpoints[endpoint] = cls

    def handle(self, request):
        path = request.path
        endpoint = self.endpoints[path]
        http_verb = request.method

        http_verb_handler = endpoint.handle(http_verb)
        return http_verb_handler(endpoint(request))
