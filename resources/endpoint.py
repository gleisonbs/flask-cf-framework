class Endpoint:
    http_verbs = ["get", "head", "post", "put", "delete", "connect", "options",
                  "trace", "patch"]

    def __init__(self, request):
        self.parameters = request["parameters"]
        self.header = request["header"]
        self.body = request["body"]

    @classmethod
    def handle(cls, method):
        method = method.lower()
        methods = ([f for f in dir(cls) if f in cls.http_verbs])

        if method not in methods:
            print("405", "method not allowed")

        return getattr(cls, method)
