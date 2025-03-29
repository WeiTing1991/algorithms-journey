#include <stdio.h>
#define SIZE 5
int queue[SIZE], front = 0, rear = 0;

void enqueue(int val) {
  if (rear == SIZE) {
      printf("Queue is Full\n");
      return;
  }
  queue[rear++] = val;
}

int dequeue() {
  if (front == rear) {
    printf("Queue is Empty\n");
    return -1;
  }
  return queue[front++];
}

int main() {
  enqueue(10);
  enqueue(20);
  printf("%d\n", dequeue()); // Output: 10
}
