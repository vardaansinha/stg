<!--- This section is Cascading Style Sheet (CSS) and applies to HTML -->
<style>
/* "row style" is flexible size and aligns pictures in center */
.row {
  align-items: center;
  display: flex;
}
#map {
      height: 700px; /* The height is 400 pixels */
      width: 150%; /* The width is the width of the web page */
}

/* "column style" is one-third of the width with padding */
.column {
  flex: 33.33%;
  padding: 5px;
}
</style>


<!-- Hide maps for now

## Breaking News with Maps API
<div id="map"></div>

<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyChhAisKAHMljl0nrnmCOL4zm0Ek6KlK2U&callback=initMap&v=weekly" defer></script>
-->

<script>                              
      // Initialize and add the map
      function initMap() {
        // The location of Borrego Springs
        var sd = { lat: 33.1005, lng: -116.3013 };
        // The map, centered at Uluru
        var map = new google.maps.Map(document.getElementById("map"), {
          zoom: 9,
          center: sd,
        });
           // Array of markers 
        var markers = [
          {
          coords : {lat: 32.7157, lng: -117.1611}, 
          content: '<a style="color:blue;" href="https://www.cbs8.com/article/news/local/padres-fanfest-mayhem-crowded-concourses-and-delayed-entry/509-543c588b-0eba-4c95-bb84-b3538894dd77">Padres FanFest mayhem: Long lines, crowded concourses, and delayed entry</a>' 
          },
          {
          coords : {lat: 33.4934, lng: -117.1488}, 
          content: '<a style="color:blue;" href="https://fox5sandiego.com/news/local-news/forklift-stolen-from-oceanside-home-depot-in-broad-daylight/">Forklifts Stolen From Home Depot</a>'  
          }, 
          {
          coords : {lat: 33.6846, lng: -117.8265}, 
          content: '<a style="color:blue;" href="https://www.usatoday.com/story/sports/ncaab/2023/02/05/long-beach-state-beats-uc-irvine-in-ot-for-6th-straight-win/51256357/">Long Beach State beats UC Irvine in OT</a> '  
          }, 
          {  
          coords : {lat: 32.7920, lng: -115.5631}, 
          content: '<a style="color:blue;" href="https://calexicochronicle.com/2022/12/30/el-centro-hosts-dog-park-groundbreaking/"> El Centro Hosts Dog Park Groundbreaking</a>'  
          }, 
          {
          coords : {lat: 33.8734, lng: -115.9010}, 
          content: '<a style="color:blue;" href="https://www.nationalparkstraveler.org/2023/02/backpacking-permits-joshua-tree-national-park-available-online">Backpacking Permits For Joshua Tree National Park Available Online</a>'  
          },
          {
          coords : {lat: 33.1192, lng: -117.0864}, 
          content: '<a style="color:blue;" href="https://thecoastnews.com/escondido-council-appoints-palomar-college-trustee-to-vacant-seat/">Escondido council appoints Palomar College trustee to vacant seat</a>'  
          },
          {
          coords : {lat: 33.3286, lng: -115.8434}, 
          content: '<a style="color:blue;" href="https://www.theguardian.com/us-news/2022/nov/29/us-spend-250m-cleanup-california-toxic-salton-sea">US to spend $250m on cleanup at California’s toxic Salton Sea</a>'  
          },
	
        ];
      
        // Loop through markers 
        for(var i = 0; i < markers.length; i++) { 
          addMarker(markers[i]); 
        }
                                          
        // Add Marker Function 
        function addMarker(props){ 
          var marker =  new google.maps.Marker({ 
            position:props.coords, 
            map:map, 
          });
          // Check content 
          if(props.content) { 
               var infoWindow = new google.maps.InfoWindow({ 
              content:props.content 
               });
            infoWindow.open(map, marker);//display by default
            marker.addListener( 'click', function(){ 
              infoWindow.open(map, marker); 
            });
          }
        }                                          
      }
      
      // Hide Google Maps for now
      //window.initMap = initMap;
</script>
<br/>

<h1>Breaking News!!</h1>
<br/>
<table id = "table">
  <thead>
  <tr>
    <th>City</th>
    <th>Network</th>
    <th>News</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>

<script>

var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("http://172.25.57.176:8086/api/breakingnews/", requestOptions)
  .then(response => response.json())
  .then(r => {
	r.forEach(ev => {
		const row = document.createElement("tr")
		const cityData = document.createElement("td")
		//cityData.innerHTML = `${ev.city}, ${ev.day}, ${ev.network}, ${ev.title}, ${ev.link}`
    cityData.innerHTML = `${ev.city}`
		row.appendChild(cityData)

  /*
    const dayData = document.createElement("td")
		dayData.innerHTML = `${ev.day}`
		row.appendChild(dayData)
  */

    const networkData = document.createElement("td")
		networkData.innerHTML = `${ev.network}`
		row.appendChild(networkData)

    const titleData = document.createElement("td")
		titleData.innerHTML = `<a href=${ev.link}> ${ev.title} </a>`
		row.appendChild(titleData)

		document.getElementById("table").appendChild(row)
	})
  })
  .catch(error => console.log('error', error))


  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
  const url = "http://localhost:8086/api/breakingnews"
  //const url = "https://flask.nighthawkcodingsociety.com/api/users"
  const create_fetch = url + '/create';
  const read_fetch = url + '/';

  // Load users on page entry
  //read_users();


  // Display User Table, data is fetched from Backend Database
  function read_users() {
    // prepare fetch options
    const read_options = {
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
      mode: 'no-cors', // no-cors, *cors, same-origin
      cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'omit', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
      },
    };

    // fetch the data from API
    fetch(read_fetch, read_options)
      // response is a RESTful "promise" on any successful fetch
      .then(response => {
        // check for response errors
        if (response.status == 205) {
            const errorMsg = 'Database read error: ' + response.status;
            console.log(errorMsg);
            const tr = document.createElement("tr");
            const td = document.createElement("td");
            td.innerHTML = errorMsg;
            tr.appendChild(td);
            resultContainer.appendChild(tr);
            return;
        }
        // valid response will have json data
        response.json().then(data => {
            console.log(data);
            for (let row in data) {
              console.log(data[row]);
              add_row(data[row]);
            }
        })
    })
    // catch fetch errors (ie ACCESS to server blocked)
    .catch(err => {
      console.error(err);
      const tr = document.createElement("tr");
      const td = document.createElement("td");
      td.innerHTML = err;
      tr.appendChild(td);
      //resultContainer.appendChild(tr);
    });
  }

  function add_row(data) {
    const tr = document.createElement("tr");
    const city = document.createElement("td");
    const day = document.createElement("td");
    const network = document.createElement("td")
    const title = document.createElement("td");
    const link = document.createElement("td");
  

    // obtain data that is specific to the API
    city.innerHTML = data.city; 
    day.innerHTML = data.day; 
    network.innerHTML = data.network;
    title.innerHTML = data.title; 
    link.innerHTML = data.link; 

    // add HTML to container
    tr.appendChild(city);
    tr.appendChild(day);
    tr.appendChild(network);
    tr.appendChild(title);
    tr.appendChild(link);

    resultContainer.appendChild(tr);
  }

</script>
		
<br/>
<br/>	
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
<a href="https://twitter.com/pcalive">US Police Chase News</a> 
<br/>
<br/>
<br/>	
## Click below for latest San Diego Police Capture News 
<a href="https://twitter.com/SanDiegoPD?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor">San Diego Police Capture News </a> 

<br/><br/><br/>
##  Signup for more Breaking News 
<br/>
<table>
  <thead>
  <tr>
    <th>News</th>
    <th>Network</th>
    <th>Actions</th>
  </tr>
  </thead>
  <tbody id="tableCreate">
    <!-- javascript generated data -->
  </tbody>
</table>

<br/>
##  Add Breaking News and Network Details: 

<table>
    <tr>
        <th><label for="name">Breaking News</label></th>
        <th><label for="email">Network</label></th>
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
var Table = document.getElementById("tableCreate");
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
    const table = document.getElementById("tableCreate");
    
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


