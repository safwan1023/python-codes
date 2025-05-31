import math

def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor(locations):
    """Greedy algorithm to solve a simple TSP."""
    n = len(locations)
    visited = [False] * n
    route = [0]  # start from the first location
    visited[0] = True
    total_distance = 0.0

    current = 0
    for _ in range(n - 1):
        nearest = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i]:
                dist = distance(locations[current], locations[i])
                if dist < min_dist:
                    min_dist = dist
                    nearest = i
        route.append(nearest)
        visited[nearest] = True
        total_distance += min_dist
        current = nearest

    # Return to the starting point
    total_distance += distance(locations[current], locations[0])
    route.append(0)

    return route, total_distance

# --- Runtime Input Section ---

def get_input_locations():
    print("Enter number of delivery locations (including starting point):")
    n = int(input("Number of locations: "))
    locations = []

    for i in range(n):
        x = float(input(f"Enter X coordinate of location {i+1}: "))
        y = float(input(f"Enter Y coordinate of location {i+1}: "))
        locations.append((x, y))

    return locations

# --- Main Execution ---

if __name__ == "__main__":
    print("📦 Delivery Route Optimizer (Greedy AI Approximation)")
    locations = get_input_locations()
    route, total_distance = nearest_neighbor(locations)

    print("\nOptimized Delivery Route (by indices):")
    print(" -> ".join(str(i + 1) for i in route))  # +1 to make human-readable
    print(f"Total Estimated Distance: {total_distance:.2f} units")
