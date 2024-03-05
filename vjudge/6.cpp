#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main()
{
    int N;
    cin>>N;
    long long arr[N+1];
    arr[0] = -9999999;
    for(int i=1;i<N+1;i++)
    {
        cin>>arr[i];
    }
    // 特判
    int judge = 1;
    long long MAX = 0;
    int index = 1;
    int pos_neg = 0;
    MAX = max(MAX,abs(arr[1]));
    for(int i=1;i<N;++i)
    {
        if(arr[i] > arr[i+1])
        {
            judge = 0;
        }
        if(abs(arr[i+1]) > MAX)
        {
            if(arr[i+1] > 0)
            {
                pos_neg = 1;
            }
            else
            {
                pos_neg = 0;
            }
            MAX = abs(arr[i+1]);
            index = i+1;
        }
    }
    if(judge)
    {
        cout<<0;
        return 0;
    }
    int operating = 0;
    vector<int>seq;
    
    for(int i=1;i<N+1;++i)
    {
        arr[i] += MAX;
        operating += 1;
        seq.push_back(index);
        seq.push_back(i);
    }
    if(pos_neg)
    {
        for(int i=N;i>1;i--)
        {
            arr[i-1] += arr[i];
            operating += 1;
            seq.push_back(i);
            seq.push_back(i-1);
        }
    }
    else
    {
        for(int i=1;i<N;i++)
        {
            arr[i+1] += arr[i];
            operating += 1;
            seq.push_back(i);
            seq.push_back(i+1);
        }
    }
    //
    cout<<operating<<endl;
    for(int i=0;i<seq.size();++i)
    {
        cout<<seq[i]<<' ';
        if(i%2)
        {
            cout<<endl;
        }
    }
    return 0;
}