document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const chatContainer = document.querySelector("#chat_container");
  

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

  function clickCorrect() {
    container = document.createElement('div'); 
    sentence = this.textContent;
    sentence = sentence.replace(/ /g, '+');
    fetch('/correct-facts?sentence=' + sentence, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then(response => response.json())
    .then(data => {
      console.log('Server response:', data.corrected_text);
      var correctedText = data.corrected_text; 

      var coloredText = '<span class="colored-text">' + correctedText + '</span>';
      container.innerHTML += coloredText;
      //container.innerHTML += correctedText; 

      var parentDiv = this.parentElement; 
      parentDiv.appendChild(container)
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }

  function createButtonsFromText(sentences) {
    
    var container = document.createElement('div');
    
    // Create a button for each sentence
    for (var i = 0; i < sentences.length; i++) {
      var button = document.createElement('button');
       // Set the button text as the sentence
      button.textContent = sentences[i];
      button.id = "textButton" + i;
      
      // button.addEventListener('click', function() {
      //   console.log('Button clicked:', this.textContent);
      // });           
      // Add the button to the container
      container.appendChild(button);
    }
    return container.innerHTML; 
  }



  function addEventListenersToButtons() {
    // Get all the buttons that have an id that starts with "textButton"
    var buttons = document.querySelectorAll('button[id^="textButton"]');
    // Loop through the buttons and add a click event listener to each
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener('click', clickCorrect);
    }
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
        //create the buttons here and then add event listeners to them

        messageDiv.innerHTML = createButtonsFromText(data.gpt_response)
        addEventListenersToButtons()


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
