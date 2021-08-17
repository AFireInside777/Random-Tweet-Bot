from twitter import *
from VideoGameTriviaDict import y
import random
import time

api = Twitter(auth=OAuth(
token='1286447442775375877-e9G29sxXrcs9jYy9C2xU9aSMjfQmXK', 
token_secret='YUKpi1ANnEaorCKPy6gCBnnDl2BD6rD7c2KbNrREjWRWB', 
consumer_key='nlOEoIMsqpEhJeVMNdUqiYs3N',
consumer_secret='LVW33fXTBeI1mLZXDvJgIxl30JmxHZa9kqOzx3HdY4Nmt4zlu8'
))

y_list = [*range(1, 20)]

random.shuffle(y_list)

for i in range(20):
    key = y_list[i]
    tweet = y[key]
    newstatus = api.statuses.update(status=tweet)
    time.sleep(60)