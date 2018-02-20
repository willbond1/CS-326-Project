

 

var Card = function(noteTitle, noteAuthor, noteDescription) {
    this.noteTitle = noteTitle;
    this.noteAuthor = noteAuthor;
    this.noteDescription = noteDescription;
  }
var list = [new Card("Dijkstra's Algorithm", "Dijkstra", "This graph search algorithm is used in different applications where the problem can be modeled as a graph and you have to find the shortest path between two nodes."),
            new Card("Random Number Generation", "RNGod", "These are used in a large number of applications, from interlink connection, cryptography, secure hash algorithm, video games, artificial intelligence, optimization, to initial conditions for problems, finances, etc."),
            new Card("Depth First Search", "Charles Tremeaux", "An algorithm for traversing or searching tree or graph data structures."),
            ]




for (var i = 0; i < 3; i++) {
    var card = document.querySelector(".recently-uploded-notes-card");
    var copy = card.cloneNode(true);

    var cardBody = copy.childNodes[1].childNodes[3];
    var cardTitle = cardBody.childNodes[1];
    var cardText = cardBody.childNodes[3];
    
    var curCard = list[i];

    cardTitle.innerText = curCard.noteTitle;
    cardText.innerText = curCard.noteDescription;

    var myNotes = document.querySelector("#Recently-Uploaded-Notes");
    myNotes.appendChild(copy);
}

for (var i = 0; i < 3; i++) {

    var card = document.querySelector(".All-Uploaded-Notes-card");
    var copy = card.cloneNode(true);


    var cardBody = copy.childNodes[1].childNodes[3];
    var cardTitle = cardBody.childNodes[1];
    var cardText = cardBody.childNodes[3];
    
    var curCard = list[i];

    cardTitle.innerText = curCard.noteTitle;
    cardText.innerText = curCard.noteDescription;

    var recentNotes = document.querySelector("#All-Uploaded-Notes");
    recentNotes.appendChild(copy);
}

 
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

/*
for (var i = 0; i < 3; i++) {
    var card = document.querySelector(".recently-uploded-notes-card");
    var copy = card.cloneNode(true);
    var myNotes = document.querySelector("#Recently-Uploaded-Notes");
    myNotes.appendChild(copy);
}   

for (var i = 0; i < 3; i++) {
    var card = document.querySelector(".All-Uploaded-Notes-card");
    var copy = card.cloneNode(true);
    var recentNotes = document.querySelector("#All-Uploaded-Notes");
    recentNotes.appendChild(copy);
}

*/




 