#include <stdio.h>
#include <stdlib.h>
#define SIZE 10

typedef struct Hashtable{
	int keys[SIZE];
	int values[SIZE];
	int occupied[SIZE];
}Hashtable;

void initializeTable(Hashtable* table){
	for(int i = 0; i < SIZE; i++){
		table -> keys[i] = -1;
		table -> values[i] = -1;
		table -> occupied[i] = 0;
	}
}

int hash(int key){
	return key % SIZE;
}

void insert(Hashtable *table , int key, int value){
	int index = hash(key);
	
	while(table -> occupied[index]){
		index = (index + 1) % SIZE;
	}
	
	table -> keys[index] = key;
	table -> values[index] = value;
	table -> occupied[index] = 1;
}

void search()

int main(){
	
	return 0;
}