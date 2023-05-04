// Get the input value
async function sendMain() {
    const inputValue = document.getElementById("input").value;
    console.log(inputValue)

    if (inputValue) {
      // hide the header
      const headerElement = document.getElementById("header"); 
      headerElement.style.display = "none"; 
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

      const resultElement = document.getElementById("result");
      resultElement.innerHTML = `The fact checked response to ${inputValue} is ${data.result}.`;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }
