def outer ():
    name ="Ashik"
    def inner () :
        print(name) 
    return inner
func = outer()
func()

