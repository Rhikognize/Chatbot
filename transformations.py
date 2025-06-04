import re
import string
from interests import simplified_interests


def transform_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation} 0-9]", "", text)
    return text


def transform_age(age):
    if age <= 14:
        return "un copil"
    if age <= 18:
        return "un tânăr"
    if age <= 30:
        return "un adult tânăr"
    if age <= 50:
        return "un adult"
    return "un om în vârstă"


def transform_interest(interest):
    interest = transform_text(interest)
    if interest in simplified_interests:
        return simplified_interests[interest]
    return f"se ocupă cu {interest}"
