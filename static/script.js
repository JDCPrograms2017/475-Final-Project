
// sends the data entered by the user into our python backend
async function sendData() {
    // make sure submitting the form doesnt cause the page to refresh
    //event.preventDefault()

    // grab all the data that the user entered
    const age = parseInt(document.getElementById("age").value, 10);
    const gender = document.getElementById("gender").value;
    const socialMedia = document.getElementById("socialMedia").value;
    const dailyUsage = parseInt(document.getElementById("daily-usage").value, 10);
    const postsPerDay = parseInt(document.getElementById("postsPerDay").value, 10);
    const likesReceivedPerDay = parseInt(document.getElementById("likesReceivedPerDay").value, 10);
    const commentsReceivedPerDay = parseInt(document.getElementById("commentsReceivedPerDay").value, 10);
    const messagesSentPerDay = parseInt(document.getElementById("messagesSentPerDay").value, 10);

    // format the data so we can send it to the back end nicely
    const userInput = {
        age: age,
        gender: gender,
        socialMedia: socialMedia,
        dailyUsage: dailyUsage,
        postsPerDay: postsPerDay,
        likesReceivedPerDay: likesReceivedPerDay,
        commentsReceivedPerDay: commentsReceivedPerDay,
        messagesSentPerDay: messagesSentPerDay,
    }

    // use a try-catch to handle unexpected errors in the communication with the backend
    try {
        // send the data to the back end
        const response = await fetch("/processUserInput", {
            method: "POST",
            headers: { // we need to tell the server that were sending json formatted data
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userInput)
        })
        // display the response
        const responseData = await response.json()
        document.getElementById("output").innerText = Json.stringify(responseData, null, 2)
    } catch (e) {
        // display an error message
        errorMessage = "Error with communication from the back end." + e.message
        document.getElementById("output").innerText = errorMessage
    }
}