# include <stdio.h>

int main(void){
    int a=20;
    for(a;a>0;a--){
        for(int b=0;b<a;b++){
            printf("*");
        }
        printf("\n");
    }

}