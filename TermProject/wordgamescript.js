const letters = [document.getElementById("p-letter"), document.getElementById("r-letter"), document.getElementById("i-letter"), document.getElementById("s-letter"), document.getElementById("m-letter")];
const submitButton = document.getElementById("submit-btn");
const resetButton = document.getElementById("reset-btn");
const guessBox = document.getElementById("guess-box");
const scoreContainer = document.getElementById("score");
const heartsContainer = document.getElementById("hearts");

const word = "prism";
let score = 0;
let lives = 3;
let openLetters = 0;

function updateScore() {
    scoreContainer.textContent = `Score: ${score}`;
}

function updateHearts() {
    heartsContainer.innerHTML = "";
    for (let i = 0; i < lives; i++) {
        const heart = document.createElement("img");
        heart.src = "heart.svg";
        heart.classList.add("heart");
        heartsContainer.appendChild(heart);
    }
}

function revealLetter(guess) {
    let correctGuess = false;
    for (let i = 0; i < word.length; i++) {
        if (word[i] === guess.toLowerCase() && letters[i].classList.contains("hidden")) {
            letters[i].classList.remove("hidden");
            correctGuess = true;
            openLetters++;
        }
    }
    return correctGuess;
}

function checkWin() {
    if (openLetters === word.length) {
        alert("Congratulations! You won the game!");
        submitButton.disabled = true;
    }
}

resetButton.style.display = "none"

guessBox.addEventListener("keydown", () => {
    resetButton.style.display = "block"
});

submitButton.addEventListener("click", () => {
    const guess = guessBox.value.toLowerCase();
    if (guess.length !== 1 && guess.length !== 5) {
        alert("Please enter a single letter or the whole word.");
        return;
    }

    const correctGuess = revealLetter(guess);
    if (correctGuess) {
        score += 20;
        updateScore();
        checkWin();
    } else {
        lives--;
        updateHearts();
        if (lives === 0) {
            alert("Game Over! You've run out of lives.");
            submitButton.disabled = true;
        }
    }

    guessBox.value = "";
});

resetButton.addEventListener("click", () => {
    score = 0;
    lives = 3;
    openLetters = 0;
    updateScore();
    updateHearts();
    submitButton.disabled = false;
    letters.forEach(img => img.classList.add("hidden"));
    guessBox.value = "";
});

updateScore();
updateHearts();