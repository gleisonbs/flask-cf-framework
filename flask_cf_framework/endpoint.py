class Endpoint:
    http_verbs = ["get", "head", "post", "put", "delete", "connect", "options",
                  "trace", "patch"]

    def __init__(self, request):
        self.headers = request.headers
        self.args = request.args
        self.body = request.get_json(silent=True)

    @classmethod
    def handle(cls, method):
        method = method.lower()
        methods = ([f for f in dir(cls) if f in cls.http_verbs])

        if method not in methods:
            print("405", "method not allowed")

        return getattr(cls, method)
