#include <stdio.h>

#define V 5

void addEdge(int graph[V][V], int u, int v) {
    graph[u][v] = 1;
    graph[v][u] = 1;
}

int main() {
    int graph[V][V] = {0};
    addEdge(graph, 0, 1);
    printf("%d\n", graph[0][1]); // Output: 1
}
