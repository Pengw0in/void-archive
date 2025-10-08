import os
import networkx as nx
import plotly.graph_objects as go
from git import Repo

def create_commit_graph(repo_path):
    """Create a directed graph from Git repository's commit history."""
    repo = Repo(repo_path)
    G = nx.DiGraph()
    labels = {}
    
    try:
        # Fetch only the last 100 commits from the 'master' branch
        commits = list(repo.iter_commits('master', max_count=100))
        for commit in commits:
            commit_hash = commit.hexsha[:7]
            commit_message = commit.message.split('\n')[0].strip()
            G.add_node(commit_hash)
            labels[commit_hash] = f"{commit_hash}: {commit_message}"
            
            # Add parent-child relationship if parent exists
            for parent in commit.parents:
                parent_commit = parent.hexsha[:7]
                # Only add edge if parent exists in the graph
                if parent_commit in G:
                    G.add_edge(commit_hash, parent_commit)
                else:
                    # If parent not in the graph yet, handle it
                    print(f"Warning: Parent commit {parent_commit} not found in the graph for commit {commit_hash}")
            
        return G, labels
    except Exception as e:
        print(f"Error creating commit graph: {str(e)}")
        return None, None

def draw_commit_graph(G, labels):
    """Draw hierarchical visualization of commit graph."""
    if not G or not labels:
        print("No graph data to visualize.")
        return
    
    # Use hierarchical layout
    pos = nx.spring_layout(G.reverse(), k=1, iterations=50)  # Reverse again for display
    
    # Normalize positions to spread them out more evenly
    x_coords = [coord[0] for coord in pos.values()]
    y_coords = [coord[1] for coord in pos.values()]
    x_range = max(x_coords) - min(x_coords)
    y_range = max(y_coords) - min(y_coords)
    
    # Scale positions
    scale_factor = 2.0
    pos = {node: (coord[0] * scale_factor / x_range, coord[1] * scale_factor / y_range) 
           for node, coord in pos.items()}
    
    x_vals = [pos[node][0] for node in G.nodes()]
    y_vals = [pos[node][1] for node in G.nodes()]
    
    # Create edges
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    # Simple edges
    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1, color='black'),
        hoverinfo='none',
        mode='lines'
    )
    
    # Nodes with labels
    node_trace = go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='markers+text',
        text=[labels[node] for node in G.nodes()],
        textposition="top center",
        textfont=dict(
            family="monospace",
            size=10,
            color='black'
        ),
        marker=dict(
            size=6,
            color='white',
            line=dict(color='black', width=1),
            symbol='circle'
        )
    )
    
    # Clean layout
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            showlegend=False,
            hovermode='closest',
            plot_bgcolor='rgb(240, 240, 240)',
            paper_bgcolor='rgb(240, 240, 240)',
            xaxis=dict(
                showgrid=False, 
                zeroline=False, 
                showticklabels=False,
                range=[-1.5, 1.5]
            ),
            yaxis=dict(
                showgrid=False, 
                zeroline=False, 
                showticklabels=False,
                range=[-1.5, 1.5]
            ),
            margin=dict(l=20, r=20, b=20, t=20),
            width=1200,
            height=800
        )
    )
    
    fig.show()

def main():
    """Main function to run the script."""
    try:
        repo_path = input("Enter the path to your git repository: ").strip()
        
        if not os.path.exists(repo_path):
            print(f"Error: Repository path '{repo_path}' does not exist.")
            return
            
        if not os.path.exists(os.path.join(repo_path, '.git')):
            print(f"Error: '{repo_path}' is not a Git repository.")
            return
        
        G, labels = create_commit_graph(repo_path)
        draw_commit_graph(G, labels)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
