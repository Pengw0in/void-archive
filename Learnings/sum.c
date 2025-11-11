#include <stdio.h>

void sum (int *arr, int size) {
	int sum = 0;
	for (int i = 0; i < size; i++) {
		sum += arr[i];
	}
}


void read (int *arr, int size){
	for(int i = 0; i < size; i++) {
		printf("Enter element %d\n", i);
		scanf("%d", &arr[i]);
	}
}

int main () {
	int size;
	printf("How many elements: ");
	scanf("%d", &size);
	int arr[size];
	
	read(arr, size);
	sum(arr, size);
	return 0;
}