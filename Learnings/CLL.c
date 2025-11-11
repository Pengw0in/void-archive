#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int data;
	struct node* next;
	struct node* prev;
}node;

node* createNode(int value){
	node* newNode = (node *)malloc(sizeof(node));
	if(!newNode) {
		printf("Memory allocation failed");
		return NULL;
	}
	
	newNode -> data = value;
	newNode -> next = NULL;
	newNode -> prev = NULL;
	
	return newNode;
}

void insertAtFirst(node **head ,int value) {
	node *newNode = createNode(value);
	if (*head == NULL) {
		*head = newNode;
		(*head) -> next = *head;
		return;
	}
	
	node *temp = *head;
	newNode -> next = *head;
	while (temp -> next != *head) {
		temp = temp -> next;
	}
	temp->next = newNode;
	*head = newNode;
}

void insertAtEnd(node **head, int value) {
	node *newNode = createNode(value);
	if (*head == NULL) {
		*head = newNode;
		(*head) -> next = *head;
		return;
	}
	
	node *temp = *head;
	while(temp -> next != *head) {
		temp = temp -> next;
	}
	temp -> next = newNode;
	newNode -> next = *head;
}

void insertAtPos(node **head, int value, int position) {
	node *newNode = createNode(value);
	if (position <= 0) {
		printf("Invalid position");
		return;
	}
	
	if (position == 1) {
		insertAtFirst(head, value);
		return;
	}
	
	node *temp = *head;
	for (int i = 1; i < position - 1; i++) {
		if(temp -> next == NULL) {
			printf("Out of Bounds");
		}
		temp = temp -> next;
	}
	newNode -> next = temp -> next;
	temp -> next = newNode;
}

void deleteAtFirst(node **head) {
	node *temp = *head;
	if (*head == NULL) {
		printf("List is empty");
		return;
	}
	
	if ((*head) -> next == (*head)) {
		free(*head);
		*head = NULL;
	} else {
		node *lastNode = *head;
		while(lastNode -> next != *head) {
			lastNode = lastNode -> next;
		}	
		*head = (*head) -> next;
		lastNode -> next = *head;
		free(temp);
	}
}

void deleteAtEnd(node **head) {
	if (*head == NULL) {
		printf("List is empty");
		return;
	}
	
	if ((*head) -> next == *head) {
		free(*head);
		*head = NULL;
		return;
	} else {
		node *temp = *head;
		node *prev = NULL;
		while (temp -> next != *head) {
			prev = temp;
			temp = temp ->next;
		}
		prev -> next = *head;
		free(temp);
	}
}

void deleteAtPos(node **head, int position) {
	if (position <= 0) {
		printf("Invalid position");
		return;
	}
	
	if (position == 1) {
		deleteAtFirst(head);
		return;
	}
	
	if (head == NULL) {
		printf("List is empty");
		return;
	}
	
	node *temp = *head;
	node *prev = NULL;
	
	for (int i = 1; i < position; i++) {
		if (temp -> next == *head) {
			printf("Out of Bounds");
			return;
		}
		prev = temp;
		temp = temp -> next;
	}
	prev -> next = temp -> next;
	free(temp);
}

void display(node **head) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    node *temp = *head;
    while (temp -> next != *head) {
        printf("%d <-> ", temp -> data);
        temp = temp ->next;
    } 
           
    printf("%d <-> head\n", temp -> data);
}

int main() {
    node *head = NULL;

    insertAtFirst(&head, 10);
    insertAtFirst(&head, 20);
    insertAtFirst(&head, 30);

    display(&head);

    deleteAtPos(&head, 2);
    display(&head);

    deleteAtFirst(&head);
    display(&head);

    deleteAtEnd(&head);
    display(&head);
   
    return 0;
}

