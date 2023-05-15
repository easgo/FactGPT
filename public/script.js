
console.log('hi');
async function printTextAnimated(text) {
  for (let i = 0; i < text.length; i++) {
    process.stdout.write(text.charAt(i));
    await new Promise((resolve) => setTimeout(resolve, 20));
  }
}

// Get the input value
async function sendMain() {
    const inputValue = document.getElementById("input").value;

    if (inputValue) {
      // hide the header
      const headerElement = document.getElementById("header");

      headerElement.style.display = "none !important"; 
    }
    // Make a POST request to our Python function
    fetch('/main', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      
      body: JSON.stringify({input: inputValue})
    })
    .then(response => response.json())
    .then(data => {
      // Update the HTML with the result
      console.log(data); 
      // const dataElement = document.getElementById("chatoutput")
      // dataElement.innerHTML = `The ChatGPT response to ${inputValue} is ${}`

      const resultElement = document.getElementById("result");
      console.log(data.result);
      const animatedText = printTextAnimated(`The fact checked response to ${inputValue} is ${data.result}.`).then(animatedText => {
        resultElement.innerHTML = animatedText;
      });
      //resultElement.innerHTML = printTextAnimated("`The fact checked response to ${inputValue} is ${data.result}.`");
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }
