window.onload = function loadDoc() {
var d = new Date();

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
  xhttp.open("GET", "http://127.0.0.1:8000/EconomicCalendar/?q="+ date, true);
  xhttp.send();
  }