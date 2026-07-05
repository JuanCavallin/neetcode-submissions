/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(node == nullptr) {
            return nullptr; //edge case check
        }
        unordered_set<Node*> visited;
        unordered_map<Node*, Node*> original_value_to_clone;
        stack<Node*> s;
        Node* current = node;
        s.push(current);
        //visited.insert(node);
        original_value_to_clone[current] = new Node(current->val);

        while(!s.empty()) {
            current = s.top();
            s.pop();
            Node* new_node = original_value_to_clone[current];
            //auto neighbors = current->neighbors;
            for(Node* n : current->neighbors) {
                if(original_value_to_clone.find(n) == original_value_to_clone.end()) {
                    //Value doesn't exist already, so we add to the stack, to OVTC, and create it
                    s.push(n);
                    Node* new_neighbor = new Node(n->val);
                    original_value_to_clone[n] = new_neighbor;
                }
                //In either case, add as neighbor to new_node
                new_node->neighbors.push_back(original_value_to_clone[n]);
            }

        }
            return original_value_to_clone[node];

    }
};
