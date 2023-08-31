#!/usr/bin/env python3
import os
import kong_pdk.pdk.kong as kong
import json
Schema = (
    {"message": {"type": "string"}},
)

version = '0.1.0'
priority = 0

# This is an example plugin that add a header to the response

class Plugin(object):
    def __init__(self, config):
        self.config = config
    def transform1(body):
        resp = json.loads(body)
        resp['text'] = 'test'
        return json.dumps(resp)

    def access(self, kong: kong.kong):
        host, err = kong.request.get_header("host")
        if err:
            pass  # error handling
        # if run with --no-lua-style
        # try:
        #     host = kong.request.get_header("host")
        # except Exception as ex:
        #     pass  # error handling

        body = kong.service.response.get_raw_body()
        if body:
          body = transform1(body)
          print(body)
          kong.response.clear_header("Content-Length")
          kong.response.set_raw_body(body)
        message = "hello"
        if 'message' in self.config:
            message = self.config['message']
        kong.response.set_header("x-hello-from-python", "Python says %s to %s" % (message, host))
        kong.response.set_header("x-python-pid", str(os.getpid()))
    
    def response(self, kong: kong.kong):
        body = kong.service.response.get_raw_body()

        body = transform1(body)
        print(body)
        kong.response.clear_header("Content-Length")
        kong.response.set_raw_body(body)


# add below section to allow this plugin optionally be running in a dedicated process
if __name__ == "__main__":
    from kong_pdk.cli import start_dedicated_server
    start_dedicated_server("redact-plugin", Plugin, version, priority, Schema)
