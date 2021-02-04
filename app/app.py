# Within app.py import the Flask module and create a web app using the following:
from flask import Flask
app = Flask(__name__)

# Next, let's define the basic route / and the corresponding request handler:
@app.route("/")
def index():
  return """
  <h1>Python Flask in Docker!</h1>
  <p>A sample web-app for running Flask inside Docker.</p>
  """
# Finally, let's launch the app if the script is invoked as the main program:
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
