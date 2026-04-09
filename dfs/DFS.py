import time
from dfs.GraphViewer import GraphViewer

class HospitalGraph:
    def __init__(self):
        self.adj_list = {
            1: [2],
            2: [4],
            # 3: [5],
            4: [8],
            # 5: [6, 8, 12],
            6: [7, 10, 11, 9, 12],
            7: [8],
            8: [7, 12],
            9: [12],
            10: [12],
            11: [12],
            12: []
        }
        self.vertex_names = {
            1: "Assessment",   
            2: "ER Triage",     
            3: "OPD Triage",
            4: "Basic Test",   
            5: "Family Medicine", 
            6: "Additional Tests",
            7: "Surgery Doc",      
            8: "Hospitalized",   
            9: "Pediatrics",
            10: "Internal",   
            11: "Geriatrics",    
            12: "Release the patient from medical care"
        }

    def name(self, v):
        return self.vertex_names[v]

    def active_names(self, stack):
        return [self.name(v) for v in stack if v is not None]

    def handle_finish(self, current_vertex, stack, timer, color, discovery_time, finish_time):
        timer[0] += 1
        finish_time[current_vertex] = timer[0]
        color[current_vertex] = "BLACK"

        print(f"\n  ✦ FINISH: {self.name(current_vertex)}"
              f"  [d={discovery_time[current_vertex]}, f={finish_time[current_vertex]}]"
              f"  |  color → BLACK")
        print(f"    stack: {self.active_names(stack)}")

    def handle_discover(self, current_vertex, stack, timer, color, discovery_time, visited_order):
        time.sleep(0.3)
        timer[0] += 1
        discovery_time[current_vertex] = timer[0]
        color[current_vertex] = "GRAY"
        visited_order.append(current_vertex)

        print(f"\n>>> DISCOVER: {self.name(current_vertex)}"
              f"  d={discovery_time[current_vertex]} | color → GRAY")
        print(f"    visited : {[self.name(v) for v in visited_order]}")

        stack.append(current_vertex)
        stack.append(None)

        for neighbor in self.adj_list[current_vertex]:
            if color[neighbor] == "WHITE":
                stack.append(neighbor)
                print(f"    push  : {self.name(neighbor)}")
            else:
                print(f"    skip  : {self.name(neighbor)} ({color[neighbor]})")

        print(f"\n    stack : {self.active_names(stack)}")

    def handle_skip(self, v, color):
        print(f"\n--- SKIP (already {color[v]}): {self.name(v)}")

    def print_summary(self, color, discovery_time, finish_time, visited_order):
        print("\n" + "=" * 55)
        print("  DFS vertex summary")
        print("=" * 55)
        print(f"  {'Vertex':<20} {'discovery time':>15}  {'finished time':>15}")
        print("  " + "-" * 45)

        for v in self.adj_list:
            d = discovery_time[v] if discovery_time[v] is not None else "-"
            f = finish_time[v]    if finish_time[v]    is not None else "-"
            print(f"  {self.name(v):<20} {str(d):>15}  {str(f):>15}")

        print(f'\nDFS Traversal {[self.name(v) for v in visited_order]}')

    def dfs(self, start_vertex):
        color          = {v: "WHITE" for v in self.adj_list}
        discovery_time = {v: None    for v in self.adj_list}
        finish_time    = {v: None    for v in self.adj_list}
        visited_order  = []
        timer          = [0]

        stack = [start_vertex]

        print("=" * 55)
        print("  DFS TRAVERSAL — Hospital Patient Workflow")
        print("=" * 55)
        print(f"\nStarting from: {self.name(start_vertex)}")
        print(f"Initial Stack: [{self.name(start_vertex)}]\n")

        while stack:
            item = stack.pop()

            if item is None:
                current = stack.pop()
                self.handle_finish(current, stack, timer, color,
                                   discovery_time, finish_time)

            elif color[item] == "WHITE":
                self.handle_discover(item, stack, timer, color,
                                     discovery_time, visited_order)

            else:
                self.handle_skip(item, color)

        self.print_summary(color, discovery_time, finish_time, visited_order)

    def detect_cycles(self):
        cycles    = []
        seen      = set()   
 
        print("=" * 55)
        print("  CYCLE DETECTION — Hospital Patient Workflow")
        print("=" * 55)
 
        for start in self.adj_list:
            color     = {v: "WHITE" for v in self.adj_list}
            gray_path = []
            stack     = [start]
 
            while stack:
                item = stack.pop()
 
                if item is None:
                    current = stack.pop()
                    color[current] = "BLACK"
                    gray_path.pop()   
                    continue
 
                if color[item] == "WHITE":
                    color[item] = "GRAY"
                    gray_path.append(item)   
 
                    stack.append(item)
                    stack.append(None)
 
                    for neighbor in reversed(self.adj_list[item]):
                        if color[neighbor] == "WHITE":
                            stack.append(neighbor)
                        elif color[neighbor] == "GRAY":
                            cycle = gray_path[gray_path.index(neighbor):] + [neighbor]
 
                            body    = cycle[:-1]
                            min_idx = body.index(min(body))
                            rotated = body[min_idx:] + body[:min_idx] + [body[min_idx]]
 
                            key = tuple(rotated)
                            if key not in seen:
                                seen.add(key)
                                cycles.append(rotated)
 
        if not cycles:
            print("\n  No cycles detected.")
        else:
            print(f"\n  Found {len(cycles)} cycle(s):\n")
            for i, cycle in enumerate(cycles, 1):
                path_str = " → ".join(self.name(n) for n in cycle)
                print(f"  Cycle {i}: {path_str}")
                print()
 
        print("=" * 55)
    
    def print_graph(self, age= None, gender = None, urgent = None):
        graph = GraphViewer(graph_nodes=self.adj_list)
        if age == None and gender == None and urgent == None:
            graph.view_all_graph()
        if urgent == 'y':
            graph.view_er_graph(age=age)
        elif urgent == 'n':
            graph.view_non_er_graph(age=age)
