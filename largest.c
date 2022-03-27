#include <stdio.h>
#include <stdlib.h>

typedef int Item;
#define less(A,B) ((A) < (B))
#define lesseq(A,B) ((A) <= (B))
#define exch(A,B) { int t; t=A;A=B;B=t; }
#define cmpexch(A,B) { if (less(B,A)) exch(A,B); }

void insertionSort(Item *v, int l, int r){
    int aux;

    for(int i=r; i>l; i--){
        if(v[i-1]>v[i]){
            aux = v[i];
            v[i] = v[i-1];
            v[i-1] = aux;
        }
    }

    for(int i = l+2; i<=r; i++){

        int j = i; int elemento = v[j];

        while(elemento < v[j-1]){
             v[j]=v[j-1];
             j--;
        }
         v[j]=elemento;
    }

}

int partition(Item *v,int l,int r){
  Item aux=v[r];
  int j=l;

  for(int k=l;k<r;k++){
    if(less(v[k],aux)){
      exch(v[k],v[j]);
      j++;
    }
  }

  exch(v[j],v[r]);
  return j;
}

void quickSortMediana3(Item *v,int l, int r){
  if (r-l<=32) {
    return;
  }

  exch(v[(l+r)/2],v[r-1]);
  cmpexch(v[l],v[r-1]);
  cmpexch(v[l],v[r]);
  cmpexch(v[r-1],v[r]);

  int j=partition(v,l+1,r-1);
  quickSortMediana3(v,l,j-1);
  quickSortMediana3(v,j+1,r);
}

void quickSortMediana3Insertion(Item *v,int l,int r){
  quickSortMediana3(v,l,r);
  insertionSort(v,l,r);
}

int findKthLargest(int* nums, int numsSize, int k){
  quickSortMediana3Insertion(nums,0,numsSize-1);
  int value = numsSize - (k-1);
  return value;
}
