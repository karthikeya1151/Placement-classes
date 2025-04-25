
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if(root==NULL) return {};
        deque<vector<int>> dq;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            int n = q.size();
            vector<int> v;
            for(int i=0;i<n;i++)
            {
                TreeNode* node = q.front();
                q.pop();
                v.push_back(node->val);
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
            dq.push_front(v);
        }
        return vector<vector<int>>(dq.begin(), dq.end());
    }
};