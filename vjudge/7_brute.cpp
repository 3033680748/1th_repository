#include <iostream>
#include <string.h>
using namespace std;

size_t n,c,b;
int arr[5*100000];
int ans[5*100000];

bool dfs(size_t depth,size_t weight,size_t cur)
{
    if(depth == n)
    {
        if(weight == c && cur == 0)
        {
            ans[depth] = cur;
            return true;
        }
        else
        {
            return false;
        }
    }
    else
    {
        if(weight > c)
        {
            return false;
        }
        else if(arr[depth]==0 && cur == 1)
        {
            return false;
        }
        else
        {
            if(cur) //当前为1
            {
                if(dfs(depth+1,weight,1))
                {
                    ans[depth] = 1;
                    return true;
                }
                else if(dfs(depth+1,weight+1,0))
                {
                    ans[depth] = 1;
                    return true;
                }
                    return false;
                }
            else //当前为0
            {
                if(dfs(depth+1,weight+1,1))
                {
                    ans[depth] = 0;
                    return true;
                }
                else if(dfs(depth+1,weight,0))
                {
                    ans[depth] = 0;
                    return true;
                }
                    return false;
            }
        }
    }
}   

int main()
{
    
    cin>>n>>c>>b;
    memset(arr,1,5*100000*sizeof(int));
    for(size_t i=0;i<b;i++)
    {
        int temp = 0;
        cin>>temp;
        arr[temp] = 0;
    }
    memset(ans,-1,5*100000*sizeof(int));

    if(dfs(1,0,1))
    {
        for(size_t i=1;;++i)
        {
            if(ans[i]!=-1)
            {
                cout<<ans[i];
            }
            else
            {
                break;
            }
        }
    }
    else
    {
        dfs(1,0,0);
        for(size_t i=1;;++i)
        {
            if(ans[i]!=-1)
            {
                cout<<ans[i];
            }
            else
            {
                break;
            }
        }
    }
    
    return 0;
}