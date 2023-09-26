from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_review = request.form.get('review')  # Assuming the textarea has a 'name' attribute of 'review'

    # Call your sentiment analysis code from SentimentAnalysisOnRestaurantReview.ipynb
    # Replace the following lines with your actual analysis code
    sentiment = "Positive"  # Replace with your sentiment analysis result
    #confidence = "High"  # Replace with your confidence score
    accuracy = "76.5%"  # Replace with your accuracy score

    return render_template('index.html', sentiment=sentiment, confidence=confidence, accuracy=accuracy)

if __name__ == '__main__':
    app.run(debug=True)
