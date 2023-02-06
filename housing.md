## On This Day
> Want to see cool things (and some not so cool things) that have happened on this day? Look below!


<br/>
<button name="button" onclick="getQuotes()" >Show me what happened on February 6th.</button>

<br/>

- <p class="news2_style" id="tips1">Click the above button to see some cool events that have happened on this day.</p>
- <p class="news2_style" id="tips2"></p>
- <p  class="news2_style" id="tips3"></p>
- <p class="news2_style" id="tips4"></p>
- <p  class="news2_style" id="tips5"></p>

<script>
var healthArray = [
"1932: First Olympic Dog sled race takes place in New York",
"1935: Monopoly goes on sale for the first time",
"1948: Cricket legend Donald Bradman retires hurt in his last innings for the Australian National Team.",
"1911: Rolls-Royce Mascot Chosen",
"1952: King George VI Dies",
"1971: Alan Shepard becomes the first man to hit a golf ball on the Moon. He hid this in his space suit!",
"1943: Frank Sinatra made his singing debut with 'Your Hit Parade'.",
"1958: 8 Man United players died in a British European Airways flight crash from Munich Airport.",
"2003: The infamous Michael Jackson interview 'Living with Michael Jackson' aired on ABC.",
"2007: DoS attack slams the Internet and lasts for 2.5 hours.",	
];
								       
// this function is called upon button click
function getQuotes() {
	var time = new Date().getMilliseconds(); //get current time
	var arrayIndex = time % 15; // get the array index value < 15
	document.getElementById("tips1").innerHTML = healthArray[arrayIndex++]; // replace the p element news 
	if (arrayIndex == 15) {
	    arrayIndex = 0
	} 
	document.getElementById("tips2").innerHTML = healthArray[arrayIndex++]; // replace the p element news 
        if (arrayIndex == 15) {
	    arrayIndex = 0
	} 								      								      
	document.getElementById("tips3").innerHTML = healthArray[arrayIndex++]; // replace the p element news 
        if (arrayIndex == 15) {
	    arrayIndex = 0
	} 								      								      
      	document.getElementById("tips4").innerHTML = healthArray[arrayIndex++]; // replace the p element news 
        if (arrayIndex == 15) {
	    arrayIndex = 0
	} 								      								      
	document.getElementById("tips5").innerHTML = healthArray[arrayIndex++]; // replace the p element news 

}
								      				      
</script>