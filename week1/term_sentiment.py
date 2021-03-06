import sys
import json
import re


def main():
    afinnfile = open(sys.argv[1])

    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            formatted_text = re.split(r"[\s\.,\?\:]+", tweet["text"])
            sentiment = 0

            for word in formatted_text:
                if word in scores:
                    sentiment = sentiment + scores[word]

            for word in formatted_text:
                if word not in scores:
                    print(word + " " + str(sentiment))


if __name__ == '__main__':
    main()
