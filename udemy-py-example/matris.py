#include<stdio.h>

int main(){
int x,y,i,j,result,counter=0;

printf("1.sayi: ");
scanf("%d",&x);

printf("2.sayi: ");
scanf("%d",&y);

for(i=x;i<y;i++)

	for(j=2;j<i;j++)
		
		if(i % j == 0)
			counter++;
		
	if(counter == 0)
		printf("%d\n",i);
}