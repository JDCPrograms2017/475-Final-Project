from flask import Flask, request, jsonify, render_template

# start the server
app = Flask(__name__)


# initialize the main entry point for the server
if __name__ == "__main__":
    app.run(debug=True)