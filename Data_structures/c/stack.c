#include <stdio.h>

#define SIZE 5

int stack[SIZE], top = -1;

void push(int data) {
  if (top == SIZE - 1) {

    printf("Stack Overflow\n");
    return;
  }
  stack[++top] = data;
}

int pop(int data) {
  if (top == -1) {
    printf("Stack Underflow\n");
    return -1;
  }
  return stack[top--];
}

void printStack() {
  for (int i = 0; i <= top; i++) {
    printf("Current Stack: %d\n", stack[i]);
  }
}

int main() {
  push(10);
  push(20);

  printf("Current top: %d\n", stack[top]);

  printStack();
  pop(20);

  printf("Current top: %d\n", stack[top]);

  printStack();
}
