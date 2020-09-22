import tweepy
from tkinter import *

# Paste your Twitter account Credentials below from: https://apps.twitter.com/
consumer_key = 'comsumer-key'
consumer_secret = 'consumer-secret'
access_token = 'access-token'
access_token_secret = 'access-token-secret'

## Authenticating with Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# To check if its working
user = api.me()
print(user.name)

# Creating a GUI
root = Tk()

label1 = Label(root, text="Search")
E1 = Entry(root,bd = 5)

label2 = Label(root,text="Number of tweets")
E2 = Entry(root,bd=5)

label3 =Label(root,text="Like?")
E3 = Entry(root,bd=5)

label4 = Label(root,text="Retweet?")
E4 = Entry(root,bd=5)

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()

def getE4():
    return E4.get()

def mainFunction():
    getE1()
    search = getE1()

    getE2()
    numberOfTweets = int(getE2())

    getE3()
    like = getE3()
    like = like.lower()

    getE4()
    retweet = getE4()
    retweet = retweet.lower()

    if retweet == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.retweet()
                print("Retweeted the tweet")

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if like == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.favorite()
                print("Liked the tweet.")

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

submit = Button(root,text="Submit", command = mainFunction)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()

submit.pack(side = BOTTOM)

root.mainloop()
