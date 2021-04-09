# Natural Language Processing Hub

This is where the tools to score investor sentiment from across the web will be stored.
I anticipate looking at a lot of examples around github and either directly using
or borrowing frameworks from random repo's.

### List of Repos with promise


-https://github.com/RyanElliott10/wsbtickerbot
This supports slang capture and emojis which is maybe good maybe bad.
Understands modifiers (e.g. <very/not/kind of> good), contractions, caps lock,
Nice documentation, and ports to php, java 

- https://github.com/KevHg/reddit-sentiment
Needs some work. Uses established toolkits
for language processing and scoring (Python)

-https://github.com/asad70/reddit-sentiment-analysis
This looks good to, uses the same scorer tk as 'KevHg' repo.
Gives benchmark of 217s for ~6k comments on 80 posts in 4 subreddits.
Assume linear scaling:
Extrapolating to something like /r/wsb/search?sort=new&restrict_sr=on&q=flair:DD
It would need roughly 900 seconds for 100 posts (assuming 300 comments per post (taken from an average on 4/6/2021)

- https://github.com/googleapis/nodejs-language
Written in nodejs so thats maybe a perk if we don't like python
