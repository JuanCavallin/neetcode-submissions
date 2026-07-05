class Solution {
public:
    bool isValid(string s) {
        stack<char> _stack;
        for(char c : s) {
            if(c == '(' || c == '{' || c == '[') {
                _stack.push(c);
            }
            if(c == ')') {
                if(_stack.empty() || _stack.top() != '(') {
                    return false;
                }
                _stack.pop();
            }
            if(c == '}') {
                if(_stack.empty() || _stack.top() != '{') {
                    return false;
                }
                _stack.pop();
            }
            if(c == ']') {
                if(_stack.empty() || _stack.top() != '[') {
                    return false;
                }
                _stack.pop();
            }
        }
        return _stack.empty();
    }
};
