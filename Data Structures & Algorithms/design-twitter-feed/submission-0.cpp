class Twitter {
private:
    unordered_map<int, unordered_set<int>> followed;
    unordered_map<int, vector<int>> posts_by_user;
public:
    Twitter() {
        
    }
    
    void postTweet(int userId, int tweetId) {
        posts_by_user[userId].push_back(tweetId);
    }
    
    vector<int> getNewsFeed(int userId) {
        priority_queue<int> maxHeap;
        for(int user : followed[userId]) {
            for(int& post : posts_by_user[user]) {
                maxHeap.push(post);
            }
        }
        //push own posts
        for(int& post : posts_by_user[userId]) {
            maxHeap.push(post);
        }
        vector<int> result;
        for(int i = 0; i < 10 && !maxHeap.empty(); i++) {
            result.push_back(maxHeap.top());
            maxHeap.pop();
        }
        return result;
    }
    
    void follow(int followerId, int followeeId) {
        followed[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        followed[followerId].erase(followeeId);
    }
};
