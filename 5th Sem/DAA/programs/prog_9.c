#include <stdio.h>
#include <stdlib.h>
#define INF 99999
struct Edge {
 int src, dest, weight;
};
struct Graph {
 int V, E;
 struct Edge* edge;
};
struct Graph* createGraph(int V, int E)
{
 struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
 graph->V = V;
 graph->E = E;
 graph->edge = (struct Edge*)malloc(sizeof(struct Edge) * E);
 return graph;
}
void printArr(int dist[], int V)
{
 printf("Vertex Distance from Source\n");
 for (int i = 0; i < V; ++i)
 printf("%d \t\t %d\n", i, dist[i]);
}
void bellmanFord(struct Graph* graph, int src)
{
 int V = graph->V;
 int E = graph->E;
 int dist[V];
 for (int i = 0; i < V; i++)
 dist[i] = INF;
 dist[src] = 0;
 for (int i = 1; i <= V - 1; i++) {
 for (int j = 0; j < E; j++) {
 int u = graph->edge[j].src;
 int v = graph->edge[j].dest;
 int weight = graph->edge[j].weight;
 if (dist[u] != INF && dist[u] + weight < dist[v])
 dist[v] = dist[u] + weight;
 } }
 for (int i = 0; i < E; i++) {
 int u = graph->edge[i].src;
 int v = graph->edge[i].dest;
 int weight = graph->edge[i].weight;
 if (dist[u] != INF && dist[u] + weight < dist[v]) {
 printf("Graph contains negative weight cycle");
 return;
 }
 }
 printArr(dist, V);
 return;
}
int main()
{
 int V = 5;
 int E = 8;
 struct Graph* graph = createGraph(V, E);
 graph->edge[0].src = 0;
 graph->edge[0].dest = 1;
 graph->edge[0].weight = 5;
 graph->edge[1].src = 0;
 graph->edge[1].dest = 2;
 graph->edge[1].weight = 4;
 graph->edge[2].src = 1;
 graph->edge[2].dest = 3;
 graph->edge[2].weight = 3;
 graph->edge[3].src = 2;
 graph->edge[3].dest = 1;
 graph->edge[3].weight = 6;
 graph->edge[4].src = 3;
 graph->edge[4].dest = 2;
 graph->edge[4].weight = 2;
 graph->edge[5].src = 3;
 graph->edge[5].dest = 4;
 graph->edge[5].weight = -1;
 graph->edge[6].src = 4;
 graph->edge[6].dest = 0;
 graph->edge[6].weight = 2;
 graph->edge[7].src = 4;
 graph->edge[7].dest = 1;
 graph->edge[7].weight = -4;
 bellmanFord(graph, 0);
 return 0;
}
