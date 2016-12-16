

from flask import Flask, Response, request, json

app = Flask(__name__, static_folder='static')


@app.route("/")
def ipcheck():
  print request.headers.keys()

  remote_ip = request.remote_addr
  x_forwarded_for = request.headers.get('X-Forwarded-For')
  via = request.headers.get('Via')

  return "{};{};{}".format(remote_ip, x_forwarded_for, via)

if __name__ == "__main__":
  app.run()