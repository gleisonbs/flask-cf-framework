import re


class RequestHandler:
    def __init__(self):
        self.endpoints = {}

    def add(self, cls, endpoint):
        self.endpoints[endpoint] = cls

    def _make_params(self, meta_info, values):
        params = {}
        for info, value in zip(meta_info, values):
            p_type = info[0]
            p_name = info[1]
            p_value = value

            params[p_name] = {
                "type": p_type,
                "value": p_value
            }
        return params

    def _match_route(self, uri):
        if uri in self.endpoints:
            return uri, []

        parameters_re = re.compile("<(\\w+):(\\w+)>")
        for route in self.endpoints.keys():
            params_desc = parameters_re.findall(route)
            if params_desc:
                new_path_re = re.sub(parameters_re, "(\\\w+)", route)
                new_path_re = f"^{new_path_re}$"

                route_params_values = re.match(new_path_re, uri)

                if route_params_values:
                    params_values = route_params_values.groups()
                    params = self._make_params(params_desc, params_values)
                    return route, params

        return "", []

    def handle(self, request):
        path = request.path
        route, params = self._match_route(path)

        endpoint = self.endpoints.get(route)
        if not endpoint:
            return "", 404

        http_verb = request.method

        http_verb_handler = endpoint.handle(http_verb)
        endpoint_handler = endpoint(request)
        endpoint_handler.parameters = params

        return http_verb_handler(endpoint_handler)
