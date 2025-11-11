#include <stdio.h>

void minAndMax (int *arr, int size) {
	int min , max = arr[1];
	
	for(int i = 0; i < size; i++) {
		if (min > arr[i]) {
			min == arr[i]
		}
	}

	for(int i = 0; i < size; i++) {
		if (max < arr[i]) {
			max == arr[i]
		}
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
	minAndMax(arr, size);
	return 0;
}