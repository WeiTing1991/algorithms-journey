#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node *left;
  struct Node *right;
};

struct Node *newNode(int data) {
  struct Node *node = (struct Node *)malloc(sizeof(struct Node));
  node->data = data;
  node->left = node->right = NULL;
  return node;
}

int main() {
  struct Node *root = newNode(10);
  root->left = newNode(5);
  root->right = newNode(15);
  printf("%d\n", root->left->data); // Output: 5
}
