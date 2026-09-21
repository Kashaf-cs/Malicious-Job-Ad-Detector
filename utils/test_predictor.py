from utils.predictor import predict_job
from utils.predictor import model

print("MODEL CLASSES:", model.classes_)


# Test 1: Suspicious job
fake_job = """
URGENT HIRING!

Work from home.

No experience required.

Earn $5000 weekly.

Immediate joining.

Limited positions available.

Click the link below to claim your job.

No interview required.
"""


# Test 2: Normal job
real_job = """
Software Engineer

We are looking for a Software Engineer with experience
in Python, SQL and Django.

Candidates should have excellent communication skills.

Medical insurance and annual bonus will be provided.
"""


# Test fake job
print("TEST 1: Suspicious Job")
print("-----------------------")

result1 = predict_job(fake_job)

print("Prediction:", result1["prediction"])
print("Fake Probability:", round(result1["fake_probability"], 2), "%")
print("Risk Indicators:")

for indicator in result1["risk_indicators"]:
    print("-", indicator)


# Test real job
print("\nTEST 2: Normal Job")
print("------------------")

result2 = predict_job(real_job)

print("Prediction:", result2["prediction"])
print("Fake Probability:", round(result2["fake_probability"], 2), "%")
print("Risk Indicators:")

if result2["risk_indicators"]:
    for indicator in result2["risk_indicators"]:
        print("-", indicator)
else:
    print("- No major suspicious patterns detected")