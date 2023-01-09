<h1>cool random info :)</h1>

<html>
<body>

<table style="width:100%">
  <tr>
    <th>random fact</th>
    <th>random word</th>
  </tr>
  <tr>
    <td id = "a">no facts?</td>
    <td id = "b">no words?</td>

  </tr>
  <tr>
</tr>
</table>


 <script type="text/javascript" 
src="data4justin'sfeature.js"> // get data from outside file

</script>

<script>
      

random = Math.floor(Math.random() * facts.length);  // get random element from the lists in outside data
random2 = Math.floor(Math.random() * words.length);

factout = (random, facts[random]) //assign random 
wordout = (random, words[random2])


document.getElementById("a").innerHTML = (factout); 
document.getElementById("b").innerHTML = (wordout);
function reset() {
  window.location.reload();
}


</script> 

<button onclick="reset()">Click here to refresh for new facts!</button>

</body>
</html>