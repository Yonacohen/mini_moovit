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


list_station = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9]



                       #kav,route[]
b1=Busses1.Busses(1,[list_station[3],list_station[5],list_station[7],list_station[9]])
b2=Busses1.Busses(2,[list_station[5],list_station[6],list_station[9]])
b3=Busses1.Busses(3,[list_station[0],list_station[3],list_station[6],list_station[7],list_station[9]])
b4=Busses1.Busses(4,[list_station[1],list_station[2],list_station[7],list_station[9]])
b5=Busses1.Busses(5,[list_station[4],list_station[5],list_station[8],list_station[9]])
b6=Busses1.Busses(6,[list_station[1],list_station[2],list_station[3],list_station[4],list_station[5],list_station[6]])



list_busses = [b1,b2,b3,b4,b5,b6]


for b in list_busses:
    b.update_station()

for s in list_station:
    s.print_busses_in_station()





































