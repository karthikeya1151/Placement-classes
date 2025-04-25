class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& t) {
        stack<int> st;
        vector<int> v(t.size(),0);
        for(int i = t.size()-1 ; i>=0 ; i--){
            int n = t[i];
            if(st.empty()){
                st.push(i);
                v[i]=0;
            } 
            else{
                if(t[st.top()]>n){
                    v[i]=st.top()-i;
                    st.push(i);
                }else{
                    while(!st.empty() && t[st.top()]<=n){
                        st.pop();
                    }
                    if(st.empty())v[i]=0;
                    else v[i]=st.top()-i;
                    st.push(i);
                }
            }
        }return v;
    }
};