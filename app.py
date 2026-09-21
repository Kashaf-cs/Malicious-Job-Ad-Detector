from flask import Flask, render_template, request, jsonify
from utils.predictor import predict_job

app = Flask(__name__)

# Main Route - HTML UI display karne ke liye
@app.route('/')
def home():
    return render_template('index.html')

# API Route - Frontend se prediction request handle karne ke liye
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        job_description = data.get('job_description', '')

        if not job_description.strip():
            return jsonify({'error': 'Please enter a job description first.'}), 400

        # utils/predictor.py se model result fetch karna
        result = predict_job(job_description)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
  if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)