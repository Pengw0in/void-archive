#include <stdio.h>


#define MAX_SIZE 10

typedef struct {
    int data[MAX_SIZE];
    int size;
} arrayADT;

void display (arrayADT *arr);

void init (arrayADT *arr) {
	int size;
	
//	int num;
//	
//	printf("Enter number of elements: ");
//	scanf("%d", &size);
//
//	for(int i = 0; i < size; i++){
//		printf("Enter element %d: ", i + 1);
//		scanf("%d", &num);
//		printf("\n");
//		arr -> data[i] = num;
//	}

    arr -> size = 0;
    
}

void delete (arrayADT *arr, int index) {
    if (index < 0 || index >= arr -> size || arr -> size >= MAX_SIZE) {
        printf("Invalid index or Element does not exist\n");
        return;
    }
    
    for (int i = index; i < arr -> size - 1; i++){
        arr -> data[i] = arr -> data[i + 1];
    }
    arr -> size--;
    display(arr);
}

void insertAt (arrayADT *arr, int index, int value) {
    if (index < 0 || index > arr -> size || arr -> size >= MAX_SIZE) {
        printf("invalid index or list is full\n");
        return;
    }
        
    for (int i = arr -> size; i > index; i--) {
        arr -> data[i] = arr -> data[i-1];
    }
    arr -> data[index] = value;
    arr -> size++;
    display(arr);
}

void insertEnd (arrayADT *arr, int value) {
    if (arr -> size >= MAX_SIZE) {
        printf("The List is full\n");
        return;
    }
    
    arr -> data[arr -> size] = value;
    arr -> size++;
    display(arr);
}

void display (arrayADT *arr) {
    if (arr -> size == 0) {
        printf("List is Empty\n");
        return;
    }
    
    for (int i = 0; i < arr -> size; i++) {
        printf("%d ", arr -> data[i]);
    }
    printf("\n");
}


int main() {

	arrayADT arr;
	init(&arr);
    insertAt(&arr, 0, 59);
    insertEnd(&arr, 7);
    insertAt(&arr, 1, 16);
    insertEnd(&arr, 8);
    delete(&arr, 3);
    
    return 0;
}

