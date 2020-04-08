# Functions for cleaning tweets using Pandas
# Lowercases everything for easier word processing using NLTK and other NLP libraries

def url(string):
    """
    From a string, any URL starting in 'http' or 'https'

    """
    wordlist = string.split()
    text = ' '.join(word for word in wordlist if 'http' in word)
    return text.lower()

def no_urls(string):
    """
    From a string, returns text that is cleaned of any URLs starting in 'http' or 'https'

    """
    wordlist = string.split()
    text = ' '.join(word for word in wordlist if not 'http' in word)
    return text.lower()

def hashtags(string):
    """
    From a string, returns any text that contains a hashtag

    """
    wordlist = string.split()
    text = ' '.join(word for word in wordlist if '#' in word)
    return text.lower()

def at_mention(string):
    """
    From a string, returns any text that contains @

    """
    wordlist = string.split()
    text = ' '.join(word for word in wordlist if '@' in word)
    return text.lower()

def cleaned_tweet(string):
    """
    Removes URLs, hashtags, and @ mentions in tweets
    """
    wordlist = string.split()
    text = ' '.join(word for word in wordlist if 'http' not in word and '@' not in word and '#' not in word)
    return text.lower()