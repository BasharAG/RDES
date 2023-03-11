import praw
import csv

reddit = praw.Reddit(client_id='yEZwcvL1xXxSvLmwXj_o2w',
                     client_secret='Bl1DCYCPpihU6RsEUCwX2xixFcrxnA',
                     user_agent='IPFResearch')

subreddit = reddit.subreddit('EssentialTremor')

# create an empty list to store the posts
posts = []

for submission in subreddit.hot(limit=10000):
    # check if the submission is a text post
    if submission.is_self and not submission.media_only:
        # create a dictionary with the post data
        post = {'title': submission.title, 'text': submission.selftext, 'author': submission.author.name, 'score': submission.score, 'created_utc': submission.created_utc}
        # check if the post is already in the list of posts
        if post not in posts:
            # add the post to the list of posts
            posts.append(post)

# write the posts to a CSV file
with open('essentialtremor_posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'text', 'author', 'score', 'created_utc']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for post in posts:
        writer.writerow(post)
