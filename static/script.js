async function checkRank() {
  let keyword = document.getElementById("keyword").value.trim();
  let domain = document.getElementById("domain").value.trim();
  let location = document.getElementById("location").value;

  // ❗ Validation
  if (!keyword || !domain) {
    alert("Enter keyword & domain");
    return;
  }

  // 🔥 DOMAIN CLEAN (IMPORTANT)
  domain = domain
    .replace("https://", "")
    .replace("http://", "")
    .replace("www.", "")
    .replace("/", "")
    .toLowerCase();

  document.getElementById("result").innerText = "Checking...";

  try {
    let res = await fetch(
      `/api/rank?keyword=${encodeURIComponent(keyword)}&domain=${encodeURIComponent(domain)}&location=${encodeURIComponent(location)}`
    );

    let data = await res.json();

    // 🧠 SAFE OUTPUT
    if (data.rank) {
      document.getElementById("result").innerText = "Rank: " + data.rank;
    } else {
      document.getElementById("result").innerText = "Rank: Not found";
    }

  } catch (error) {
    console.error(error);
    document.getElementById("result").innerText = "Error fetching data";
  }
}