#include <stdio.h>

void reverse (int *arr, int size) {
	int rarr[size];
	int incre = 0;
	for(int i = size - 1; i >= 0; i--) {
		rarr[incre] = arr[i];
		incre++;
	}
	printf("Reversed array: ");
	for (int i = 0; i < size; i++) {
		printf("%d, ", rarr[i]);
	}
}

int main () {
	int element;
	int arr[6] = {7, 4, 2, 35, 13, 54};
	int size = sizeof(arr) / sizeof(int);
	reverse(arr, size);
	return 0;
}