import logging

from flask import Flask
from flask import request
app = Flask(__name__)

def is_prime(num):
    """Check if a given number is a prime number."""
    for i in range(3, num):
        if num % i == 0:
            return False
    return True

@app.route("/")
def index():
    # make sure a number was provided
    if request.args.get('num') is None:
        return "Please provide a number via URL parameter, example: <a href='/?num=179426549'>?num=2038074743</a>"

    num = int(request.args.get('num'))

    message = "Sorry, %s is not prime :(" % num
    if is_prime(num):
        message = "It looks like %s is prime!" % num

    return message

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)