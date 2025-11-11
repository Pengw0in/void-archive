#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	char data;
	struct node *left;
	struct node *right;
}node;

node* createNode(char value){
	node* newNode = (node*)malloc(sizeof(node));
	newNode -> data = value;
	newNode -> left = NULL;
	newNode -> right = NULL;
	
	return newNode;
}

node* findMin(node* root){
	while(root && root -> left != NULL)
		root = root -> left;
	return root;
}

node* insertNode(node* root, char key){
	if(root == NULL){
		return createNode(key);
	}
	if(key < root -> data){
		root -> left = insertNode(root -> left, key);
	} else if(key > root -> data){
		root -> right = insertNode(root -> right, key);
	}
	return root;
}

node* deleteNode(node* root, char key){
	if (root == NULL) return NULL;
	if(key < root -> data){
		root -> left = deleteNode(root -> left, key);
	} else if(key > root -> data){
		root -> right = deleteNode(root -> right, key);
	} else{
		if(root -> left == NULL){
			node* temp = root -> right;
			free(root);
			return temp;
		} else if(root -> right == NULL){
			node* temp = root -> left;
			free(root);
			return temp;
		}
		node* temp = findMin(root -> right);
		root -> data = temp -> data;
		root -> right = deleteNode(root -> right, temp -> data);
	}
	return root;
}


void inOrder(node* root){
	if(root == NULL) return;
	inOrder(root -> left);
	printf("%c ", root ->data);
	inOrder(root -> right);
}

int main(){
    node* root = NULL;

    root = createNode('U');
    insertNode(root, 'B');
    insertNode(root, 'C');
    insertNode(root, 'H');
    insertNode(root, 'L');
    insertNode(root, 'Z');
    insertNode(root, 'I');
    inOrder(root);
    printf("\n");
    root = deleteNode(root, 'Z');
    inOrder(root);
    
    return 0;
}