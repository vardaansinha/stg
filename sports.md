# Sports

<html>
<body>

<table style="width:100%" id="table">
  <tr>
    <th>Check for your Favorite NFL Team! Your favorite team's statistics will show the number of games they have played, their overall regular season record, and different statistics about the number of points they have scored and allowed. The last column shows if your team made the playoffs!</th>
  </tr>
</table>


<script>

var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("http://192.168.68.53:8086/api/nflteam", requestOptions)
  .then(response => response.json())
  .then(r => {
	  r.forEach(ev => {
		  const row = document.createElement("tr")
		  const data = document.createElement("td")
		  data.innerHTML = `${ev.team}, ${ev.division}: ${ev.gamesplayed} and ${ev.gameswon}-${ev.gameslost}: ${ev.gamesdrawn}, ${ev.gamesplayedathome}, ${ev.gamesplayedaway}, ${ev.gameswonathome}, ${ev.gameslostathome}, ${ev.gameswonaway}, ${ev.gamesplayed5}, ${ev.gameslost5}, ${ev.pointsfor}, ${ev.pointsagainst}, ${ev.playoffs}: Playoff Berth`
		  row.appendChild(data)
		  document.getElementById("table").appendChild(row)
	  })
  })
  .catch(error => console.log('error', error));

function reset() {
  window.location.reload();
}

</script>

<script>

const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
const url = "http://localhost:8086/api/nflteam"
  //const url = "https://flask.nighthawkcodingsociety.com/api/users"
const create_fetch = url + '/create';
const read_fetch = url + '/';
read_users();

function read_users() {
    // prepare fetch options
    const read_options = {
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'omit', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
      },
    };     // fetch the data from API
    fetch(read_fetch, read_options)
      // response is a RESTful "promise" on any successful fetch
      .then(response => {
        // check for response errors
        if (response.status !== 200) {
            const errorMsg = 'Database read error: ' + response.status;
            console.log(errorMsg);
            const tr = document.createElement("tr");
            const td = document.createElement("td");
            td.innerHTML = errorMsg;
            tr.appendChild(td);
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
      resultContainer.appendChild(tr);
    });
  }
</script>