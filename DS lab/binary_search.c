#include<stdio.h>
int main()
{
 int i,n,key,mid,high,low,found=0;
 printf("Enter number of elements:\n");
 scanf("%d",&n);
 int arr[n];
 printf("Enter %d elements in sorted order:\n",n);
 for(i=0;i<n;i++)
 {
  scanf("%d",&arr[i]);
 }
 printf("Enter number to search:/n");
 scanf("%d",&key);
 low=0;
 high=n-1;
 while(low<high)
 {
  mid=(low+high)/2;
  if(arr[mid]==key)
  {
   printf("Enter %d element is found at the position %d\n",key,mid+1);
   found=1;
   break;
  }
  else
  {
   high=mid-1;
  }
 }
 if(found==0)
 {
  printf("Element %d not found in the array\n",key);
 }
 return 0; 
}

