// Clears the calculator display
function clearScreen() {
    document.getElementById("result").value = "";
}

// Appends + join the clicked button's value to the display
function setScreenValue(value) {
    document.getElementById("result").value += value;//2*3 a+=a a=a+a
}

// Calculates and displays the result
function calculateResult() {
    const resultElement = document.getElementById("result");
    const expression = resultElement.value.trim();

    // Check for empty input
    if (expression === '') {
        resultElement.value = 'Enter an expression';
        return;
    }

    // Evaluate expression and handle errors2++2
    try {
        resultElement.value = eval(expression);
    } catch (e) {
        resultElement.value = 'Invalid expression'; //2++2
    }
}
