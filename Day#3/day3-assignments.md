## 1 Pick any one of the algorithm from the units 3 / 4 / 5
###  Enter the choosen algorithm
###  Create a docker image for the same and push the same to dockerhub.
###  Add the screenshots here

✅ I'll choose **Dijkstra’s Algorithm** (Shortest Path Algorithm) from **Graph Algorithms**.

---

### Step 1: Create a Simple Python Program for Dijkstra's Algorithm

**`dijkstra.py`**
```python
import sys

def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in graph}
    D[start_vertex] = 0

    visited = set()

    while visited != set(graph.keys()):
        min_vertex = None
        for vertex in graph:
            if vertex not in visited:
                if min_vertex is None:
                    min_vertex = vertex
                elif D[vertex] < D[min_vertex]:
                    min_vertex = vertex

        for neighbor, cost in graph[min_vertex].items():
            if cost + D[min_vertex] < D[neighbor]:
                D[neighbor] = cost + D[min_vertex]
        visited.add(min_vertex)

    return D

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)
    print(f"Shortest distances from {start_vertex}: {distances}")
```

---

### Step 2: Create a `Dockerfile`

**`Dockerfile`**
```dockerfile
# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY dijkstra.py .

# Run the script
CMD ["python", "dijkstra.py"]
```

---

### Step 3: Build the Docker Image

Open your terminal and run:

```bash
docker build -t yourdockerhubusername/dijkstra-algorithm .
```

---

### Step 4: Run and Test the Docker Image Locally

```bash
docker run yourdockerhubusername/dijkstra-algorithm
```

✅ You should see output like:
```
Shortest distances from A: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

---

### Step 5: Push the Docker Image to DockerHub

First, login to DockerHub:

```bash
docker login
```

Then push your image:

```bash
docker push yourdockerhubusername/dijkstra-algorithm
```

---

### Step 6: Screenshots to Take 📸
You need to capture:
1. Dockerfile and Python code screenshot.
2. Docker build success screenshot.
3. Docker run output screenshot.
4. Docker push to DockerHub success screenshot.
5. DockerHub repository showing the pushed image.

---

