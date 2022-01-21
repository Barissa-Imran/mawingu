function menu () {
    
};

var timeDisplay = document.getElementById("time");

function refreshTime() {
  var dateString = new Date(Date.now());
//   var formattedString = dateString.replace(", ", " - ");
  timeDisplay.innerHTML = dateString;
}

setInterval(refreshTime, 1000);