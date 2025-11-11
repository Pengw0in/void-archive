#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int data;
	struct node *next;
} node;

node* createNode(int value) {
	node *newNode = (node *)malloc(sizeof(node));
	newNode -> data = value;
	newNode -> next = NULL;
	
	return newNode;
}

void display(node **head) {
	if (*head == NULL) {
		return;
	}
	
	node *temp = *head;
	while(temp != NULL) {
		printf("%d", temp -> data);
		if (temp -> next != NULL){
			printf(" -> ");
		}
		temp = temp->next;
	}
	printf("\n");
}

void insertAtFirst(node **head , int value) {
	node *newNode = createNode(value);
	newNode -> next = *head;
	*head = newNode;
}

void insertAtEnd(node **head, int value) {
	node *newNode = createNode(value);
	if (*head == NULL) {
		*head = newNode;
		return;
	}
	
	node *temp = *head;
	while(temp -> next != NULL) {
		temp = temp -> next;
	}
	temp -> next = newNode;
}

void insertAtPos(node **head, int pos, int value) {
	if (pos < 1) {
		printf("Invalid Position\n");
		return;
	}
	
	if (pos == 1) {
		insertAtFirst(head, value);
		return;
	}
	
	node *temp = *head;
	node *newNode = createNode(value);
	for (int i = 1; i < pos - 1; i++) {
		temp = temp -> next;
	}
	newNode -> next = temp -> next;
	temp -> next = newNode;
}

void deleteAtFirst(node **head) {
	if (*head == NULL) {
		printf("List is Empty\n");
		return;
	}
	
	node *temp = *head;
	*head = (*head) -> next;
	free(temp);
}

void deleteAtEnd(node **head) {
	if (*head == NULL) {
		printf("List is Empty\n");
		return;
	}
	
	if ((*head) -> next == NULL) {
		free(*head);
		*head = NULL;
		return;
	}
	
	node *temp = *head;
	while (temp -> next -> next != NULL) {
		temp = temp -> next;
	}
	
	free(temp -> next);
	temp -> next = NULL;	
}


void deleteAtPos(node **head, int pos) {
	if (pos < 1) {
		printf("Invalid Position\n");
		return;
	}
	
	if (pos == 1) {
		deleteAtFirst(head);
		return;
	}
	
	node *temp = *head;
	for (int i = 1; i < pos - 1; i++) {
		if (temp -> next == NULL) {
			printf("Position Out of Bounds\n");
			return;
		}
		temp = temp -> next;
	}
	
	if (temp->next == NULL) {
		printf("Position Out of Bounds\n");
		return;
	}
	
	node *toDelete = temp->next;
	temp -> next = temp -> next -> next;
	free(toDelete);
}

int main() {
	node *head = NULL;

	printf("Inserting at end: 10, 20, 30\n");
	insertAtEnd(&head, 10);
	insertAtEnd(&head, 20);
	insertAtEnd(&head, 30);
	display(&head);

	printf("Inserting at position 2: 15\n");
	insertAtPos(&head, 2, 15);
	display(&head);

	printf("Inserting at beginning: 5\n");
	insertAtFirst(&head, 5);
	display(&head);
	
	printf("Deleting first node\n");
	deleteAtFirst(&head);
	display(&head);
	
	printf("Deleting last node\n");
	deleteAtEnd(&head);
	display(&head);

	printf("Deleting node at position 2\n");
	deleteAtPos(&head, 2);
	display(&head);

	printf("Deleting node at position 5 (should fail)\n");
	deleteAtPos(&head, 5);
	display(&head);

	printf("Deleting all nodes...\n");
	deleteAtFirst(&head);
	deleteAtFirst(&head);
	display(&head);

	printf("Trying to delete from empty list\n");
	deleteAtEnd(&head);
	deleteAtPos(&head, 1);

	return 0;
}
