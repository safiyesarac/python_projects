
import math
states1=[]
states2=[]


class TwoBodyController():

    def rungeKutta(h, u, derivative) :
    
        def calculate(h, u, derivative) : 
            a = [h/2, h/2, h, 0]
            b = [h/6, h/3, h/3, h/6]
            u0 = []
            ut = []
            dimension = len(u)

            for i in range(dimension) :
                u0.append(u[i])
                ut.append(0)
      

            for j in range(4) :
                du = derivative

                for i in range(dimension) :
                    u[i] = u0[i] + a[j]*du[i]
                    ut[i] = ut[i] + b[j]*du[i]
        
      

            for i in range(dimension) : 
                u[i] = u0[i] + ut[i]
      
    

        return calculate(h, u, derivative);
    
    
    def initialVelocity(q, eccentricity) :
        return math.sqrt( (1 + q) * (1 + eccentricity) );
    
    
    def euler(h,u):
        du = TwoBodyController.derivative()
        for i in range(4):
            u[i] = u[i] + du[i]*h
    
    def derivative() :
        du =  [None] * len(TwoBodyModel.state["u"])
        r = TwoBodyModel.state["u"][0:2]
        rr = math.sqrt( math.pow(r[0],2) + math.pow(r[1],2) )
        
        for i in range(2):
            du[i] = TwoBodyModel.state["u"][i + 2];
      
            du[i + 2] = -(1 + TwoBodyModel.state["masses"]["q"]) * r[i] / (math.pow(rr,3))
          
    
        return du;
    timestep=0.15
    def  updatePosition() :
        
        TwoBodyController.rungeKutta(TwoBodyController.timestep, TwoBodyModel.state["u"], TwoBodyController.derivative())
        TwoBodyController.calculateNewPosition()
     #print(state)
        
    def calculateNewPosition() :
        r = 1
        a1 = (TwoBodyModel.state["masses"]["m2"] / TwoBodyModel.state["masses"]["m12"]) * r
        a2 = (TwoBodyModel.state["masses"]["m1"] / TwoBodyModel.state["masses"]["m12"]) * r
    
        TwoBodyModel.state["positions"][0]["x"] = -a2 * TwoBodyModel.state["u"][0]
        TwoBodyModel.state["positions"][0]["y"] = -a2 * TwoBodyModel.state["u"][1]
    
        TwoBodyModel.state["positions"][1]["x"]  = a1 * TwoBodyModel.state["u"][0]
        TwoBodyModel.state["positions"][1]["y"] = a1 * TwoBodyModel.state["u"][1]
    
    
    def  separationBetweenObjects() :
        return initialConditions.position.x / (1 - state.eccentricity)
 

class TwoBodyModel():
    calculater=TwoBodyController()
    state = { "u": [0, 0, 0, 0],
      "masses": {
        "q": 0, 
        "m1": 1,
        "m2": 0,
        "m12": 0 
      },
      "eccentricity": 0, 
 
      "positions": [
        {
          "x": 0,
          "y": 0
        },
        {
         "x": 0,
          "y": 0
        }
      ],
      
    };

    initialConditions = {
      "eccentricity": 0.07, 
      "q": 0.5, 
      "position": {
       "x": 1,
        "y": 0
      },
      "velocity": {
        "u": 0
      }
    };
    def   updateParametersDependentOnUserInput() :
        TwoBodyModel.state["masses"]["m2"] = TwoBodyModel.state["masses"]["q"]
        TwoBodyModel.state["masses"]["m12"] = TwoBodyModel.state["masses"]["m1"] + TwoBodyModel.state["masses"]["m2"]
        TwoBodyModel.state["u"][3] = TwoBodyController.initialVelocity(TwoBodyModel.state["masses"]["q"], TwoBodyModel.state["eccentricity"])
    

    def resetStateToInitialConditions( ) :
        TwoBodyModel.state["masses"]["q"] = TwoBodyModel.initialConditions["q"]
        TwoBodyModel.state["eccentricity"] = TwoBodyModel.initialConditions["eccentricity"]
        TwoBodyModel.state["u"][0] = TwoBodyModel.initialConditions["position"]["x"]
        TwoBodyModel.state["u"][1] = TwoBodyModel.initialConditions["position"]["y"]
        TwoBodyModel.state["u"][2] = TwoBodyModel.initialConditions["velocity"]["u"]
    
        TwoBodyModel.updateParametersDependentOnUserInput()
    def  updateMassRatioFromUserInput(massRatio) :
        TwoBodyModel.state["masses"]["q"]= massRatio
        TwoBodyModel.updateParametersDependentOnUserInput()
        
    
    def  updateEccentricityFromUserInput(eccentricity) :
        TwoBodyModel.state["eccentricity"] = eccentricity
        TwoBodyModel.updateParametersDependentOnUserInput()
    
    
    def storeValues(numberOfIter):
        TwoBodyModel.resetStateToInitialConditions()
        f = open("test.txt", "a")
        #f.writelines(str(state["positions"][0]["x"])+","+str(state["positions"][0]["y"])+","+str(state["positions"][1]["x"])+","+str(state["positions"][1]["x"])+"\n")
        for i in range(numberOfIter):
            TwoBodyController.updatePosition()
            f.writelines(str(TwoBodyModel.state["positions"][0]["x"])+","+str(TwoBodyModel.state["positions"][0]["y"])+","+str(TwoBodyModel.state["positions"][1]["x"])+","+str(TwoBodyModel.state["positions"][1]["x"])+"\n")
        f.close()



 













"""
ask inputs for initial conds

"""
print(  "Welcome to the two body simulation")
number=input("enter number of iterations")
stepsize=float(input("enter stepsize"))
TwoBodyController.timestep=stepsize
massRatio=float(input("enter mass Ratio"))
TwoBodyModel.updateMassRatioFromUserInput(massRatio)
eccen=input("enter eccentricity")
TwoBodyModel.updateEccentricityFromUserInput(float(eccen))

TwoBodyModel.storeValues(int(number))