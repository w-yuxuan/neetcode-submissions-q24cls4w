class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet = defaultdict(list) #user => (count,tweetId)
        self.mem = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -=1
        self.tweet[userId].append((self.count,tweetId))        

    def getNewsFeed(self, userId: int) -> List[int]:
        # push all the tweets in this user's sphere to a heap
        h = []
        res = []
        temp = []
        self.mem[userId].add(userId)
        for followed in self.mem[userId]:
            for tw in self.tweet[followed]:
                heapq.heappush(h,tw)
        while h and len(res)<10:
            item = heapq.heappop(h)
            res.append(item)
            temp.append(item)
        while temp:
            heapq.heappush(h,temp.pop())
        return [x[1] for x in res]

        #pop 10 to output then push back onto heap

    def follow(self, followerId: int, followeeId: int) -> None:
        self.mem[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.mem[followerId].discard(followeeId)

