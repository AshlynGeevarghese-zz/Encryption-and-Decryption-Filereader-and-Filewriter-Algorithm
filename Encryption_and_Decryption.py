from random import randint

class Nutrient:

    def __init__(self):
        self.hasMoved = False
    def getMoved(self):
        return self.hasMoved
    def setMoved(self):
        self.hasMoved = True
    def clearMoved(self):
        self.hasMoved = False;


class Microbe:
    def __init__(self):
        self.heldNutrient = None
    def hasNutrient(self):
        if(microbe.hasNutrient):
            return True
        else:
            return False
    def takeNutrient(self, nutrient):
        nutrient = self.heldNutrient
    def consumeNutrient(self):
        self.heldNutrient = None



class PetriCell:
    def __init__(self):
        self.microbe = None
        self.nutrients = []
    def getMicrobe(self):
        return self.microbe
    def hasMicrobe(self):
        if self.microbe != None:
             return True
        else:
            return False
    def createMicrobe(self):
        self.microbe = Microbe()
    def getNutrient(self):
        if len(self.nutrients) > 0:
            return self.nutrients.pop()
        else:
            return None
    def getUnmoved(self):
        list = []
        for nutrient in self.nutrients:
            if(self.nutrients.hasMoved == False):
                list.append(nutrient)
                self.nutrient.remove(nutrient)
        return list
    def clearAllMoved(self):
        for nutrient in self.nutrients:
            nutrient.clearMoved()
    def hasNutrients(self):
        a = len(self.nutrients)
        if (a>0):
            return True
        else:
            return False
    def placeNutrient(self, nutrient):
        self.nutrients.append(nutrient)
    def __str__(self):
        self.status = ""
        if self.microbe:
            self.status += "M"
        else:
            self.status += "_"
        self.status += str(len(self.nutrients)) + "N"
        return self.status

class PetriDish:
    def __init__(self, x, y, concentration, microbes):
        self.grid = []
        #Creating the grid
        for j in range(y):
            row = []
            for i in range(x):
                row.append(PetriCell())
            self.grid.append(row)
        newnutrient = int(concentration * x * y )
        for one in range(newnutrient):
            a = randint(0, x-1)
            b = randint(0, y-1)
            self.grid[a][b].placeNutrient(Nutrient())
        for micro in microbes:
            self.grid[micro[0]][micro[1]].createMicrobe()
        

        #Add your code here
    def moveNutrients(self):
        for x in self.grid:
            for y in self.grid:
                if (self.grid[x][y].hasNutrients()):
                    for nutrient in self.grid[x][y].getUnmoved():
                        nutrient.setMoved()
                        move = randint(0,2)
                        if (move == 0):
                            if (x+1<len(self.grid)):
                                vertx = x+1
                            else:
                                vertx = x
                        elif(move==1):
                            vertx = x
                        else:
                            if (x-1>=0):
                                vertx = x-1
                            else:
                                vertx = x

                        move2 = randintt(1,2)

                        if(move2==0):
                            if(y+1<len(self.grid)):
                                verty = y + 1
                            else:
                                verty = y
                        elif (move2==1):
                            verty = y
                        else:
                            if(y-1>=0):
                                verty = y-1
                            else:
                                verty = y
                        self.grid[vertx][verty].placeNutrient(nutrient)
        for x in self.grid:
            for y in self.grid:
                self.grid[x][y].hasMoved = False
    def checkMicrobes(self):
        newmicrobe = []
        for x in self.grid:
            for y in self.grid:
                var = self.grid[x][y].getMicrobe()
                if(var != None and var.hasNutrient()==False):
                    if (self.grid[x][y].hasNutrient()):
                            var.takeNutrient(self.grid[x][y].getNutrient())
                            movements = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(1,1),(-1,-1)]
                            newmicrobe.append(movements)
                            if (x-1<0):
                                newmicrobe.remove((-1,0))
                                newmicrobe.remove((1,1))
                            if(y-1<0):
                                newmicrobe.remove((0,-1))
                                newmicrobe.remove((1,-1))
                            if(x+1>len(self.grid)):
                                newmicrobe.remove((1,0))
                            if(y+1>len(self.grid[0])):
                                newmicrobe.remove((0,1))
                                newmicrobe.remove((-1,1))
                                newmicrobe.remove((1,1))
                            for i in movements:
                                if(self.grid[i[0]][i[1]].hasMicrobe()): #grid misspelled
                                    movements.remove(i)
                                if(i in newmicrobe and i in movements):
                                    movements.remove(i)
                                    o = randint(0,len(self.grid))#don't need random in front of randint
                                    p = randint(0,len(selg.grid[x]))#don't need random in front of randint
                                    self.grid[o][p].append(newmicrobe[i])
                            if(len(movements)>0):
                                microbe.consumeNutrient()
                                lenl = randint(0,len(movements)-1)#don't need random in front of randint
                                newmicrobe.append(movements[lenl][0],movements[lenl][1])
        for z in newmicrobe:
            (self.grid[z[0]][z[1]].createMicrobe()) #self.grid part should go first, followed by .createMicrobe()

        #Add your code here
    def step(self, iterations):
        for iteration in range(iterations):
            self.moveNutrients()
            self.checkMicrobes()

    def __str__(self):
        result = ""
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                result += str(self.grid[y][x].getN) + " "
            result += "\n"
        return result
def main():
    Petri = PetriDish(5,5,.96, (2,2))#Needs to be a list of tuples for 4th argument such as [(2,2), (4, 1)]
    Petri.step()
    print(Petri)
    #Add your code here
if __name__ == '__main__':
    main()