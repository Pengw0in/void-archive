package main

import (
    "container/heap"
    "math"
    rl "github.com/gen2brain/raylib-go/raylib"
)

// Node represents a grid cell in the LPA* algorithm
type Node struct {
    position rl.Vector2
    g        float64  // Cost from start
    rhs      float64  // Right-hand side value
    inQueue  bool     // Whether node is in priority queue
}

// Key represents priority queue ordering
type Key struct {
    k1, k2 float64
}

// LPAStar implements the LPA* algorithm
type LPAStar struct {
    grid        map[rl.Vector2]*Node
    start       rl.Vector2
    goal        rl.Vector2
    queue       PriorityQueue
    obstacles   map[rl.Vector2]bool  // Dynamic obstacles (snake segments)
    km          float64              // Key modifier for efficiency
}

// Priority queue implementation
type PriorityQueue []*QueueItem

type QueueItem struct {
    node *Node
    key  Key
}

// Heuristic function (Manhattan distance for grid)
func (lpa *LPAStar) heuristic(from, to rl.Vector2) float64 {
    return math.Abs(float64(from.X-to.X)) + math.Abs(float64(from.Y-to.Y))
}

// Calculate key for priority queue ordering
func (lpa *LPAStar) calculateKey(node *Node) Key {
    minVal := math.Min(node.g, node.rhs)
    return Key{
        k1: minVal + lpa.heuristic(node.position, lpa.goal) + lpa.km,
        k2: minVal,
    }
}

// Get neighbors of a position
func (lpa *LPAStar) getNeighbors(pos rl.Vector2) []rl.Vector2 {
    neighbors := []rl.Vector2{}
    directions := []rl.Vector2{
        {X: 0, Y: -cellHeight}, // Up
        {X: 0, Y: cellHeight},  // Down
        {X: -cellWidth, Y: 0},  // Left
        {X: cellWidth, Y: 0},   // Right
    }
    
    for _, dir := range directions {
        newPos := rl.Vector2{X: pos.X + dir.X, Y: pos.Y + dir.Y}
        // Check bounds
        if newPos.X >= 0 && newPos.X < screenWidth && 
           newPos.Y >= 0 && newPos.Y < screenHeight {
            neighbors = append(neighbors, newPos)
        }
    }
    return neighbors
}

// Cost between adjacent nodes
func (lpa *LPAStar) cost(from, to rl.Vector2) float64 {
    if lpa.obstacles[to] {
        return math.Inf(1) // Infinite cost for obstacles
    }
    return 1.0 // Unit cost for free cells
}

// Update vertex (core LPA* operation)
func (lpa *LPAStar) updateVertex(node *Node) {
    if node.position != lpa.start {
        node.rhs = math.Inf(1)
        for _, pred := range lpa.getNeighbors(node.position) {
            predNode := lpa.getNode(pred)
            cost := lpa.cost(pred, node.position)
            node.rhs = math.Min(node.rhs, predNode.g + cost)
        }
    }
    
    // Remove from queue if present
    if node.inQueue {
        lpa.removeFromQueue(node)
    }
    
    // Add to queue if inconsistent
    if node.g != node.rhs {
        lpa.addToQueue(node)
    }
}

// Main LPA* computation
func (lpa *LPAStar) computeShortestPath() {
    for !lpa.queue.Empty() && 
        (lpa.compareKeys(lpa.queue.TopKey(), lpa.calculateKey(lpa.getNode(lpa.goal))) || 
         lpa.getNode(lpa.goal).rhs != lpa.getNode(lpa.goal).g) {
        
        u := lpa.queue.Pop()
        
        if u.g > u.rhs {
            // Overconsistent case
            u.g = u.rhs
            for _, succ := range lpa.getNeighbors(u.position) {
                lpa.updateVertex(lpa.getNode(succ))
            }
        } else {
            // Underconsistent case
            u.g = math.Inf(1)
            
            // Update u itself
            lpa.updateVertex(u)
            
            // Update successors
            for _, succ := range lpa.getNeighbors(u.position) {
                lpa.updateVertex(lpa.getNode(succ))
            }
        }
    }
}

// Update obstacles (when snakes move)
func (lpa *LPAStar) updateObstacles(newObstacles map[rl.Vector2]bool) {
    // Find changed cells
    changedCells := []rl.Vector2{}
    
    // Check for newly blocked cells
    for pos := range newObstacles {
        if !lpa.obstacles[pos] {
            changedCells = append(changedCells, pos)
        }
    }
    
    // Check for newly freed cells
    for pos := range lpa.obstacles {
        if !newObstacles[pos] {
            changedCells = append(changedCells, pos)
        }
    }
    
    lpa.obstacles = newObstacles
    
    // Update affected vertices
    for _, pos := range changedCells {
        node := lpa.getNode(pos)
        lpa.updateVertex(node)
        
        // Update neighbors
        for _, neighbor := range lpa.getNeighbors(pos) {
            lpa.updateVertex(lpa.getNode(neighbor))
        }
    }
    
    lpa.computeShortestPath()
}

// Get next move towards goal
func (lpa *LPAStar) getNextMove(currentPos rl.Vector2) rl.Vector2 {
    bestNext := currentPos
    bestCost := math.Inf(1)
    
    for _, neighbor := range lpa.getNeighbors(currentPos) {
        node := lpa.getNode(neighbor)
        totalCost := lpa.cost(currentPos, neighbor) + node.g
        
        if totalCost < bestCost {
            bestCost = totalCost
            bestNext = neighbor
        }
    }
    
    return bestNext
}