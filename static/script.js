async function checkRank() {
  let keyword = document.getElementById("keyword").value;
  let domain = document.getElementById("domain").value;
  let location = document.getElementById("location").value;
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
    console.log("Error:", error);
  }
}