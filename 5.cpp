#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

vector<size_t>ANS;

void dp(string A,int a,int b)
{
    size_t n = A.size();
    size_t dp[n][2] = {0}; // 每个顺序串的末尾放与不放
    // 初始化
    if(A[0] == '0')
    {
        dp[0][1] = a+b;
    }
    else
    {
        dp[0][1] = a;
        dp[0][0] = 999999999;
    }
    for(size_t i=1;i<n;++i)
    {
        if(A[i] == '0')
        {
            dp[i][0] = min(dp[i-1][0],dp[i-1][1]);
            dp[i][1] = min(dp[i-1][0]+a+b,dp[i-1][1]+b);
        }
        else
        {
            dp[i][1] = min(dp[i-1][1],dp[i-1][0]+a);
            dp[i][0] = 999999999;
        }
    }
    size_t ans = min(dp[n-1][0],dp[n-1][1]);
    ANS.push_back(ans); 
}

int main()
{
    size_t total;
    string temp;
    cin>>total;
    for(size_t i=0;i<total;++i)
    {
        int a,b;
        cin>>a>>b;
        cin>>temp;
        dp(temp,a,b);
    }
    for(size_t i=0;i<total;++i)
    {
        cout<<ANS[i]<<endl;
    }
    return 0;
}

    