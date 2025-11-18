#include<stdio.h>
int cost[10][10];
int parent[10];
int n;
int find(int i)
{
  while (parent[i]!=i)
  i=parent[i];
  return i;
}
void union_set(int i,int j)
{
  int a=find(i);
  int b=find(j);
  parent[a]=b;
}
int main()
{
  int i,j,ne=1;
  int min,a,b,u,v,mincost=0;
  printf("Enter the number of nodes:");
  scanf("%d",&n);
  printf("\nEnter the cost adjacency matrix:\n");
  for(i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
      scanf("%d",&cost[i][j]);
      if(cost[i][j]==0)
      cost[i][j]==999;
    }
  }
  for(i=0;i<n;i++)
     parent[i]=i;
  printf("\nThe edges of the minimum cost spanning tree are:\n");
  while(ne<n)
  {
   min=999;
   a=b=-1;
   for(i=0;i<n;i++)
   {
     for(j=0;j<n;j++)
     {
       if(cost[i][j]<min)
       {
        min=cost[i][j];
        a=i;
        b=j;
       }
     }
   }
   u=find(a);
   v=find(b);
   if(u!=v)
   {
     printf("\nEdges %d:(%d->%d)\tCost:%d",ne++,a,b,min);
     mincost += min;
     union_set(u,v);
   }
   cost[a][b]=cost[b][a]=999;
 }
 printf("\n\nMinimum cost=%d\n",mincost);  
 return 0;
 }
