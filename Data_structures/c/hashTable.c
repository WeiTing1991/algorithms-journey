#include <stdio.h>

#define SIZE 5

struct HashTable {
  char key;
  int value;
} table[SIZE];

void insert(char key, int value){
  int index = key % SIZE;
  table[index].key = key;
  table[index].value = value;
}

void printTable() {
  for (int i = 0; i < SIZE; i++) {
    printf("Key: %c, Value: %d\n", table[i].key, table[i].value);
  }
}
int main() {
  insert('a', 1);
  insert('b', 2);
  insert('c', 3);
  printTable();
}


