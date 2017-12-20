window.onload = function loadDoc() {
var d = new Date();
var month = d.getMonth()+1;
var day = d.getDate();

var date = d.getFullYear() + '-' +
    ((''+month).length<2 ? '0' : '') + month + '-' ;
alert(date);
    var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("result").innerHTML = this.responseText;
      alert('we did itttttt');
    }
  };
  xhttp.open("GET", "/economicCalendar/?q="+ date, true);
  xhttp.send();
  }