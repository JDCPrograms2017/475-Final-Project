from flask import Flask, request, jsonify, render_template
import socialmodel as sm

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

    # deconstruct the json to get each field and format it into a dictionary to send to the model
    userInputDict = {
        "Age": userInput.get("age"),
        "Daily_Usage_Time..minutes.": userInput.get("dailyUsage"),
        "Posts_Per_Day": userInput.get("postsPerDay"),
        "Likes_Received_Per_Day": userInput.get("likesReceivedPerDay"),
        "Comments_Received_Per_Day": userInput.get("commentsReceivedPerDay"),
        "Messages_Sent_Per_Day": userInput.get("messagesSentPerDay"),
        "gender": userInput.get("gender"),
        "socialMedia": userInput.get("socialMedia")
    }

    # call the ML model with the data
    # and get the predicted output from the model
    prediction = sm.make_predictions(userInputDict)

    # send the output back to the front end
    return jsonify(prediction)

# initialize the main entry point for the server
if __name__ == "__main__":
    app.run(debug=True)