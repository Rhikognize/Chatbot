
substitutii = {
    'ă': 'a', 'â': 'a', 'î': 'i', 'ș': 's', 'ş': 's', 'ț': 't', 'ţ': 't',
    'Ă': 'a', 'Â': 'a', 'Î': 'i', 'Ș': 's', 'Ş': 's', 'Ț': 't', 'Ţ': 't'
}

interests = {
    "fotbal": "joacă fotbal",
    "muzică": "ascultă muzică",
    "citit": "citește cărți",
    "programare": "scrie cod",
    "călătorii": "călătorește",
    "gătit": "gătește",
    "sport": "practică sport",
    "dans": "dansează",
    "arte": "creează artă",
}


def simplify_text(text):
    for key, value in substitutii.items():
        text = text.replace(key, value)
    return text


simplified_interests = {simplify_text(k): v for k, v in interests.items()}
