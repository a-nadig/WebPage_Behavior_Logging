function switchgraph(e){
	console.log(e);
	var plotURL = e.value + '.embed';
	console.log("Iske neeche");
	console.log(plotURL);
	var iframe = document.getElementById('firstplot');
	iframe.src = plotURL;
};

function switchgraph2(e){
	console.log(e);
	var plotURL = e.id + '.embed';
	console.log("Iske neeche");
	console.log(plotURL);
	var iframe = document.getElementById('secondplot');
	iframe.src = plotURL;
};



/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

