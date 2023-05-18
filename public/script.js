document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const chatContainer = document.querySelector("#chat_container");



  function typeText(element, text) {
    let index = 0

    let interval = setInterval(() => {
        if (index < text.length) {
            element.innerHTML += text.charAt(index)
            index++
        } else {
            clearInterval(interval)
        }
    }, 20)
}


  function generateUniqueID() {
    const timestamp = Date.now();
    const randomNumber = Math.random();
    const hexadecimalstring = randomNumber.toString(16);

    return `id-${timestamp}-${hexadecimalstring}`;
  }

  function chatStripe(isAi, value, uniqueId) {
    return `
        <div class="wrapper ${isAi && 'ai'}">
            <div class="chat">
                <div class="profile">
                    <div class="profile-image"></div>
                </div>
                <div class="message" id="${uniqueId}">${value}</div>
            </div>
        </div>
    `;
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = new FormData(form);
    // User's chatstrip
    chatContainer.innerHTML += chatStripe(false, data.get('prompt'));

    form.reset();
    // Bot's chatstripe
    const uniqueId = generateUniqueID();
    chatContainer.innerHTML += chatStripe(true, " ", uniqueId);

    chatContainer.scrollTop = chatContainer.scrollHeight;

    const messageDiv = document.getElementById(uniqueId);
    //Second evidence chatstripe 


    //const inputValue = document.getElementById("input").value;

    await fetch('/main', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        prompt: data.get('prompt')
      })
    })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        messageDiv.innerHTML = " "
        evidence = ""
        for (item in data.arr) {
          evidence += "########Question########\n"
          evidence += data.arr[item].q + "\n" + data.arr[item].snips + "\n"
        }
        // typeText(messageDiv, data.gpt_response + "\n")
        messageDiv.innerHTML = data.gpt_response + evidence
        // const secId = generateUniqueID();
        // chatContainer.innerHTML += chatStripe(true, " ", secId);
        // evDiv = document.getElementById(secId);
        // console.log(data.arr)
        // typeText(evDiv,JSON.stringify(data.arr));
      })

    

    // messageDiv.innerHTML = " "


    //   if (response.ok) {
    //     const data = await response.json();
    //     const parsedData = data;  

    //     typeText(messageDiv, parsedData)
    // } else {
    //     const err = await response.text()

    //     messageDiv.innerHTML = "Something went wrong"
    //     alert(err)
    // }
  }
  form.addEventListener('submit', handleSubmit);
  form.addEventListener('keyup', (e) => {
    if (e.keyCode == 13) {
      handleSubmit(e);
    }
  })

});


// Get the input value
async function sendMain() {
    const inputValue = document.getElementById("input").value;
``
    if (inputValue) {
      // hide the header
      const headerElement = document.getElementById("header");
      headerElement.style.display = "none !important"; 
    }
    // Make a POST request to our Python function
    fetch('/main', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
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
      const gpt_response = data.gpt_response
      // chatoutput.innerHTML = printTextAnimated(gpt_response);
      
      const animatedText = printTextAnimated(`The fact checked response to ${inputValue} is ${data.result}.`).then(animatedText => {
        resultElement.innerHTML = data.gpt_response;
      });
      //resultElement.innerHTML = printTextAnimated("`The fact checked response to ${inputValue} is ${data.result}.`");
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }


  

    // function printTextAnimated(text) {
  //   const resultElement = document.getElementById('result');
  
  //   let i = 0;
  //   const intervalId = setInterval(() => {
  //     if (i < text.length) {
  //       resultElement.innerHTML += text.charAt(i);
  //       i++;
  //     } else {
  //       clearInterval(intervalId);
  //     }
  //   }, 20);
  // }


     // .then(response => response.json())
    // .then(data => { 
    //   // Update the HTML with the result
    //   console.log(data); 
    //   // const dataElement = document.getElementById("chatoutput")
    //   // dataElement.innerHTML = `The ChatGPT response to ${inputValue} is ${}`

    //  // const resultElement = document.getElementById("result");
    //   console.log(data.result);
      // const animatedText = printTextAnimated(`The fact checked response to ${data.result}.`).then(animatedText => {
      //   resultElement.innerHTML = animatedText;
      // })
    