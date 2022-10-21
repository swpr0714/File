#include<iostream>
using namespace std;

int main()
{
    string letter;
    int h, w;
    cout<<"Enter a letter (e or v):";
    cin>>letter;
    // cout<<letter<<h<<w;
    if (letter=="e"){
        cout<<"Enter the height and width:";
        cin>>h>>w;
        for (int j=0; j<w; j++){cout<<"*";}
        for (int j=0; j<(h-3)/2; j++){cout<<endl<<"*";}
        cout<<endl;
        for (int j=0; j<w; j++){cout<<"*";}
        for (int j=0; j<(h-3)/2; j++){cout<<endl<<"*";}
        cout<<endl;
        for (int j=0; j<w; j++){cout<<"*";}
    }
    if (letter=="v"){
        cout<<"Enter the height:";
        cin>>h;
        int in=2*(h-1)-1;
        int out = 1;
        for (int j=0; j<h; j++){
            if (in>0){
                for (int i=0; i<out; i++){cout<<" ";}
                cout<<"*";
                for (int i=0; i<in; i++){cout<<" ";}
                in=in-2;
                out++;
                cout<<"*";
                cout<<endl;
            }
        }
        for (int i=0; i<h; i++){cout<<" ";}
        cout<<"*"<<endl;
    }
}