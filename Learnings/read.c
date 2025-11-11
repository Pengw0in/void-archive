#include <stdio.h>

void display (int *arr, int size){
	printf("your array is: ");
	for(int i = 0; i < size; i++) {
		printf("%d, ", arr[i]);
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
	display(arr, size);
	return 0;
}