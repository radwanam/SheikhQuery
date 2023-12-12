document.addEventListener("DOMContentLoaded", function () {
  //ALL THIS IS MODAL STUFF
  // Get the modal
  var modal = document.getElementById("tmgan");

  // Get the button that opens the modal
  var btn = document.getElementsByClassName("box");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal
  btn.onclick = function () {
    modal.style.display = "block";
  };

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  };

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };

  var modals = document.getElementsByClassName("modal");
  var btns = document.getElementsByTagName("button");
  var spans = document.getElementsByClassName("close");

  for (var i = 0; i < btns.length; i++) {
    (function (index) {
      btns[index].onclick = function () {
        modals[index].style.display = "block";
      };

      spans[index].onclick = function () {
        modals[index].style.display = "none";
      };
    })(i);
  }

  window.onclick = function (event) {
    for (var i = 0; i < modals.length; i++) {
      if (event.target === modals[i]) {
        modals[i].style.display = "none";
      }
    }
  };
  // END MODAL STUFF



//START SEARCH STUFF
  // Get the search form and search input field
  const searchForm = document.getElementById("search-form");
  const searchInput = document.getElementById("search-input");
  const resultsContainer = document.querySelector(".card-container");

  // Add an event listener to the search form for form submission
  searchForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const query = searchInput.value.trim();

    fetch("/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: query }),
    })
      .then((response) => response.json())
      .then((data) => {
        resultsContainer.innerHTML = ""; // Clear previous search results

        if (data.length === 0) {
          resultsContainer.innerHTML = "<p>No results found.</p>";
        } else {
          data.forEach((card) => {
            resultsContainer.innerHTML += `
            <button class="card-btn" data-title="${card.title}" data-transcript="${card.transcript}" data-embed="${card.embed}" data-author="${card.author}">
              <div class="card">
                <div class="card-header">
                  <h2>${card.title}</h2>
                </div>
              </div>
            </button>

            <div id="tmgan" class="modal">
              <div class="modal-content" class="card-body">
                <span class="close">&times;</span>
                <div>Question: ${card.title}</div>
                <br/>
                <div>Answer:</div>
                <div class="full-transcript">${card.transcript}</div>
                <br/>
                <p>Original Video:</p>
                <div class="video-container">
                  <iframe loading="lazy" src="${card.embed}"></iframe>
                </div>
                <p class="author">Author: ${card.author}</p>
              </div>
            </div>
          `;
          });
        }
      })
      .catch((error) => console.error("Error performing search:", error));
  });
  resultsContainer.addEventListener("click", function (event) {
    const target = event.target;

    // Check if the click target is a card button or its parent (in case the click happened on the card itself)
    const cardButton = target.closest(".card-btn");
    if (cardButton) {
      const modal = document.getElementById("tmgan");
      const title = cardButton.dataset.title;
      const transcript = cardButton.dataset.transcript;
      const embed = cardButton.dataset.embed;
      const author = cardButton.dataset.author;

      const modalContent = modal.querySelector(".modal-content");
      modalContent.innerHTML = `
        <span class="close">&times;</span>
        <div>Question: ${title}</div>
        <br/>
        <div>Answer:</div>
        <div class="full-transcript">${transcript}</div>
        <br/>
        <p>Original Video:</p>
        <div class="video-container">
          <iframe loading="lazy" src="$"></iframe>
        </div>
        <p class="author">Author: ${author}</p>
      `;

      modal.style.display = "block";
    }
  });
})