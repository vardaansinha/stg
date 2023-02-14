<h1>Education: Cool Information</h1>

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
    <th>question</th>
    <th>Answer</th>
  </tr>
  <tr>
    <td id = "question">a question</td>
    <td id = "correct?">correct answer appears when the question's answered correctly</td>

  </tr>
  <tr>
</tr>
</table>



 <script type="text/javascript" 
src="data4justin'sfeature.js"> // get data from outside file

</script>

<script>

function question(){
  random3 = Math.floor(Math.random() * quest.length); 

  questout = (random, quest[random3]);

  questoutQ = questout.question;
  
  questoutANS = questout.correctAnswer;

  document.getElementById("question").innerHTML = (questoutQ);
  document.getElementById("correct?").innerHTML = ("The correct answer will appear when the question is answered correctly");

  alert("new question made!")
}

function test(ans){
  ans = parseInt(useranswer.value);
  
  if (ans == (questoutANS)) {
  
  alert("right!");
  
  document.getElementById("correct?").innerHTML = 
(questoutANS);
  

  } else if (isNaN(ans))  { //is it a number?

    alert("only numbers are allowed!")
  }

  else {
  
  alert("wrong answer!");
  x = 1
  while(true) {
    
    userInput = prompt(" Now think about the question and enter the correct answer this time");
  
  if (userInput == questoutANS) {
    
    alert("good job...")
    document.getElementById("correct?").innerHTML = 
(questoutANS);
    break;
  }
  x = x + 1;
  alert("how many times until you get it right? you have failed this question " + (x) + " times now!");
}
  }
    }



 /*function question(ans) {
  randquestion = ("test")
  randans = ("test2")
  i = 5
  var useranswer = letter1.value;
  while i == 1 {
    if useranswer = ("test2") {
      document.getelementbyid("right") = ("right!")
    }
  }
} */

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



<button onclick="question()">Click here to create a math question!</button>

<button onclick="test()">Click here to check the answer!</button>


 <p><label>
        put answer here!:
        <input type="text" name="letter1" id="useranswer">
    </label></p>


 <!-- <p><label>
        score:
        <input type="text" name="letter2" id="letter2">
    </label></p> -->

<script>

function store_data() {

var naMe1 = letter1.value;
var sCore1 = letter2.value;

alert("updated!");

document.getElementById("name").innerHTML = (naMe1); 
document.getElementById("score").innerHTML = (sCore1); 


}



</script>

 <!-- <p><button onclick="store_data()">add names and score</button></p> -->

<form action="javascript:create_user()">
 <p><label>
        add a new fact:
        <input type="text" name="test" id="testr" required>
    </label></p>
    <p><button>Create</button></p>
</form>

<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
  const url = "http://localhost:8086/api/scores"
  //const url = "https://flask.nighthawkcodingsociety.com/api/users"
  const create_fetch = url + '/create';
  const read_fetch = url + '/';

read_scores();




</script>


</body>

</html>