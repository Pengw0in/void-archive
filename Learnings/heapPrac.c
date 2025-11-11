#include <stdio.h>

void heapify(int arr[], int i, int n){
	int largest = i;
	int l = i * 2 + 1;
	int r = i * 2 + 2;
	
	if(l < n && arr[l] > arr[largest]){
		largest = l;
	}
		
	if(r < n && arr[r] > arr[largest]){
		largest = r;
	}

	if(largest != i){
		int temp = arr[i];
		arr[i] = arr[largest];
		arr[largest] = temp;
		
		heapify(arr, largest, n);
	}		
}

void heapSort(int arr[], int n){

	
	for(int i = n / 2 - 1; i >= 0; i--){
		heapify(arr, i, n);
	}
	
	for(int i = n - 1; i > 0; i--){
		int temp = arr[0];
		arr[0] = arr[i];
		arr[i] = temp;
		
		heapify(arr, 0, i);
	}
}

int main() {
	int arr[] = {9, 4, 3, 8, 10, 2, 5};
	int n = sizeof(arr) / sizeof(arr[0]);
	
	heapSort(arr, n);
	
	for(int i = 0; i < n; ++i)
		printf("%d ", arr[i]);
		
		return 0;
}