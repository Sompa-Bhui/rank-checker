const cities = {
  us: [
    "New York, United States",
    "Los Angeles, United States",
    "Miami, United States"
  ],
  ca: [
    "Toronto, Canada",
    "Vancouver, Canada",
    "Montreal, Canada"
  ]
};

function updateCities() {
  let country = document.getElementById("country").value;
  let citySelect = document.getElementById("city");

  citySelect.innerHTML = "";

  cities[country].forEach(city => {
    let option = document.createElement("option");
    option.value = city;
    option.text = city;
    citySelect.appendChild(option);
  });
}

async function checkRank() {
  let keyword = document.getElementById("keyword").value;
  let domain = document.getElementById("domain").value;
  let country = document.getElementById("country").value;
  let location = document.getElementById("city").value;
  let device = document.getElementById("device").value;

  let res = await fetch(`/api/rank?keyword=${keyword}&domain=${domain}&country=${country}&location=${location}&device=${device}`);
  let data = await res.json();

  document.getElementById("result").innerText = "Rank: " + data.rank;
  document.getElementById("usage").innerText = "Monthly Usage: " + data.usage;
}

updateCities();