#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int value;
  struct Node* next;
} Node_t;

void printList(Node_t* n){
  while(n != NULL){
    printf("%d\n", n->value);
    n = n->next;
    // same as n = (*n).next;
  }
}


int main() {
  // head node
  Node_t* head = (Node_t*)malloc(sizeof(Node_t));

  head->value = 1;
  head->next = NULL;

  // next node
  Node_t* second = (Node_t*)malloc(sizeof(Node_t));

  second->value = 2;
  second->next = NULL;

  head->next = second;

  printList(head);

  free(head);
  free(second);
  return 0;
}
