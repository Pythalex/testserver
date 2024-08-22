# testserver

A simple HTTP test server that will print incoming requests query, headers and body.

See on [Docker Hub](https://hub.docker.com/r/pythalex/testserver)

To quickly run with docker:

```bash
docker run -it -p 80:8888 pythalex/testserver:latest
```

## example

```
$ docker run -it -p 80:8888 pythalex/testserver:latest
[08/22/24 09:41:38] INFO     2024-08-22 09:41:38,752:INFO:root:run  testserver.py:67
                             Starting httpd... on port 8888

[08/22/24 09:41:53] INFO     2024-08-22                             testserver.py:37
                             09:41:53,008:INFO:root:do_POST POST
                             request,
                             Path: /
                             Headers:
                             Host: localhost
                             User-Agent: curl/7.74.0
                             Accept: */*
                             Content-Length: 11
                             Content-Type:
                             application/x-www-form-urlencoded



                             Body:
                             Hello world

172.17.0.1 - - [22/Aug/2024 09:41:53] "POST / HTTP/1.1" 200 -
```
