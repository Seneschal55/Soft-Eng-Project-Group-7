var nav_html = '';
nav_html += '<a href="bloomington_pedestrians.html">Pedestrian/ Cyclist Information</a>';
nav_html += '<a href="bloomington_crashesbyreasonandstreet_barchart.html">Crash Data by Reason and Street</a>';
nav_html += '<a href="bloomington_crashesbydaymonthandyear_barchart.html">Time and Type of Crashes</a>';
nav_html += '<a href="bloomington_timeandtype.html">Crash Statistics Over Time</a>';

var footer_html = '';
footer_html += '<p>This site was made as a school project for the city of Bloomington, Indiana</p>';

window.onload = function(){
    document.getElementById("nav-bar").innerHTML = nav_html;
    document.getElementById("footer-bar").innerHTML = footer_html;
}

