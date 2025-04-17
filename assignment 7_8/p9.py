import re

def tokenize(text):
    patterns = {
        'punctuation': r'[.,!?;:()\'\"]',
        'date': r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',
        'url': r'https?://\S+',
        'email': r'\b[\w.-]+@[\w.-]+\.\w+\b',
        'number': r'\b\d+(\.\d+)?\b',
        'username': r'@\w+',
        'gujarati': r'[\u0A80-\u0AFF]+'
    }

    combined_pattern = '|'.join(f'(?P<{key}>{pattern})' for key, pattern in patterns.items())

    return [(match.lastgroup, match.group()) for match in re.finditer(combined_pattern, text)]


text = "મારો ઈમેલ છે test@example.com અને મારી વેબસાઇટ છે https://example.com. હું 12/12/2022 ને મળ્યો હતો."
tokens = tokenize(text)

for token in tokens:
    print(token)
