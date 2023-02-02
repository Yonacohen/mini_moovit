import Position1
class Station:
    def __init__(self, id_station, pos):
        self.id_station = id_station
        self.                                     = []              #buss list
        self.pos = pos

    def calc_dist(self,s2):
        res =  self.pos.calcdist3(s2.pos)

        return res

    def print_station(self):
         print("The id station is :", self.id_station)
         (self.pos).print_pos()

    def print_busses_in_station(self):
        print("The buses that pass by this" , self.id_station,"station:" )
        for x in self.busses_number:
            print(x,end = " : ")
        print("")

    def add_bus(self,new_bus_num):
        self.busses_number.append(new_bus_num)

    def delete_bus(self,delete_bus):
        self.busses_number.remove(delete_bus)











