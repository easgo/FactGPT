document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const chatContainer = document.querySelector("#chat_container");

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

  function createButtonsFromText(sentences) {
    
    var container = document.createElement('div');
    
    // Create a button for each sentence
    for (var i = 0; i < sentences.length; i++) {
      var button = document.createElement('button');
    
      // Set the button text as the sentence
      button.textContent = sentences[i];

      button.addEventListener('click', function() {
        var sentence = this.textContent;
      
        fetch('/correct-facts', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            sentence: sentence
          })
        })
        .then(response => response.json())
        .then(data => {
          console.log('Server response:', data.corrected_text);
        })
        .catch(error => {
          console.error('Error:', error);
        });
      });
      

      
      // button.addEventListener('click', function() {
      //   console.log('Button clicked:', this.textContent);
      // });
    
      // Add the button to the container
      container.appendChild(button);
    }
    return container.innerHTML; 
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
        


        /* **** READ ME****  
        
        data.gpt_response is an array with each entry being each individual string.. Not sure how to display those separately but you can access them here at least */
        /*Also there's a method in app.py now called "get_single_replaced_sentence(string)" which takes in a string and returns the replaced string. We just need to have a call to it when text is clicked/something like that*/
        
        
        // typeText(messageDiv, data.gpt_response + "\n")
        messageDiv.innerHTML = createButtonsFromText(data.gpt_response) //we would obviously need to change this to the whole sentences as objects thing, just doing this temporarily
        // const secId = generateUniqueID();
        // chatContainer.innerHTML += chatStripe(true, " ", secId);
        // evDiv = document.getElementById(secId);
        // console.log(data.arr)
        // typeText(evDiv,JSON.stringify(data.arr));
      })
  }
  form.addEventListener('submit', handleSubmit);
  form.addEventListener('keyup', (e) => {
    if (e.keyCode == 13) {
      handleSubmit(e);
    }
  })

});







