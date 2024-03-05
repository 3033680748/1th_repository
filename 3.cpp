#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

void mutiple(size_t a,size_t b)
{   
    vector<int>out;
    vector<int>A;
    vector<int>B;
    for(int i=10;i>-1;--i)
    {
        A.push_back(a%10);
        a = a / 10; 
        B.push_back(b%10);
        b = b / 10;
    }
    int n = max(A.size(),B.size());
    int m = min(A.size(),B.size());
    for(int i=0;i<n+m;++i)
    {
        // 多一个用于进位
        out.push_back(0);
    }
    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
            if(A.size() >= B.size())
            {
                out[i+j] += A[j]*B[i];
            }
            else
            {
                out[i+j] += A[i]*B[j];
            }
        }
    }
    for(int i=0; i<out.size()-1;i++)
    {
        out[i+1] += out[i] / 10;
        out[i] = out[i] % 10; 
    }
    int beg = 0;
    for(int i=out.size()-1;i>-1;--i)
    {
        if(out[i])
        {
            beg = i;
            break;
        }
    }
    for(int i=beg;i>-1;i--)
    {
        cout<<out[i];
    }

}

int main()
{
    size_t a,b;
    scanf("%lld",&a);
    scanf("%lld",&b);
    printf("%lld\n",a+b);
    printf("%lld\n",a-b);
    mutiple(a,b);
    return 0;
}