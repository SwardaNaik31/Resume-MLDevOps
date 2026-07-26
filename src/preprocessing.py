import pandas as pd
import re
import string
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def clean_resume(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)