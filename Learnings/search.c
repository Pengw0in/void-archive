#include <stdio.h>

int search (int *arr, int size, int element) {
	int found = 0;
	for(int i = 0; i < size; i++) {
		if (arr[i] == element) {
			printf("element found at %d position: ", i + 1 );
			found = 1;
			break;
		}
	}
	if(!found) {
		printf("element not found");
	}
}

int main () {
	int element;
	int arr[6] = {7, 4, 2, 35, 13, 54};
	printf("Enter the element you want to search: ");
	scanf("%d", &element);
	int size = sizeof(arr) / sizeof(int);
	search(arr, size, element);
	return 0;
}