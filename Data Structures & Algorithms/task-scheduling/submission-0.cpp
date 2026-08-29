class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int interval = 0;

        // Count frequency of each task
        unordered_map<char, int> counts;

        for (char task : tasks) {
            counts[task]++;
        }

        // Most frequent task comes first
        priority_queue<pair<int, char>> maxHeap;

        for (auto& p : counts) {
            maxHeap.push({p.second, p.first});
        }

        while (!maxHeap.empty()) {

            // Tasks used during this n+1-sized scheduling block
            queue<pair<int, char>> cooldown;

            int tasksRun = 0;

            // Need n+1 distinct task positions:
            // A _ _ A when n = 2
            // distance between A's = 3 positions
            for (int i = 0; i < n + 1 && !maxHeap.empty(); i++) {
                auto task = maxHeap.top();
                maxHeap.pop();

                task.first--;      // executed once
                tasksRun++;

                if (task.first > 0) {
                    cooldown.push(task);
                }
            }

            // Put tasks back after the entire block
            while (!cooldown.empty()) {
                maxHeap.push(cooldown.front());
                cooldown.pop();
            }

            // If more work remains, the block must occupy n+1 intervals.
            // Otherwise, only count the tasks actually executed.
            if (!maxHeap.empty()) {
                interval += n + 1;
            } else {
                interval += tasksRun;
            }
        }

        return interval;
    }
};