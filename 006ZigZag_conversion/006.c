#include<string.h>
#include<stdlib.h>
char* convert(char* s, int numRows) {
    int n = strlen(s);
    char* a= (char*)malloc(sizeof(char)*(n+1));;
    int k=0;

    if(numRows==1 || n<=numRows)return s;
    for(int i=0;i<numRows;i++){
        for(int j=1; j<n; j+=2*(numRows-1)){
            a[k++]=s[j];
            if(i!=0 && i!=numRows-1){
                int t = j+2*(numRows-1)-2*i;
                if(t<n){
                    a[k++]=s[t];
                }
            }
        }
    }
    a[k]='\0';
    return a;
}
int main(){
    char* res;
    // PAYPALISHIRING
    char s[]={'P','A','Y','P','A','L','I',
    'S','H','I','R','I','N','G'};
    res = convert(s,4);
    return 0;
}