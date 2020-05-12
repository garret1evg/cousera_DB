import sys
import json
from collections import Counter


def main():
    tweet_file = open(sys.argv[1])
    hashtags = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if "entities" in tweet:
            entities = tweet["entities"]
            curr_tags = entities["hashtags"]

            for tag in curr_tags:
                tag_text = tag["text"]
                if tag_text in hashtags.keys():
                    hashtags[tag_text] += 1
                else:
                    hashtags[tag_text] = 1

    sorted = Counter(hashtags)
    top_ten = sorted.most_common(10)
    for top in top_ten:
        print(top[0] + " " + str(top[1]))





if __name__ == '__main__':
    main()
