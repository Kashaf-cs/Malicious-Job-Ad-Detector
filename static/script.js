function scrollToSection(sectionId) {
    const target = document.getElementById(sectionId);

    if (target) {
        target.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
}

document.addEventListener("DOMContentLoaded", () => {

    const jobForm = document.getElementById("job-form");
    const resultsWrapper = document.getElementById("results-wrapper");

    if (jobForm) {

        jobForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const title = document.getElementById("job-title").value;
            const description = document.getElementById("job-description").value;
            const analyzeBtn = document.getElementById("analyze-btn");

            // Disable button while analyzing
            analyzeBtn.disabled = true;
            analyzeBtn.innerText = "⏳ Analyzing Job Posting...";

            try {

                // Send job description to Flask
                const response = await fetch("/predict", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        job_description: description
                    })
                });

                const data = await response.json();

                // Check if Flask returned an error
                if (!response.ok) {
                    throw new Error(
                        data.error || "Prediction failed."
                    );
                }

                // -----------------------------
                // Display Model Prediction
                // -----------------------------

                document.getElementById("model-output").innerText =
                    data.prediction || "N/A";

                // Display Fake Probability
                document.getElementById("risk-score-text").innerText =
                    (data.fake_probability || 0).toFixed(2) + "%";

                // Display number of risk indicators
                document.getElementById("risk-count").innerText =
                    data.risk_indicators
                        ? data.risk_indicators.length
                        : 0;

                // -----------------------------
                // Display Risk Indicators
                // -----------------------------

                const riskList =
                    document.getElementById("risk-list");

                riskList.innerHTML = "";

                if (
                    data.risk_indicators &&
                    data.risk_indicators.length > 0
                ) {

                    data.risk_indicators.forEach(flag => {

                        const item =
                            document.createElement("div");

                        item.className = "risk-item";

                        item.innerText = "⚠️ " + flag;

                        riskList.appendChild(item);
                    });

                } else {

                    riskList.innerHTML =
                        "<p style='color:#8EB69B; font-size:14px;'>" +
                        "No high-risk indicators detected." +
                        "</p>";
                }

                // Show results section
                resultsWrapper.classList.remove("hidden");

                // Scroll to results
                scrollToSection("results-wrapper");

            } catch (err) {

                console.error("Prediction Error:", err);

                alert(
                    err.message ||
                    "Error connecting to server."
                );

            } finally {

                // Enable button again
                analyzeBtn.disabled = false;
                analyzeBtn.innerText =
                    "🔍 Analyze Job Posting";
            }
        });
    }


    // -----------------------------
    // Star Rating Interactivity
    // -----------------------------

    const stars = document.querySelectorAll(".star");

    stars.forEach(star => {

        star.addEventListener("click", function () {

            const val =
                parseInt(
                    this.getAttribute("data-value")
                );

            stars.forEach((s, idx) => {

                if (idx < val) {
                    s.classList.add("active");
                } else {
                    s.classList.remove("active");
                }

            });
        });
    });

});
/* ================================
   SCROLL REVEAL ANIMATION
   ================================ */

function revealOnScroll() {
    const reveals = document.querySelectorAll('.reveal');

    reveals.forEach((element) => {
        const windowHeight = window.innerHeight;
        const elementTop = element.getBoundingClientRect().top;
        const revealPoint = 150;

        if (elementTop < windowHeight - revealPoint) {
            element.classList.add('active');
        } else {
            element.classList.remove('active');
        }
    });
}

window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);