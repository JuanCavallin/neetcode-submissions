class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty() || s.empty() || s.size() < t.size()) return "";
        if (s == t) return t;

        // Count needed copies of each char in t
        unordered_map<char,int> need;
        unordered_set<char> remaining; // chars whose need[c] > 0
        for (char c : t) {
            need[c]++;
        }
        for (auto &kv : need) remaining.insert(kv.first);

        int n = (int)s.size();
        int slow = 0, fast;

        // Align slow to first char that appears in t
        while (slow < n && !need.count(s[slow])) slow++;
        if (slow == n) return "";     // s has none of t's chars
        fast = slow;

        string ans = "";
        while (fast < n) {
            char c = s[fast];

            // Consume s[fast] if it's relevant
            if (need.count(c)) {
                need[c]--;
                // When a char's need drops to zero, it's no longer "remaining"
                if (need[c] == 0) {
                    remaining.erase(c);
                }
            }

            // When all needs are met, try to shrink from the left
            while (remaining.empty() && slow <= fast) {
                // Update best
                int len = fast - slow + 1;
                if (ans.empty() || len < (int)ans.size()) {
                    ans = s.substr(slow, len);
                }

                // Release s[slow] and advance slow to next relevant char
                char sc = s[slow];
                if (need.count(sc)) {
                    need[sc]++;
                    if (need[sc] > 0) {
                        // We just broke the window
                        remaining.insert(sc);
                    }
                }
                slow++;

                // Skip non-target chars quickly (doesn't affect counts)
                while (slow < n && !need.count(s[slow])) slow++;
            }

            fast++;
        }

        return ans;
    }
};
