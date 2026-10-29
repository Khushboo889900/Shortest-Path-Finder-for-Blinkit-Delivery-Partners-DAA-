from flask import Flask, render_template, request, jsonify
import heapq
app = Flask(__name__)

# Illustrative demo distances in kilometres; not live map data.
NODES = {
 "Store":{"Sector 1":1.2,"Sector 2":2.0,"Market":1.7},
 "Sector 1":{"Store":1.2,"Sector 3":1.1,"Market":0.8},
 "Sector 2":{"Store":2.0,"Market":0.9,"Sector 4":1.4},
 "Sector 3":{"Sector 1":1.1,"Market":1.0,"Customer A":1.6,"Sector 5":1.3},
 "Market":{"Store":1.7,"Sector 1":0.8,"Sector 2":0.9,"Sector 3":1.0,"Sector 4":1.2},
 "Sector 4":{"Sector 2":1.4,"Market":1.2,"Customer B":1.1,"Sector 5":0.7},
 "Sector 5":{"Sector 3":1.3,"Sector 4":0.7,"Customer A":1.0,"Customer B":1.5},
 "Customer A":{"Sector 3":1.6,"Sector 5":1.0},
 "Customer B":{"Sector 4":1.1,"Sector 5":1.5}
}
def dijkstra(graph,start,end):
    dist={n:float("inf") for n in graph}; prev={}; dist[start]=0; queue=[(0,start)]; seen=set()
    while queue:
        d,u=heapq.heappop(queue)
        if u in seen: continue
        seen.add(u)
        if u==end: break
        for v,w in graph[u].items():
            if d+w<dist[v]:
                dist[v]=d+w; prev[v]=u; heapq.heappush(queue,(dist[v],v))
    if dist[end]==float("inf"): return None,None
    path=[]; cur=end
    while cur!=start: path.append(cur); cur=prev[cur]
    path.append(start); path.reverse()
    return path,round(dist[end],2)

@app.route("/")
def home(): return render_template("index.html",nodes=list(NODES),graph=NODES)
@app.route("/api/route",methods=["POST"])
def calculate_route():
    data=request.get_json(silent=True) or {}; start=data.get("start"); end=data.get("end")
    if start not in NODES or end not in NODES: return jsonify(error="Choose valid locations."),400
    if start==end: return jsonify(error="Start and destination must be different."),400
    path,distance=dijkstra(NODES,start,end)
    if path is None: return jsonify(error="No route found."),404
    eta=max(1,round(distance/18*60+2))
    return jsonify(start=start,destination=end,path=path,distance_km=distance,eta_minutes=eta,
      stops=max(0,len(path)-2),algorithm="Dijkstra's Algorithm",
      note="Demo route with sample distances. Not live GPS or official Blinkit routing.")
if __name__=="__main__": app.run(debug=True)
