#include <iostream>
#include <string.h>
using namespace std;
int ans[5*1000000+5];
int arr[5*1000000+5];

int main()
{
    size_t n,c,b;
    cin>>n>>c>>b;
    
    /*
    memset(ans,0,sizeof(int)*(n+1));
    memset(arr,1,sizeof(int)*(n+1));
    */
    size_t temp = 0;
    for(size_t i=0;i<b;i++)
    {
        cin>>temp;
        arr[temp] = 1;
    }

    ans[1] = 0;
    int beg = 2;
    if(c % 2)
    {
        ans[1] = 1;
        c--;
        beg = 3;
    }

    for(int i=beg;i<=n;++i)
    {
        int length = 0, len = i;
        int check = 1;
        while(!arr[i] && i<=n)
        {
            length ++;
            ++i;
        }
        for(int j=len; j<len+length;j+=2)
        {
            if(c)
            {
              ans[j] = 1;
                c -= 2;  
            }
            else
            {
                check = 0;
                break;
            }
        }
        if(!check)
        {
            break;
        }
    }

    for(int i=1;i<n+1;++i)
    {
        cout<<ans[i];
    }
    
    return 0;
}