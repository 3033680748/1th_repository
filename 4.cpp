#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(size_t* a,size_t* b)
{
    return (a[0]<=b[0]);
}

int main()
{
    size_t n;
    vector<size_t*>A;
    cin>>n;
    size_t temp[n][2];
    for(size_t i=0;i<n;++i)
    {
        
        cin>>temp[i][0]; // 数
        temp[i][1] = i+1; // 索引 
        A.push_back(temp[i]);
    }
    sort(A.begin(),A.end(),cmp);

    size_t check = 0;
    size_t ans[n+1];
    check = A[0][0]+A[n-1][0];
    ans[A[0][1]] = A[n-1][1];
    ans[A[n-1][1]] = A[0][1];

    for(int i=1;i<=n-1-i;++i)
    {
        if((A[i][0]+A[n-i-1][0]) != check)
        {
            cout<<-1;
            return 0;
        }
        else
        {
            ans[A[i][1]] = A[n-i-1][1];
            ans[A[n-1-i][1]] = A[i][1];
        }
    }
    for(int i=1;i<n+1;++i)
    {
        cout<<ans[i]<<' ';
    }
    return 0;
}
