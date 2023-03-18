import tweepy

# Twitter API credentials
consumer_key = 'your_consumer_key_here'
consumer_secret = 'your_consumer_secret_here'
access_token = 'your_access_token_here'
access_token_secret = 'your_access_token_secret_here'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# List of usernames to send the message to
usernames = ['username1', 'username2', 'username3']

# Message to send
message = 'Hello, this is a test message!'

# Loop through the list of usernames and send the message to each one
for username in usernames:
    try:
        user = api.get_user(username)
        api.send_direct_message(user.id, message)
        print(f"Message sent to {username}")
    except tweepy.TweepError as e:
        print(f"Error sending message to {username}: {e}")
