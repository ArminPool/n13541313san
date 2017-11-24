window.onload = function loadDoc() {
var d = new Date();
alert("i'm here");
var month = d.getMonth()+1;
var day = d.getDate();

var date = d.getFullYear() + '-' +
    ((''+month).length<2 ? '0' : '') + month + '-' ;

    var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("result").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "http://arminoldboy.pythonanywhere.com/EconomicCalendar/?q="+ date, true);
  xhttp.send();
  }