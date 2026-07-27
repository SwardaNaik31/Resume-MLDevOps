sample_resume = """
Python SQL Machine Learning Deep Learning
Pandas NumPy TensorFlow
"""

sample = vectorizer.transform([sample_resume])

prediction = model.predict(sample)

print(
    encoder.inverse_transform(prediction)
)