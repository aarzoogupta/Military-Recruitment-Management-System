#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int space_var=2*n-1;
    for (int i=1;i<=n;++i)
    {
        for(int j=1;j<=i;++j)
        {
            cout<<j<<"\t";
        }
        for(int j=space_var;j>2*i;--j)
        {
            cout<<"\t";
        }
        for(int j=i;j>=1;--j)
        {
            if (j==n){continue;}
            else{cout<<j<<"\t";}
        }
        cout<<endl;
    }
}