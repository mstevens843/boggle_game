const $form = $("#word-form");
const $wordInput = $("#word");
const $result = $("#result");
const $score = $("#score");
const $highscore = $("#highscore");
const $timesPlayed = $("#times_played");
const $timer = $("#timer");

let currentScore = 0;
let timer = 60;

async function handleSubmit(e) {
    e.preventDefault();
    const word = $wordInput.val();
    if (!word) return;

    // Make the request to check the word
    try {
        const res = await axios.get("/check-word", { params: { word } });
        const result = res.data.result;

        // If the word is valid, update the score
        if (result === "ok") {
            currentScore = res.data.score;  // Use the score returned from the server
            $score.text(currentScore);  // Update the score in the UI
        }

        // Display the result to the user
        $result.text(result === "ok" ? "Valid word!" : result === "not-on-board" ? "Word not on board!" : "Not a valid word!");
    } catch (error) {
        console.error("Error during word submission:", error);  // Debugging
    }

    $wordInput.val('');  // Clear the input field
}

$form.on("submit", handleSubmit);

function startTimer() {
    const interval = setInterval(async () => {
        timer--;
        $timer.text(`Time Left: ${timer}`);
        if (timer <= 0) {
            clearInterval(interval);
            $form.off("submit");
            await postScore();
        }
    }, 1000);
}

async function postScore() {
    try {
        const res = await axios.post("/post-score", { score: currentScore });
        if (res.data.brokeRecord) {
            alert("New High Score!");
            $highscore.text(currentScore);  // Update high score in the UI
        }
        const updatedTimesPlayed = Number($timesPlayed.text()) + 1;
        $timesPlayed.text(updatedTimesPlayed);  // Update times played in the UI
    } catch (error) {
        console.error("Error posting score:", error);  // Debugging
    }
}

startTimer();  // Start the timer when the game starts
