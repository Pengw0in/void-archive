#include <stdio.h>
#include <stdlib.h>

int merge(int arr[], int l, int m, int r){
	int i, j, k;
	int n1 = m - l + 1;
	int n2 = r - m;
	
	L[n1], R[n2];
	for(i = 0; i < n1; i++){
		L[i] = arr[l + 1];
	}
	for(j = 0; j < n2; j++){
		R[j] = arr[r + m + 1];
	}
	
	i = 0;
	j = 0;
	k =l;
	while(i < n1 && j < n2){
		if (L[i] < R[j]){
			arr[k] = L[i];
			i++;
		} else{
			arr[k] = R[j];
		}
		k++;
	}
	
	
}