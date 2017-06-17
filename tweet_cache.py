import log
import csv

def cache_and_trim(file_name, tweets):
    trimmed_tweets = []
    used_ids = []

    try:
        with open(file_name, "r") as id_file:
            reader = csv.reader(id_file, delimiter = ',')
            used_ids = list(reader)[0]
    except IOError, IndexError:
        with open(file_name, 'w') as myfile:
            myfile.write("")

    for index, tweet in enumerate(tweets):
        log.log(' '.join(('The tweets to check...', str(tweet['id']))))
        if tweet['id_str'] not in used_ids:
            trimmed_tweets.append(tweet)
            log.log(' '.join(('Adding...', tweet['id_str'])))

    log.log(' '.join(('Number of tweets to post:', str(len(trimmed_tweets)))))
    tweet_ids = [tweet['id_str'] for tweet in tweets]

    with open(file_name, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(tweet_ids)

    return trimmed_tweets