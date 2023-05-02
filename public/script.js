function sendMain() {
    // Get the input value
    const inputValue = document.getElementById("input").value;
  
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
      const resultElement = document.getElementById("result");
      resultElement.innerHTML = `The fact checked response to ${inputValue} is ${data.result}.`;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }