<!--- This section is Cascading Style Sheet (CSS) and applies to HTML -->
<style>
/* "row style" is flexible size and aligns pictures in center */
.row {
  align-items: center;
  display: flex;
}

/* "column style" is one-third of the width with padding */
.column {
  flex: 33.33%;
  padding: 5px;
}
</style>
## Breaking News
> Click below to refresh News.

<br/>
<button name="button" onclick="getNews()" >Get the news!!!</button>

<br/>
Top News:  
<p class="news2_style" id="news1">Click the above button to generate news.</p>
<p class="news2_style" id="news2"></p>
<p id="news3"></p>

<script>
// Array of 10 news
var newsArray = [
"Bolsonaro supporters storm Brazilian Congress.",
"Kevin McCarthy is new speaker",
"Woman sentenced to three years in state prison for collecting $400,000 in viral GoFundMe scam",
"Ukraine denies Russian claim it killed 600 soldiers",
"Damar Hamlin: Buffalo Bills make stirring display in support of safety during victory",
"Worshippers in Tokyo plunge into ice bath to mark new year",
"Driver crashes and flips vehicle inside drive-through car wash",
"Brazilian police fire tear gas at Bolsonaro supporters",
"Deer rescued from frozen river in Wisconsin",
"Two years after Covid food still tastes rotten",
];
								       
// this function is called upon button click
function getNews() {
	var time = new Date().getMilliseconds(); //get current time
	var arrayIndex = time % 10; // get the arrray index value < 10
	document.getElementById("news1").innerHTML = newsArray[arrayIndex++]; // replace the p element news 
	if (arrayIndex == 10) {
	    arrayIndex = 0
	} 
	document.getElementById("news2").innerHTML = newsArray[arrayIndex++]; // replace the p element news 
	document.getElementById("news3").innerHTML = newsArray[arrayIndex++]; // replace the p element news 
}
</script>
