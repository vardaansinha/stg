<h1>cool random info :) (learn something new every day)</h1>

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

<table style="width:100%">
  <tr>
    <th>name</th>
    <th>score</th>
  </tr>
  <tr>
    <td id = "name">name</td>
    <td id = "score">score</td>

  </tr>
  <tr>
</tr>
</table>



 <script type="text/javascript" 
src="data4justin'sfeature.js"> // get data from outside file

</script>

<script>
      

random = Math.floor(Math.random() * facts.length);  // get random element from the lists in outside data (thks stack overflow)
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





<p><label>
        name:
        <input type="text" name="letter1" id="letter1">
    </label></p>

<p><label>
        score:
        <input type="text" name="letter2" id="letter2">
    </label></p>

<script>

function store_data() {

var naMe1 = letter1.value;
var sCore1 = letter2.value;

alert("updated!");

document.getElementById("name").innerHTML = (naMe1); 
document.getElementById("score").innerHTML = (sCore1); 


}


</script>

 <p><button onclick="store_data()">add names and score</button></p>

</body>

</html>