async function loadCities() {
  let country = document.getElementById("country").value;

  let res = await fetch(`https://api.geoapify.com/v1/geocode/autocomplete?text=${country}&type=city&limit=10&apiKey=9b035938a53443d4bf651c7a47f607a1`);
  let data = await res.json();

  let citySelect = document.getElementById("city");
  citySelect.innerHTML = "";

  data.features.forEach(place => {
    let option = document.createElement("option");
    option.value = place.properties.formatted;
    option.text = place.properties.formatted;
    citySelect.appendChild(option);
  });
}

async function checkRank() {
  let keyword = document.getElementById("keyword").value;
  let domain = document.getElementById("domain").value;
  let location = document.getElementById("city").value;
  let device = document.getElementById("device").value;

  let res = await fetch(`/api/rank?keyword=${keyword}&domain=${domain}&location=${location}&device=${device}`);
  let data = await res.json();

  document.getElementById("result").innerText = "Rank: " + data.rank;
  document.getElementById("usage").innerText = "Monthly Usage: " + data.usage;
}

loadCities();