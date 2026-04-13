async function checkRank() {
  let keyword = document.getElementById("keyword").value;
  let domain = document.getElementById("domain").value;
  let location = document.getElementById("location").value;

  if (!keyword || !domain) {
    alert("Enter keyword & domain");
    return;
  }

  document.getElementById("result").innerText = "Checking...";

  try {
    let res = await fetch(`/api/rank?keyword=${keyword}&domain=${domain}&location=${location}`);
    let data = await res.json();

    document.getElementById("result").innerText = "Rank: " + data.rank;

  } catch (error) {
    document.getElementById("result").innerText = "Error";
  }
}