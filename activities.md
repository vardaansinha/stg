
<h1>Breaking News!!</h1>
<br/>

<table  style="width:100%" id = "table">
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


//fetch("http://172.23.68.4:8086/api/breakingnews/", requestOptions)
fetch("http://localhost:8086/api/breakingnews/", requestOptions)
  .then(response => response.json())
  .then(r => {
    r.forEach(ev => {
      const row = document.createElement("tr")
      const cityData = document.createElement("td")
      cityData.innerHTML = `${ev.city}`
      row.appendChild(cityData)

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

function reset() {
  window.location.reload();
}

</script>
		


