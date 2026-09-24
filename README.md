<div align="center">

# 🛡️ Malicious Job-Ad Detector

### A Job Verification Tool — *Apply with confidence, verify first.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![NLTK](https://img.shields.io/badge/NLTK-154F5B?style=for-the-badge&logo=python&logoColor=white)](https://www.nltk.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)

</div>

---

## 📌 Overview

Fake job postings cost job seekers money, personal data and trust.

This project is a **Job Verification Tool** built with **Machine Learning and Natural Language Processing**. Paste any job description and check it **before you apply**.

> ✅ **Real Job**: go ahead and apply.
> ❌ **Fake Job**: you just saved yourself.

---

## 🎯 Key Features

* **ML-Based Detection:** Logistic Regression classifier trained on TF-IDF features.
* **Risk Analyzer:** Rule-based engine that flags suspicious patterns in job postings.
* **Red Flag Detection:** Identifies unrealistic salaries, urgent hiring language and payment requests.
* **Confidence Score:** Returns a fake probability percentage for every prediction.
* **NLP Preprocessing:** Text cleaning, stopword removal and lemmatization using NLTK.
* **Web Interface:** Clean, responsive Flask UI for real-time job verification.

---

## 🚩 Red Flags Detected

| Indicator | Example |
|-----------|---------|
| 💰 Unrealistic Salary | *"Earn $5000 weekly"* |
| 🚫 No Experience Required | *"No experience needed"* |
| ⏰ Urgent Hiring Language | *"URGENT! Limited positions"* |
| 💳 Payment Requests | *"Pay registration fee"* |
| 📱 Suspicious Contacts | *"Contact on Telegram/WhatsApp"* |
| 🎣 Too-Good-To-Be-True | *"Guaranteed income"* |

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **ML & NLP:** Scikit-learn, NLTK, TF-IDF Vectorizer
* **Backend:** Flask
* **Frontend:** HTML, CSS, JavaScript
* **Libraries:** NumPy, Joblib, Regex
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
Malicious-Job-Ad-Detector/
│
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── fake_job_detector_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── utils/
│   ├── predictor.py
│   ├── preprocessing.py
│   └── risk_analyzer.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    ├── script.js
    └── screenshots/
        ├── homepage.png
        ├── fake-result.png
        └── real-result.png
```

---

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/Kashaf-cs/Malicious-Job-Ad-Detector.git
cd Malicious-Job-Ad-Detector
```

**2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

**3. Install requirements**

```bash
pip install -r requirements.txt
```

**4. Download NLTK data**

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

**5. Run the application**

```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000**

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | XX% |
| Precision | XX% |
| Recall | XX% |
| F1-Score | XX% |

*Dataset: [name and source of your dataset]*

---

## ⚠️ Limitations

* The model reads text only. It cannot confirm that a company or recruiter really exists.
* A low risk score does not guarantee a job is safe. Always research the employer yourself.

---

## 🔮 Future Improvements

- [ ] Browser extension for LinkedIn / Indeed / Rozee.pk
- [ ] WhatsApp bot for instant job checks
- [ ] Deep learning upgrade (BERT / LSTM)
- [ ] Urdu language support
- [ ] Cloud deployment (Render / AWS)
- [ ] User feedback loop for continuous retraining

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

This project is distributed under the MIT License.

## 👩‍💻 Connect With Me

<div align="center">

**Kashaf Rasheed** — BS Computer Science, LCWU '28

[![GitHub](https://img.shields.io/badge/GitHub-Kashaf--cs-181717?style=for-the-badge&logo=github)](https://github.com/Kashaf-cs)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/kashaf-rasheed-694a11416/)

⭐ **If you found this useful, drop a star!**

</div>
