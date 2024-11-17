from flask import Flask, request, jsonify, render_template

# start the server
app = Flask(__name__)

# route for rendering the main landing page of the UI
@app.route("/")
def home():
    # render the html page containing the form
    return render_template("index.html")

# route for processing the user input
@app.route("/processUserInput", methods=["POST"])
def processUserInput():
    # get the data from the front end
    userInput = request.get_json()

    # deconstruct the json to get each field
    age = userInput.get("age")
    gender = userInput.get("gender")
    socialMedia = userInput.get("socialMedia")
    dailyUsage = userInput.get("dailyUsage")
    postsPerDay = userInput.get("postsPerDay")
    likesReceivedPerDay = userInput.get("likesReceivedPerDay")
    commentsReceivedPerDay = userInput.get("commentsReceivedPerDay")
    messagesSentPerDay = userInput.get("messagesSentPerDay")

    # send it to our ML model

    # get the predicted output from the model
    prediction = {
        "output": "this is a placeholder for our prediction",
    }

    # send the output back to the front end
    return jsonify(prediction)

# initialize the main entry point for the server
if __name__ == "__main__":
    app.run(debug=True)