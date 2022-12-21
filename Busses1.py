import Station1
class Busses:


    def __init__(self,kav,route):
        self.kav=kav
        self.route=route                           # list of station (id_station, busses_number, pos)
        self.first_station=route[0]
        self.last_station=route[-1]
        self.price = round( 2 *(self.first_station.calc_dist(self.last_station)),2)

    def update_station(self):
        for x in self.route:
            x.add_bus(self.kav)


    def print_bus(self):
        print("Kav is" ,self.kav," |  Price is:  ",self.price)
        print("First station:" , self.first_station.id_station ,"|" ,"Last station:  ",self.last_station.id_station)
        self.print_route()



    def print_route(self):
        print("The busses that pass by the station :  " , end = " ")

        for x in self.route:
            print (x.id_station,",", end="  ")
        print("")
        print("")


    def calc_price(self):
       d = self.first_station.calc_dist(self.last_station)
       return d * 2















