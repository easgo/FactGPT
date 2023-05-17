
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
      //the json looks like this 
      // arr = [{"q": question, "snips": ["string", "string", "string"]}, {"q": question, "snips": ["string", "string", "string"]]
      //write a script that takes the question and the snips and prints them out in a nice way
      //
      chatoutput = document.getElementById("chatoutput")
      const gpt_response = data.gpt_response
      chatoutput.innerHTML = printTextAnimated(gpt_response);

      const resultElement = document.getElementById("result");
      const questions = data.arr;
      
      // Iterate over each question
      questions.forEach(function(questionObj) {
        const question = questionObj.q;
        const snips = questionObj.snips;
      
        // Print the question
        const questionHeader = document.createElement("h3");
        questionHeader.textContent = "Question: " + question;
        resultElement.appendChild(questionHeader);
      
        // Print the snippets
        const snipsList = document.createElement("ul");
        snips.forEach(function(snip) {
          const snipItem = document.createElement("li");
          snipItem.textContent = snip;
          snipsList.appendChild(snipItem);
        });
        resultElement.appendChild(snipsList);
      
        // Empty line for formatting
        const lineBreak = document.createElement("br");
        resultElement.appendChild(lineBreak);
      });
      //resultElement.innerHTML = printTextAnimated("`The fact checked response to ${inputValue} is ${data.result}.`");
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }
