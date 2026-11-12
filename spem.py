SPAM_WORDS = {
    'free': 2, 'winner': 3, 'prize': 3, 'urgent': 2,
    'click': 2, 'cash': 2, 'verify': 2, 'now': 1
}

THRESHOLD = 4

def get_score(message):
    return sum(SPAM_WORDS.get(word.lower().strip('.,!?'), 0) for word in message.split())

def classify(message):
    return 'SPAM' if get_score(message) >= THRESHOLD else 'SAFE'

tests = [
    ('You WON a free prize! Click now', 'SPAM'),
    ('URGENT: verify your account', 'SPAM'),
    ('Hey, are we still meeting at 5?', 'SAFE')
]

for msg, expected in tests:
    res = classify(msg)
    print(f'[{res}] Score: {get_score(msg)} | {msg}')