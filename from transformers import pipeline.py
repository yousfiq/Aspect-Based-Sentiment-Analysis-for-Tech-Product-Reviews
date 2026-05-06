from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

reviews = [
    "The laptop’s performance is excellent, but the battery drains too quickly.",
    "Customer support was very helpful and solved my issue fast.",
    "The design is sleek, but the screen brightness is disappointing.",
    "Battery life is amazing, but performance lags when multitasking."
]

aspects = ["performance", "battery", "customer support", "design", "screen"]

def analyze_reviews(reviews, aspects):
    results = []
    for review in reviews:
        aspect_sentiments = {}
        for aspect in aspects:
            text = f"{aspect}: {review}"
            sentiment = sentiment_analyzer(text)[0]
            aspect_sentiments[aspect] = sentiment
        results.append({"review": review, "analysis": aspect_sentiments})
    return results

analysis_results = analyze_reviews(reviews, aspects)

for result in analysis_results:
    print("Review:", result["review"])
    for aspect, sentiment in result["analysis"].items():
        print(f"  {aspect}: {sentiment['label']} ({sentiment['score']:.2f})")
    print()