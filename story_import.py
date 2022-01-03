import sys
from urllib.request import urlopen
""" This module imports the urlib from url"""
# use url = "http://sixty-north.com/c/t.txt"

def fetch_words(url):
    """ This function fetches the url
    from the web and prints out words
    
    Args: url : The url 
    
    Returns: A list of strings containing the words from teh document.
    
    """
    
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    for item in items:
        print(item)
        
def main(url):
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])
