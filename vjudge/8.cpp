#include <iostream>
#include <string>
#include <vector>
#include <deque>
using namespace std;

string a,b;
int dp[1000000+9];
int abs_ = 0;

bool judge(char zz,int idx)
{
    int cur = abs_;
    if(zz != a[idx])
    {
        cur++;
    }
    if(zz != b[idx])
    {
        cur--;
    }
    return (abs(cur)<=dp[idx+1]);
}

int main()
{
    int T;
    cin>>T;
    int range=0;
    for(int i=0;i<T;++i)
    {
        
        cin>>a;
        cin>>b;
        int n = a.length();
        
        dp[n] = 0;
        for(int j=n-1;j>=0;--j)
        {
            dp[j] = dp[j+1];
            if(a[j] != b[j])
            {
                dp[j]++;
            }
        }
        cout<<"Case "<<++range<<": ";
        abs_ = 0;
        for(int j=0;j<n;++j)
        {
            for(int k=0;k<26;++k)
            {
                char zzz = 'a'+k;
                if(!judge(zzz,j))
                {
                    continue;
                }
                cout<<zzz;
                if(zzz != a[j])
                {
                    abs_++;
                }
                if(zzz != b[j])
                {
                    abs_--;
                }
                break;
            }
        }
        cout<<endl;
    }
    return 0;
}