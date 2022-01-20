from datetime import date
class Tweet:
    ind = 0
    def __init__(self, text) :
        self.text = text
        self.created_at = date.today()
        self.id = None
        Tweet.ind += 1
        pass
    
class TweetRepository:
    def __init__(self):
        pass