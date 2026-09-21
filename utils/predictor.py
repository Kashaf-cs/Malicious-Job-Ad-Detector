import joblib

from utils.preprocessing import preprocess_text
from utils.risk_analyzer import analyze_risk


# -----------------------------------------
# Load trained ML model
# -----------------------------------------

model = joblib.load(
    "models/fake_job_detector_model.pkl"
)


# -----------------------------------------
# Load TF-IDF vectorizer
# -----------------------------------------

tfidf = joblib.load(
    "models/tfidf_vectorizer.pkl"
)


def predict_job(job_text):

    # -----------------------------------------
    # Step 1: Validate input
    # -----------------------------------------

    if not job_text or not job_text.strip():
        raise ValueError(
            "Job description cannot be empty."
        )


    # -----------------------------------------
    # Step 2: Preprocess job description
    # -----------------------------------------

    cleaned_text = preprocess_text(job_text)


    # -----------------------------------------
    # Step 3: Convert text into TF-IDF features
    # -----------------------------------------

    text_vector = tfidf.transform(
        [cleaned_text]
    )


    # -----------------------------------------
    # Step 4: Make ML prediction
    # -----------------------------------------

    prediction = model.predict(
        text_vector
    )[0]


    # -----------------------------------------
    # Step 5: Get prediction probabilities
    # -----------------------------------------

    probabilities = model.predict_proba(
        text_vector
    )[0]


    # -----------------------------------------
    # Step 6: Find Fake class probability
    # -----------------------------------------

    if 1 in model.classes_:

        fake_class_index = list(
            model.classes_
        ).index(1)

        fake_probability = (
            probabilities[fake_class_index] * 100
        )

    else:

        fake_probability = 0.0


    # -----------------------------------------
    # Step 7: Convert prediction to readable text
    # -----------------------------------------

    if prediction == 1:

        result = "Fake Job Posting"

    else:

        result = "Real Job Posting"


    # -----------------------------------------
    # Step 8: Analyze suspicious indicators
    # -----------------------------------------

    risk_indicators = analyze_risk(
        job_text
    )


    # -----------------------------------------
    # Step 9: Return results to Flask
    # -----------------------------------------

    return {

        "prediction": result,

        "fake_probability": round(
            float(fake_probability),
            2
        ),

        "risk_indicators": risk_indicators

    }