

from flask import Flask, Response, request, json

app = Flask(__name__, static_folder='static')


@app.route("/")
def ipcheck():
  proxy_headers = [
    'via',
    'forwarded',
    'client-ip',
    'useragent_via',
    'proxy_connection',
    'xproxy_connection',
    'http_pc_remote_addr',
    'http_client_ip',
    'http_x_appengine_country'
  ]

  headers = dict((x, request.headers.get(x)) for x in proxy_headers if request.headers.get(x) is not None)
  dat = json.dumps(headers)

  return Response(response = dat,
    status = 200,
    mimetype="application/json")

if __name__ == "__main__":
  app.run()