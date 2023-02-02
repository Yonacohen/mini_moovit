
import networkx as nx
import Busses1
import Position1
import Station1

# id_station,pos
s0=Station1.Station('A',Position1.Position(2,3))
s1=Station1.Station('B',Position1.Position(6,8))
s2=Station1.Station('C',Position1.Position(9,2))
s3=Station1.Station('D',Position1.Position(12,13))
s4=Station1.Station('E',Position1.Position(41,23))
s5=Station1.Station('F',Position1.Position(54,7))
s6=Station1.Station('G',Position1.Position(25,11))
s7=Station1.Station('H',Position1.Position(23,13))
s8=Station1.Station('I',Position1.Position(66,55))
s9=Station1.Station('J',Position1.Position(85,44))
s10=Station1.Station('K',Position1.Position(55,38))


list_station = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
#add node to graph
G = nx.Graph()
for add in list_station:
    G.add_node(add)


G.add_weighted_edges_from([(s0, s1, s0.calc_dist(s1)),
                           (s1,s2,s1.calc_dist(s2)),
                           (s1, s3,s1.calc_dist(s3)),
                           (s0, s3, s0.calc_dist(s3),
                            )])

arrStations = nx.dijkstra_path(G, s0, s3)
print('frrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
for x in arrStations:
     x.print_station()


                       #kav,route[]
b1=Busses1.Busses(1,[list_station[3],list_station[5],list_station[7],list_station[9]])
b2=Busses1.Busses(2,[list_station[5],list_station[6],list_station[9],list_station[10]])
b3=Busses1.Busses(3,[list_station[0],list_station[3],list_station[6],list_station[7],list_station[9]])
b4=Busses1.Busses(4,[list_station[1],list_station[2],list_station[7],list_station[9]])
b5=Busses1.Busses(5,[list_station[4],list_station[5],list_station[8],list_station[9],list_station[10]])
b6=Busses1.Busses(6,[list_station[1],list_station[2],list_station[3],list_station[4],list_station[5],list_station[6]])
b7=Busses1.Busses(7,[list_station[3],list_station[5],list_station[8],list_station[9],list_station[10]])
b8=Busses1.Busses(8,[list_station[10],list_station[9],list_station[3],list_station[9],list_station[1]])




list_busses = [b1,b2,b3,b4,b5,b6,b7,b8]


for b in list_busses:
    b.update_station()

for s in list_station:
    s.print_busses_in_station()


p0=Position1.Position(0,0)
p1=Position1.Position(3,2)
p2=Position1.Position(6,4)
p3=Position1.Position(9,6)
p4=Position1.Position(12,80)
p5=Position1.Position(15,10)
p6=Position1.Position(18,12)
p7=Position1.Position(21,14)

list_pos=[p0,p1,p2,p3,p4,p5,p6,p7]


for p in list_pos:
    p.print_pos()







































