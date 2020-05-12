import sys
import json
import re


def main():
    file = open(sys.argv[1])

    scores = {}
    for line in file:
        term, score = line.split("\t")
        scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            formatted_text = re.split(r"[\s\.,\?\:]+", tweet["text"])
            sentiment = 0

            for word in formatted_text:
                if word in scores:
                    sentiment = sentiment + scores[word]

            print(sentiment)


if __name__ == '__main__':
    main()
