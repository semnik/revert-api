import falcon
from wsgiref import simple_server
import json


class ReverseResource(object):

    def to_json(self, body_dict):
        return json.dumps(body_dict, ensure_ascii=False)

    def on_post(self, req, resp):

        try:

            raw_json = req.stream.read()

        except Exception as ex:

            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Error',
                                   ex.message)

        try:

            decoded_json = json.loads(raw_json, encoding='utf-8')
            reversed_string = decoded_json['text'][::-1]

        except(ValueError, KeyError):

            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode the request body. '
                                   'The JSON was incorrect.')

        resp.status = falcon.HTTP_201
        dict_obj = {"response": reversed_string}
        resp.body = self.to_json(dict_obj)


application = falcon.API()

application.add_route('/revert', ReverseResource())

if __name__ == "__main__":
    httpd = simple_server.make_server('0.0.0.0', 8080, application)
    print("falcon service starting on localhost: "
          "{}".format(httpd.base_environ['SERVER_PORT']))
    httpd.serve_forever()
