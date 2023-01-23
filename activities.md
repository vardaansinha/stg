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
<button name="button" onclick="getNews()" >Get the latest news!!!</button>

<br/>

- <p class="news2_style" id="news1">Click the above button to generate news.</p>
- <p class="news2_style" id="news2"></p>
- <p  class="news2_style" id="news3"></p>
- <p class="news2_style" id="news4"></p>
- <p  class="news2_style" id="news5"></p>

<script>
// Array of 15 news
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
"Woman dies after thrown from horse at Florida rodeo",
"Dog rescued from frozen Quebec lake",
"DeSantis activates National Guard amid increase of migrant landings on Florida Keys",
"Amid unrest, Iran's hardliners turn their anger to France",
"Filipino Catholics hold big procession after pandemic eases",	
	
];
								       
// this function is called upon button click
function getNews() {
	var time = new Date().getMilliseconds(); //get current time
	var arrayIndex = time % 15; // get the arrray index value < 15
	document.getElementById("news1").innerHTML = newsArray[arrayIndex++]; // replace the p element news 
	if (arrayIndex == 15) {
	    arrayIndex = 0
	} 
	document.getElementById("news2").innerHTML = newsArray[arrayIndex++]; // replace the p element news 
        if (arrayIndex == 15) {
	    arrayIndex = 0
	} 								      								      
	document.getElementById("news3").innerHTML = newsArray[arrayIndex++]; // replace the p element news 
        if (arrayIndex == 15) {
	    arrayIndex = 0
	} 								      								      
      	document.getElementById("news4").innerHTML = newsArray[arrayIndex++]; // replace the p element news 
        if (arrayIndex == 15) {
	    arrayIndex = 0
	} 								      								      
	document.getElementById("news5").innerHTML = newsArray[arrayIndex++]; // replace the p element news 

}
</script>
	
	
<br/>
<br/>
<br/>

## Click below for latest US Police Chase News 
![](images/chase1.jpg)
<a href="https://twitter.com/pcalive">US Police Chase News</a> 
<br/>
<br/>
<br/>	
## Click below for latest San Diego Police Capture News 
![](images/sdpd.jpg)
<a href="https://twitter.com/SanDiegoPD?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor">San Diego Police Capture News </a> 

<br/><br/><br/>
##  Signup for weekly Newsletter 
<br/>
<table>
  <thead>
  <tr>
    <th>Name</th>
    <th>ID</th>
    <th>Actions</th>
  </tr>
  </thead>
  <tbody id="table">
    <!-- javascript generated data -->
  </tbody>
</table>

<br/>
##  Enter your Name and ID: 

<table>
    <tr>
        <th><label for="name">Name</label></th>
        <th><label for="email">ID</label></th>
        <th><label for="password">Password</label></th>
        <th><label for="phone">Phone</label></th>
    </tr>
    <tr>
        <td><input type="text" name="name" id="name" required></td>
        <td><input type="email" name="email" id="email" placeholder="abc@xyz.org" required></td>
        <td ><button onclick="createUser()">Create</button></td>
    </tr>
</table>

<script>

// Static json, this can be used to test data prior to API and Mo
jsonStr = '[{"_name": "Bolsonaro supporters storm Brazilian Congress.", "_uid": "CNN"}, {"_name": "Kevin McCarthy is new speaker", "_uid": "Fox"}, {"_name": "Woman sentenced to three years in state prison for collecting $400,000 in viral GoFundMe scam", "_uid": "ABC"}, {"_name": "Ukraine denies Russian claim it killed 600 soldiers", "_uid": "NBC"}, {"_name": "Damar Hamlin: Buffalo Bills make stirring display in support of safety during victory", "_uid": "BBC"}]';
	
glob = 1;

function createUser() {
var Table = document.getElementById("table");
Table.innerHTML = "";

    name = document.getElementById("name").value;
    email = document.getElementById("email").value;

    // Convert JSON string to JSON object
    data = JSON.parse(jsonStr);
    
    //str = 
    //TO push new element
    //data.push({"_name": "Thomas3", "_uid": "t8test"});
    data.push({ "_name" : name, "_uid": email});
    
    jsonStr = JSON.stringify(data);
    
    
    //data = JSON.parse(jsonStr);
    //showRows(data);
    showTable();

}
    
function showRows(data) {
// prepare HTML result container for new output
    const table = document.getElementById("table");
    
    data.forEach(user => {
    // build a row for each user
    const tr = document.createElement("tr");

    // td's to build out each column of data
    const name = document.createElement("td");
    const id = document.createElement("td");
    const action = document.createElement("td");
           
    // add content from user data          
    name.innerHTML = user._name; 
    id.innerHTML = user._uid; 

    // add action for update button
    var updateBtn = document.createElement('input');
    updateBtn.type = "button";
    updateBtn.className = "button";
    updateBtn.value = "Update";
    updateBtn.style = "margin-right:16px";
    updateBtn.onclick = function () {
      alert("Update: " + user._uid);
    };
    action.appendChild(updateBtn);

    // add action for delete button
    var deleteBtn = document.createElement('input');
    deleteBtn.type = "button";
    deleteBtn.className = "button";
    deleteBtn.value = "Delete";
    deleteBtn.style = "margin-right:16px"
    deleteBtn.onclick = function () {
      alert("Delete: " + user._uid);
    };
    action.appendChild(deleteBtn);  

    // add data to row
    tr.appendChild(name);
    tr.appendChild(id);
    tr.appendChild(action);

    // add row to table
    table.appendChild(tr);
  });
    
}

function showTable() {

    // Convert JSON string to JSON object
    data1 = JSON.parse(jsonStr);
    
    strName = "_name"
    strNameValue = "nameName"
    strUser = "_uid"
    strUserValue = "uidValue" + glob
    
    //data.push({ "_name" : strNameValue, "_uid": strUserValue});
    //TO push new element
    //data.push({"_name": "Thomas3", "_uid": "t8"});
    //jsonStr = JSON.stringify(data);
    
    //data = JSON.parse(jsonStr);
    showRows(data1);
}

showTable();
</script>


