#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	char data;
	struct node *left;
	struct node *right;
}node;

node* createNode(char value){
	node* newNode = (node*)malloc(sizeof(node));
	newNode -> data = char;
	newNode -> left = NULL;
	newNode -> right = NULL;
	
	return newNode; 
}

node* findMin(node* root){
	while(root && root -> left != NULL){
		root = root -> left;
	}
	return root;
}

node* insertNode(node* root, char value){
	if(root == NULL){
		createNode(value);
	}
	if(value < root -> data){
		root -> left = insertNode(root -> left, value);
	} else if(value > root -> data){
		root -> right = insertNode(root -> right, value);
	}
	return root;
}

node* deleteNode(node* root, char value){
	if(root == NULL) return NULL;
	if(value < root -> data){
		root -> left = deleteNode(root -> left, value);
	} else if(value > root -> data){
		root -> right = deleteNode(root -> right, value);
	} else{
		if(root -> left == NULL){
			node* temp = root -> right;
			free(root);
			return temp;
		} else if(root -> right == NULL){
			node* temp = root -> left;
			free(root);
			return left;
		}
		node* temp = findMin(root -> right);
		root -> data = temp -> data;
		root -> right = deleteNode(root -> right, temp -> data);		
	}
	return root;
}

int main(){

	return 0;
}