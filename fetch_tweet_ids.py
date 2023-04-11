import json

def fetch_tweet_ids(files):
    tweet_ids = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            ids = [data[i]['tweet']['id'] for i in range(len(data))]
            tweet_ids.extend(ids)
    return tweet_ids
