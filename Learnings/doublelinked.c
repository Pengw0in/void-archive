#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int data;
	struct node* next;
	struct node* prev;
}node;

node* createNode(int value){
	node* newNode = (node *)malloc(sizeof(node));
	
	newNode -> data = value;
	newNode -> next = NULL;
	newNode -> prev = NULL;
	
	return newNode;
}

void insertAtFirst(node **head, int value) {
    node *newNode = createNode(value);
    newNode -> next = *head;
    if (*head != NULL) {
        (*head) -> prev = newNode;
    }
    *head = newNode;
}

void insertAtEnd(node **head, int value) {
    node *newNode = createNode(value);
    
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    
    node* temp = *head;
    while(temp -> next != NULL) {
        temp = temp -> next;
    }
    temp -> next = newNode;
    newNode -> prev = temp;
}

void insertAtPos(node **head, int value, int position) {
	node *newNode = createNode(value);
	node *temp = *head;
	for (int i = 1; i < position - 1; i ++) {
		if (temp -> next == NULL) {
			printf("Put of Bounds!");
		}
		temp = temp -> next;
	}
	newNode -> prev = temp;
	newNode -> next = temp -> next;
	
	if (temp -> next != NULL) {
		newNode -> next -> prev = newNode;
	}
	temp -> next = newNode;
}

void deleteAtFirst(node **head) {
	if (*head == NULL) {
		printf("List is empty");
		return;
	}
	
	node *temp = *head;
	*head = (*head)->next;
	if (*head != NULL) {
		(*head) -> prev = NULL;
	}
	free(temp);
}

void deleteAtEnd(node **head) {
	if (*head == NULL) {
		printf("List is empty");
		return;
	}
	
	node *temp = *head;
	
	while(temp -> next != NULL) {
		temp = temp -> next;
	}
    if (temp -> prev == NULL) {
        *head = NULL;
    } else {
        temp -> prev -> next = NULL;
    }
	free(temp);
}

void deleteAtPosition(node **head, int position) {
    if (*head == NULL || position <= 0) return;

    node *temp = *head;
    int i = 1;

    while (temp != NULL && i < position) {
        temp = temp -> next;
        i++;
    }

    if (temp == NULL) return;

    if (temp -> prev != NULL)
        temp -> prev -> next = temp -> next;
    else
        *head = temp -> next;

    if (temp -> next != NULL)
        temp -> next -> prev = temp -> prev;

    free(temp);
}


void display(node *head) {
    while (head != NULL) {
        printf("%d", head -> data);
        if (head -> next != NULL) {
            printf(" <-> ");
        }
        head = head -> next;
    }
    printf("\n");
}

int main() {
    node *head = NULL;

    insertAtFirst(&head, 10);
    insertAtFirst(&head, 20);
    insertAtFirst(&head, 30);

    display(head);

    deleteAtPosition(&head, 2);
    display(head);

    deleteAtFirst(&head);
    display(head);

    deleteAtEnd(&head);
    display(head);

    return 0;
}
