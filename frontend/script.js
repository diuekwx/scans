const form = document.getElementById("search-form");
const input = document.getElementById("search-input");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = input.value.trim();
  if (!title) return;

  resultsDiv.textContent = "Searching...";

  try {
    const response = await fetch("http://localhost:8000/series/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ title })
    });

    const data = await response.json();
    resultsDiv.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    console.error(err);
    resultsDiv.textContent = "Error fetching results.";
  }
});
