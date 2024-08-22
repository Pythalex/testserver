#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
import logging
import logging.config
import yaml
from http.server import BaseHTTPRequestHandler, HTTPServer


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        logging.info(
            "GET request,\nPath: %s\nHeaders:\n%s\n",
            str(self.path),
            str(self.headers),
        )
        self._set_response()
        self.wfile.write(
            "GET request for {}".format(self.path).encode("utf-8")
        )

    def do_POST(self):
        content_length = int(
            self.headers["Content-Length"]
        )  # <--- Gets the size of data
        post_data = self.rfile.read(
            content_length
        )  # <--- Gets the data itself
        logging.info(
            "POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
            str(self.path),
            str(self.headers),
            post_data.decode("utf-8"),
        )

        with open("/tmp/payload_received", "wb") as f:
            f.write(post_data)

        self._set_response()
        self.wfile.write(
            "POST request for {}".format(self.path).encode("utf-8")
        )


def run(server_class=HTTPServer, handler_class=S, port=8888):
    logging.basicConfig(level=logging.INFO)
    try:
        with open("logging.yml", "r") as stream:
            logging_cfg = yaml.load(stream, Loader=yaml.FullLoader)
            logging.config.dictConfig(logging_cfg)
    except FileNotFoundError:
        logging.warning(
            "logging.yml not found, logging will be basic. Note: You can use"
            " logging.yml.example."
        )

    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logging.info(f"Starting httpd... on port {port}\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("Stopping httpd...\n")


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
