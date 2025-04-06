<script>
  document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault(); // Prevent form from reloading the page

    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    if (!file) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const resultDiv = document.getElementById("result");
    resultDiv.innerText = "Analyzing..."; // Optional: show loading

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        body: formData
      });
      
      

      if (!response.ok) {
        throw new Error("Prediction failed");
      }

      const result = await response.json();
      resultDiv.innerText = `🧠 Result: ${result.result.toUpperCase()}`; // Show result in uppercase
    } catch (error) {
      console.error("Error:", error);
      resultDiv.innerText = "❌ Error during prediction.";
    }
  });
  document.getElementById("predict-btn").addEventListener("click", function () {
        const audio = new Audio("glitch-sound.mp3");
        audio.play().catch(err => {
            console.log("Sound error:", err);
        });
      });
</script>
