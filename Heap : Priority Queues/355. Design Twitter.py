class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = {userId}
        if userId in self.follows:
            users.update(self.follows[userId])

        for user in users:
            if user in self.tweets and self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time_stamp, tweet_id = self.tweets[user][index]
                heapq.heappush(heap, (-time_stamp, user, index, tweet_id))

        result = []
        while heap and len(result) < 10:
            neg_time, user, index, tweet_id = heapq.heappop(heap)
            result.append(tweet_id)
            if index - 1 >= 0:
                prev_time, prev_tweet = self.tweets[user][index - 1]
                heapq.heappush(heap, (-prev_time, user, index - 1, prev_tweet))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)