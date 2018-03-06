var Card = function(noteTitle, noteAuthor, noteDescription) {
    this.noteTitle = noteTitle;
    this.noteAuthor = noteAuthor;
    this.noteDescription = noteDescription;
  }
var list = [new Card("Dijkstra's Algorithm", "Dijkstra", "This graph search algorithm is used in different ..."),
            new Card("Random Number Generation", "RNGod", "These are used in a large number of applications..."),
            new Card("Depth First Search", "Charles Tremeaux", "An algorithm for traversing or searching tree or graph data structures..."),
            ]


// for (var i = 0; i < 3; i++) {
//     var card = document.querySelector(".my-note-card");
//     var copy = card.cloneNode(true);

//     var cardBody = copy.childNodes[1].childNodes[3];
//     var cardTitle = cardBody.childNodes[1];
//     var cardText = cardBody.childNodes[3];
    
//     var curCard = list[i];

//     cardTitle.innerText = curCard.noteTitle;
//     cardText.innerText = curCard.noteDescription;

//     var myNotes = document.querySelector("#my-notes");
//     myNotes.appendChild(copy);
// }



// for (var i = 0; i < 3; i++) {

//     var card = document.querySelector(".recent-note-card");
//     var copy = card.cloneNode(true);


//     var cardBody = copy.childNodes[1].childNodes[3];
//     var cardTitle = cardBody.childNodes[1];
//     var cardText = cardBody.childNodes[3];
    
//     var curCard = list[i];

//     cardTitle.innerText = curCard.noteTitle;
//     cardText.innerText = curCard.noteDescription;

//     var recentNotes = document.querySelector("#recent-notes");
//     recentNotes.appendChild(copy);
// }

// for (var i = 0; i < 3; i++) {
//     var card = document.querySelector(".favorite-note-card");
//     var copy = card.cloneNode(true);

//     var cardBody = copy.childNodes[1].childNodes[3];
//     var cardTitle = cardBody.childNodes[1];
//     var cardText = cardBody.childNodes[3];
    
//     var curCard = list[i];

//     cardTitle.innerText = curCard.noteTitle;
//     cardText.innerText = curCard.noteDescription;

//     var favNotes = document.querySelector("#favorite-notes");
//     favNotes.appendChild(copy);
// }

$(function () {
    $('[data-toggle="popover"]').popover({
        html : true,
        content: function() {
          var content = $(this).attr("data-popover-content");
          return $(content).html();
        }
    })
  })
$('.popover-dismiss').popover({
    trigger: 'focus'
  })