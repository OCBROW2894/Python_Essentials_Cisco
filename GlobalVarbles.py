"""
-GLOBAL VARIABLES - Variables created outside a function

"""

x = "Naruto";

def bestAnime():
    print(x, " is my First Anime"); #I am Split between naruto and One Piece so I just changed the output

y="Rolls Royes";
def dreamCar():
    y="Bentely";
    print(y, " Is My Dream Car");

z="Pilot";
def myDream():
    global z;
    z="Mad Tech Scientist";
    print("Lazima nikue a ",z);

bestAnime();
dreamCar();
myDream();

print("I must be a ",z);
