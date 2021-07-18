

class Laptop():
    """ This is a class of Laptop

    we have the blue print of laptop that was designed
    """
    build_by = ""
    ram = ""
    battery = ""
    screen = ""
    processer = ""

    def info(self):
        """This Function provides info about the laptops 
        
        This gives the details of the laptop
        """
        print("Hi i am the laptop")
        print("i am build by ",self.build_by)
        print("I have a  ram of ",self.ram)
        print("I have a battery capacity of ",self.battery)
        print("I have a screen of ",self.screen)
        print("I have the processer of ",self.processer)    


hpLaptop = Laptop()
hpLaptop.processer = "Intel-i7"
hpLaptop.ram = "16 GB"
hpLaptop.screen="1080 X 960"
hpLaptop.battery = "5000Mah"
hpLaptop.build_by = "HP"

Dell = Laptop()
Dell.processer = "Intel-i11"
Dell.ram = "8 GB"
Dell.screen="2080 X 960"
Dell.battery = "4000Mah"
Dell.build_by = "Dell"

Mac = Laptop()
Mac.processer = "Intel-i11 10gen"
Mac.ram = "32 GB"
Mac.screen="4080 X 2960"
Mac.battery = "4000Mah"
Mac.build_by = "Mac"


Mac.info()