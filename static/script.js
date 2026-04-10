async function loadCities() {
  let country = document.getElementById("country").value;

  // country code fix
  let countryCode = country === "United States" ? "us" : "ca";

  try {
    let res = await fetch(
      `https://api.geoapify.com/v1/geocode/autocomplete?text=&filter=countrycode:${countryCode}&type=city&limit=20&apiKey=9b035938a53443d4bf651c7a47f607a1`
    );

    let data = await res.json();

    let citySelect = document.getElementById("city");
    citySelect.innerHTML = "";

    if (!data.features || data.features.length === 0) {
      let option = document.createElement("option");
      option.text = "No cities found";
      citySelect.appendChild(option);
      return;
    }

    data.features.forEach(place => {
      let city = place.properties.city || place.properties.name || "";
      let state = place.properties.state || "";

      if (!city) return;

      let option = document.createElement("option");
      option.value = `${city}, ${state}`;
      option.text = `${city}, ${state}`;

      citySelect.appendChild(option);
    });

  } catch (error) {
    console.log("Error loading cities:", error);
  }
}


async function checkRank() {
  let keyword = document.getElementById("keyword").value;
  let domain = document.getElementById("domain").value;
  let location = document.getElementById("city").value;
  let device = document.getElementById("device").value;

  if (!keyword || !domain) {
    alert("Enter keyword & domain");
    return;
  }

  try {
    let res = await fetch(`/api/rank?keyword=${keyword}&domain=${domain}&location=${location}&device=${device}`);
    let data = await res.json();

    document.getElementById("result").innerText = "Rank: " + data.rank;
    document.getElementById("usage").innerText = "Monthly Usage: " + data.usage;

  } catch (error) {
    console.log("Error fetching rank:", error);
  }
}


// page load pe auto run
window.onload = loadCities;