async function checkRank() {
  const keyword = document.getElementById("keyword").value.trim();
  const location = document.getElementById("location").value;
  let domain = document.getElementById("domain").value.trim();

  if (!keyword || !domain) {
    alert("Keyword aur domain dono bharo");
    return;
  }

  domain = domain.replace("https://","").replace("http://","").replace("www.","").replace("/","").toLowerCase();

  document.getElementById("result").innerHTML = "Checking...";

  try {
    const res = await fetch(`/api/rank?keyword=${encodeURIComponent(keyword)}&domain=${encodeURIComponent(domain)}&location=${encodeURIComponent(location)}`);
    const data = await res.json();

    if (data.rank === "Not found") {
      document.getElementById("result").innerHTML = `<span class="notfound">Not found in top 100</span>`;
    } else if (data.rank === "Error") {
      document.getElementById("result").innerHTML = `<span class="error">Error: ${data.error}</span>`;
    } else {
      document.getElementById("result").innerHTML = `<span class="rank">Rank: ${data.rank}</span><span class="type">${data.type}</span>`;
    }
  } catch (e) {
    document.getElementById("result").innerHTML = `<span class="error">Something went wrong</span>`;
  }
}