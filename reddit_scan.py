import praw

class RedditScan:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    def scan_user_posts(self, username):
        user = self.reddit.redditor(username)
        return [post.title for post in user.submissions.new(limit=10)]
