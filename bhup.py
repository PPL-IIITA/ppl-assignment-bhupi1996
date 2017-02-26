from operator import attrgetter
import csv
import logging

class Girl:
    def __init__(self,name,attractiveness,intelligence,maintainanceCost,datingCriteria):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.maintainanceCost = maintainanceCost
        self.datingCriteria = datingCriteria
        self.committed = False
        self.bfName = ""

class Boy:
    def __init__(self,name,attractiveness,intelligence,budget,minAttraction):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.minAttraction = minAttraction
        self.committed = False
        self.gfName = ""
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

def logs(log):
    logging.basicConfig(filename='logs.log',filemode='w',datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',level=logging.DEBUG)
    logging.info(log)

	
def solve():
    girls = []
    boys = []
    inp = []
    n=3

    #first line of input is no of boys or girls
    #next n lines contains information about girls
    #next n lines contains information about boys
    with open('bhupInput.csv','rb') as f:
        data = csv.reader(f)
        for row in data:
            inp.append(row[0])
    #print inp
            
    #dating criteria
    #1 most Attractive
    #2 most intelli
    #3 most rich

    n = int(inp[0])
    for i in range(n):
        name,a,inte,m,dc = inp[1+i].split()
        girls.append(Girl(name,int(a),int(inte),int(m),int(dc)))
    for i in range(n):
        name,a,inte,m,ma = inp[i+n+1].split()
        boys.append(Boy(name,int(a),int(inte),int(m),int(ma)))
        
    for i in range(n):
        eligBoys = [boy for boy in boys if boy.committed==False and boy.budget > girls[i].maintainanceCost and girls[i].attractiveness > boy.minAttraction]
        if eligBoys:
            if girls[i].datingCriteria == 1:
                boy = max(eligBoys,key=attrgetter('attractiveness'))
                boy.committed = girls[i].committed = True
                boy.gfName = girls[i].name
                girls[i].bfName = boy.name
            elif girls[i].datingCriteria == 2:
                boy = max(eligBoys,key=attrgetter('intelligence'))
                boy.committed = girls[i].committed = True
                boy.gfName = girls[i].name
                girls[i].bfName = boy.name
            elif girls[i].datingCriteria == 3:
                boy = max(eligBoys,key=attrgetter('budget'))
                boy.committed = girls[i].committed = True
                boy.gfName = girls[i].name
                girls[i].bfName = boy.name

    for i in range(3):
        if girls[i].committed == True:
            print girls[i].name ,"is commited with ",girls[i].bfName
            logs(girls[i].name+" is commited with "+girls[i].bfName)



solve()
