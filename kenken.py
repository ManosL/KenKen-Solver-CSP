from enum import Enum
import csp
import time

############################# GAME PUZZLES ################################################
def Create_Easy_Set():
    square_side_length = 4
    cliques = []

    cliques.append(Clique(((0,0),(0,1),(0,2),(0,3)),24,Calculation.MULTIPLICATION))
    cliques.append(Clique(((1,0),(1,1),(2,0),(2,1)),12,Calculation.ADDITION))
    cliques.append(Clique(((1,2),(1,3)),3,Calculation.DIVISION))
    cliques.append(Clique(((2,2),(2,3),(3,3)),8,Calculation.ADDITION))
    cliques.append(Clique(((3,0),(3,1),(3,2)),6,Calculation.MULTIPLICATION))

    return (square_side_length,cliques)

def Create_Medium_Set():   #The one on exercise
    square_side_length = 6
    cliques = []

    cliques.append(Clique(((0,0),(1,0)),11,Calculation.ADDITION))
    cliques.append(Clique(((0,1),(0,2)),2,Calculation.DIVISION))
    cliques.append(Clique(((0,3),(1,3)),20,Calculation.MULTIPLICATION))
    cliques.append(Clique(((0,4),(0,5),(1,5),(2,5)),6,Calculation.MULTIPLICATION))
    cliques.append(Clique(((1,1),(1,2)),3,Calculation.SUBTRACTION))
    cliques.append(Clique(((1,4),(2,4)),3,Calculation.DIVISION))
    cliques.append(Clique(((2,0),(2,1),(3,0),(3,1)),240,Calculation.MULTIPLICATION))
    cliques.append(Clique(((2,2),(2,3)),6,Calculation.MULTIPLICATION))
    cliques.append(Clique(((3,2),(4,2)),6,Calculation.MULTIPLICATION))
    cliques.append(Clique(((3,3),(4,3),(4,4)),7,Calculation.ADDITION))
    cliques.append(Clique(((3,4),(3,5)),30,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,0),(4,1)),6,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,5),(5,5)),9,Calculation.ADDITION))
    cliques.append(Clique(((5,0),(5,1),(5,2)),8,Calculation.ADDITION))
    cliques.append(Clique(((5,3),(5,4)),2,Calculation.DIVISION))

    return (square_side_length,cliques)

def Create_Easy_Set_9x9():
    square_side_length = 9
    cliques = []

    cliques.append(Clique(((0,0),(1,0),(1,1),(2,1)),21,Calculation.ADDITION))
    cliques.append(Clique(((0,1),(0,2)),17,Calculation.ADDITION))
    cliques.append(Clique(((0,3),(0,4)),42,Calculation.MULTIPLICATION))
    cliques.append(Clique(((0,5),(0,6),(0,7)),10,Calculation.MULTIPLICATION))
    cliques.append(Clique(((0,8),(1,8)),21,Calculation.MULTIPLICATION))
    cliques.append(Clique(((1,2),(1,3)),4,Calculation.DIVISION))
    cliques.append(Clique(((1,4),(2,4),(3,4)),72,Calculation.MULTIPLICATION))
    cliques.append(Clique(((1,5),(1,6)),3,Calculation.DIVISION))
    cliques.append(Clique(((1,7),(2,7)),15,Calculation.MULTIPLICATION))
    cliques.append(Clique(((2,0),),5,Calculation.MULTIPLICATION))
    cliques.append(Clique(((2,2),(2,3)),24,Calculation.MULTIPLICATION))
    cliques.append(Clique(((2,5),(3,5)),17,Calculation.ADDITION))
    cliques.append(Clique(((2,6),(3,6)),15,Calculation.ADDITION))
    cliques.append(Clique(((2,8),(3,8),(3,7)),6,Calculation.MULTIPLICATION))
    cliques.append(Clique(((3,0),(4,0)),8,Calculation.SUBTRACTION))
    cliques.append(Clique(((3,1),(4,1),(4,2)),7,Calculation.ADDITION))
    cliques.append(Clique(((3,2),(3,3)),15,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,3),(5,3),(5,2),(5,1)),392,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,4),(4,5)),20,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,6),(5,6)),54,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,7),(4,8)),2,Calculation.SUBTRACTION))
    cliques.append(Clique(((5,0),(6,0)),5,Calculation.SUBTRACTION))
    cliques.append(Clique(((5,4),(5,5)),2,Calculation.SUBTRACTION))
    cliques.append(Clique(((5,7),(5,8),(6,8)),17,Calculation.ADDITION))
    cliques.append(Clique(((6,1),(6,2)),11,Calculation.ADDITION))
    cliques.append(Clique(((6,3),(7,3)),8,Calculation.SUBTRACTION))
    cliques.append(Clique(((6,4),(6,5)),4,Calculation.DIVISION))
    cliques.append(Clique(((6,6),(6,7),(7,7)),20,Calculation.ADDITION))
    cliques.append(Clique(((7,0),(8,0),(7,1)),16,Calculation.ADDITION))
    cliques.append(Clique(((7,2),(8,2),(8,1),(8,3)),17,Calculation.ADDITION))
    cliques.append(Clique(((7,4),(8,4),(8,5)),36,Calculation.MULTIPLICATION))
    cliques.append(Clique(((7,5),(7,6),(8,6)),13,Calculation.ADDITION))
    cliques.append(Clique(((7,8),(8,8)),10,Calculation.MULTIPLICATION))
    cliques.append(Clique(((8,7),),7,Calculation.DIVISION))                     

    return (square_side_length,cliques)

def Create_Medium_Set_9x9():
    square_side_length = 9
    cliques = []
                   
    cliques.append(Clique(((0,0),(0,1)),2,Calculation.DIVISION))
    cliques.append(Clique(((0,2),(1,2),(1,3),(2,3)),27,Calculation.ADDITION))
    cliques.append(Clique(((0,3),(0,4),(1,4)),24,Calculation.MULTIPLICATION))
    cliques.append(Clique(((0,5),(0,6)),8,Calculation.ADDITION))
    cliques.append(Clique(((0,7),(0,8)),40,Calculation.MULTIPLICATION))
    cliques.append(Clique(((1,0),(2,0)),36,Calculation.MULTIPLICATION))
    cliques.append(Clique(((1,1),(2,1)),3,Calculation.ADDITION))
    cliques.append(Clique(((1,5),(2,5)),3,Calculation.SUBTRACTION))
    cliques.append(Clique(((1,6),(1,7),(1,8)),14,Calculation.ADDITION))
    cliques.append(Clique(((2,2),(3,2),(3,1)),28,Calculation.MULTIPLICATION))
    cliques.append(Clique(((2,4),(3,4)),2,Calculation.SUBTRACTION))
    cliques.append(Clique(((2,6),(2,7)),3,Calculation.SUBTRACTION))
    cliques.append(Clique(((2,8),(3,8),(3,7)),12,Calculation.ADDITION))
    cliques.append(Clique(((3,0),(4,0)),3,Calculation.ADDITION))
    cliques.append(Clique(((3,3),(4,3),(5,3)),20,Calculation.ADDITION))
    cliques.append(Clique(((3,5),(3,6)),3,Calculation.SUBTRACTION))
    cliques.append(Clique(((4,1),(5,1),(6,1)),288,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,2),(5,2),(6,2)),30,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,4),(4,5)),2,Calculation.DIVISION))
    cliques.append(Clique(((4,6),(5,6)),4,Calculation.DIVISION))
    cliques.append(Clique(((4,7),(4,8)),2,Calculation.DIVISION))
    cliques.append(Clique(((5,0),(6,0),(7,0)),336,Calculation.MULTIPLICATION))
    cliques.append(Clique(((5,4),(5,5)),6,Calculation.SUBTRACTION))
    cliques.append(Clique(((5,7),(5,8)),4,Calculation.SUBTRACTION))
    cliques.append(Clique(((6,3),(6,4)),1,Calculation.SUBTRACTION))
    cliques.append(Clique(((6,5),(6,6),(7,5)),81,Calculation.MULTIPLICATION))
    cliques.append(Clique(((6,7),(7,7)),8,Calculation.SUBTRACTION))
    cliques.append(Clique(((6,8),(7,8)),3,Calculation.DIVISION))
    cliques.append(Clique(((7,1),(7,2)),2,Calculation.SUBTRACTION))
    cliques.append(Clique(((7,3),(8,3)),5,Calculation.SUBTRACTION))
    cliques.append(Clique(((7,4),(8,4)),8,Calculation.SUBTRACTION))
    cliques.append(Clique(((7,6),(8,6),(8,5)),48,Calculation.MULTIPLICATION))
    cliques.append(Clique(((8,0),(8,1),(8,2)),16,Calculation.ADDITION))
    cliques.append(Clique(((8,7),(8,8)),11,Calculation.ADDITION))

    return (square_side_length,cliques)

def Create_Expert_Set_9x9():  #Works fast only with FC and FC+MRV
    square_side_length = 9
    cliques = []

    cliques.append(Clique(((0,0),(1,0),(2,0),(2,1)),432,Calculation.MULTIPLICATION))
    cliques.append(Clique(((0,1),(0,2)),4,Calculation.DIVISION))
    cliques.append(Clique(((0,3),),2,Calculation.MULTIPLICATION))
    cliques.append(Clique(((0,4),(0,5)),11,Calculation.ADDITION))
    cliques.append(Clique(((0,6),(1,6),(1,5)),19,Calculation.ADDITION))
    cliques.append(Clique(((0,7),(1,7)),2,Calculation.SUBTRACTION))
    cliques.append(Clique(((0,8),(1,8)),1,Calculation.SUBTRACTION))
    cliques.append(Clique(((1,1),(1,2)),1,Calculation.SUBTRACTION))
    cliques.append(Clique(((1,3),(1,4)),3,Calculation.DIVISION))
    cliques.append(Clique(((2,2),(2,3)),7,Calculation.SUBTRACTION))
    cliques.append(Clique(((2,4),(2,5)),3,Calculation.SUBTRACTION))
    cliques.append(Clique(((2,6),(2,7),(2,8)),210,Calculation.MULTIPLICATION))
    cliques.append(Clique(((3,0),(3,1),(4,1)),12,Calculation.MULTIPLICATION))
    cliques.append(Clique(((3,2),(3,3)),12,Calculation.MULTIPLICATION))
    cliques.append(Clique(((3,4),(3,5)),3,Calculation.SUBTRACTION))
    cliques.append(Clique(((3,6),(3,7),(3,8)),504,Calculation.MULTIPLICATION))
    cliques.append(Clique(((4,0),(5,0)),1,Calculation.SUBTRACTION))
    cliques.append(Clique(((4,2),(5,2),(5,1)),21,Calculation.ADDITION))
    cliques.append(Clique(((4,3),(5,3)),6,Calculation.ADDITION))
    cliques.append(Clique(((4,4),(4,5)),2,Calculation.SUBTRACTION))
    cliques.append(Clique(((4,6),(4,7)),1,Calculation.SUBTRACTION))
    cliques.append(Clique(((4,8),(5,8)),8,Calculation.SUBTRACTION))
    cliques.append(Clique(((5,4),(6,4)),13,Calculation.ADDITION))
    cliques.append(Clique(((5,5),(6,5)),2,Calculation.SUBTRACTION))
    cliques.append(Clique(((5,6),(5,7)),11,Calculation.ADDITION))
    cliques.append(Clique(((6,0),(7,0)),1,Calculation.SUBTRACTION))
    cliques.append(Clique(((6,1),(6,2),(7,1)),17,Calculation.ADDITION))
    cliques.append(Clique(((6,3),(7,3),(7,2),(7,4)),24,Calculation.ADDITION))
    cliques.append(Clique(((6,6),(6,7)),2,Calculation.DIVISION))
    cliques.append(Clique(((6,8),(7,8)),6,Calculation.SUBTRACTION))
    cliques.append(Clique(((7,5),(8,5),(8,6)),19,Calculation.ADDITION))
    cliques.append(Clique(((7,6),(7,7),(8,7)),9,Calculation.ADDITION))
    cliques.append(Clique(((8,0),(8,1),(8,2)),40,Calculation.MULTIPLICATION))
    cliques.append(Clique(((8,3),(8,4)),2,Calculation.SUBTRACTION))
    cliques.append(Clique(((8,8),),3,Calculation.SUBTRACTION))

    return (square_side_length,cliques)
##################################################################################
    
class Calculation(Enum):
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4

class Clique:   #Contains the necessary information of the clique
                #the boxes coordination, the result and the calculation

    def __init__(self,boxes_,result_,calculation_):
        self.boxes = boxes_
        self.result = result_
        self.calculation = calculation_
    
    def getBoxesCoordinations(self):
        return self.boxes
    
    def getResult(self):
        return self.result
    
    def getCalculation(self):
        return self.calculation

    def isInClique(self,coordinates):
        return (coordinates in self.boxes)

def get_n_aries(lists,curr):       #Function that returns n-aries from n lists
                                   #by selecting one element of each list
    result = []

    if lists == []:
        return [tuple(curr)]

    first_list = list(lists[0])
    del lists[0]

    for elem in first_list:
        curr1 = list(curr)
        curr1.append(elem)

        result = result + get_n_aries(list(lists),curr1)
    
    return result


class KenKen(csp.CSP):

    #Creating the problem

    def __init__(self,square_size,cliques):
        self.constraint_fn_called = 0
        self.square_size = square_size
        self.cliques = cliques

        vars = []
        domains = {}
        neighbors = {}

        #Getting the variables and the domains(what are these I will explain it on the report)
        for clique in cliques:
            clique_coords = clique.getBoxesCoordinations()
            clique_coords_len = len(clique_coords)
            clique_calc = clique.getCalculation()
            clique_result = clique.getResult()

            final_var = clique_coords
            vars.append(final_var)

            domains[final_var] = []

            n_aries_list = get_n_aries(clique_coords_len*[list(range(1,square_size + 1))],[])

            for n_ary in n_aries_list:
                if self.CanFilledLikeThat(clique_coords,n_ary)\
                and self.have_result(n_ary,clique_calc,clique_result):
                    domains[final_var].append(n_ary)

        #Getting the neighbors of each variable
        for var in vars:
            neighbors[var] = []
            temp = list(vars)
            temp.remove(var)

            for temp_var in temp:
                if self.is_neighbor(var,temp_var):
                    neighbors[var].append(temp_var)
        
        #Creating our CSP
        csp.CSP.__init__(self,vars,domains,neighbors,self.constraints_function)


    #Function that checks if 2 cliques are neighbors
    #by checking if some box of each one are in the
    #same row or column

    def is_neighbor(self,var1,var2):   
        for elem1 in var1:
            (x1,y1) = elem1
            for elem2 in var2:
                (x2,y2) = elem2

                if x1 == x2 or y1 == y2:
                    return True
    
        return False

    #Checks if I apply to the tuple nums
    #the calculation Calc the result will be
    #equal to WantedResult
 
    def have_result(self,Nums,Calc,WantedResult):
        curr_result = Nums[0]

        for index1 in list(range(1,len(Nums))):
            if Calc == Calculation.ADDITION:
                curr_result = curr_result + Nums[index1]
        
            if Calc == Calculation.MULTIPLICATION:
                curr_result = curr_result * Nums[index1]
        
            if Calc == Calculation.SUBTRACTION:
                curr_result = abs(curr_result - Nums[index1])

            if Calc == Calculation.DIVISION:
                if Nums[index1] >= curr_result:
                    if Nums[index1] % curr_result != 0:
                        return False

                    curr_result = Nums[index1] / curr_result
                else:
                    if curr_result % Nums[index1] != 0:
                        return False

                    curr_result = curr_result / Nums[index1]

        if curr_result != WantedResult:
            return False
    
        return True


    def CanFilledLikeThat(self,Coords,Nums):
        for index1 in list(range(0,len(Coords))):
            (x1,y1) = Coords[index1]
            for index2 in list(range(index1 + 1,len(Coords))):
                (x2,y2) = Coords[index2]

                if (x1 == x2 or y1 == y2) and Nums[index1] == Nums[index2]:
                    return False
    
        return True

    #The constraint function just checks that the 
    #boxes of 2 different cliques that are on the 
    #same row or column of the grid have different
    #value if I assign a to A and b to B.

    def constraints_function(self,A,a,B,b):
        self.constraint_fn_called += 1

        for index1 in list(range(0,len(A))):
            (x1,y1) = A[index1]
            for index2 in list(range(0,len(B))):
                (x2,y2) = B[index2]

                if x1 == x2 or y1 == y2:
                    if a[index1] == b[index2]:
                        return False
    
        return True 


    #Calls BT and displays the result
    def kenken_backtrack(self):
        self.__display(csp.backtracking_search(self))
    
    #Calls BT+MRV and displays the result
    def kenken_backtrack_mrv(self):
        self.__display(csp.backtracking_search(self,csp.mrv))
    
    #Calls FC and displays the result
    def kenken_forward__checking(self):
        self.__display(csp.backtracking_search(self,
                        select_unassigned_variable=csp.first_unassigned_variable,
                        order_domain_values=csp.unordered_domain_values,
                        inference = csp.forward_checking)
                        )
    
    #Calls FC+MRV and displays the result
    def kenken_forward__checking_mrv(self):
        self.__display(csp.backtracking_search(self,
                        select_unassigned_variable=csp.mrv,
                        order_domain_values=csp.unordered_domain_values,
                        inference = csp.forward_checking))

    #Calls MAC and displays the result
    def kenken_mac(self):
        self.__display(csp.backtracking_search(self,
                        select_unassigned_variable=csp.first_unassigned_variable,
                        order_domain_values=csp.unordered_domain_values,
                        inference = csp.mac))
    
    #Calls minConflicts and displays the result
    def kenken_minConflicts(self):
        self.__display(csp.min_conflicts(self))

    def __display(self,solution):      #I declare it private
        boxes = {}

        if solution == None:
            print("There is no solution")
            return

        print("Solution is:")
        for key in solution.keys():
            values = solution[key]
            coords = key

            for index in list(range(0,len(coords))):
                boxes[coords[index]] = values[index]
        
        for i in range(0,self.square_size):
            for j in range(0,self.square_size):
                print(boxes[(i,j)], end = "  ")
            
            print(end = '\n\n')
        
        print("With cliques and result of each one:")

        for clique in self.cliques:
            print("Clique = ",clique.getBoxesCoordinations()," ,Result = ",clique.getResult(),end = " ")

            clique_calc = clique.getCalculation()
            if clique_calc == Calculation.ADDITION:
                print("by addition")
            
            if clique_calc == Calculation.DIVISION:
                print("by division")
            
            if clique_calc == Calculation.MULTIPLICATION:
                print("by multiplication")
            
            if clique_calc == Calculation.SUBTRACTION:
                print("by subtraction")

def main():
    print("Please Enter the number of the puzzle you want:\n\
    1. Easy 4x4 \n\
    2. Medium 6x6\n\
    3. Easy 9x9\n\
    4. Medium 9x9\n\
    5. Expert 9x9\n")
    
    puzzle_select = int(input())
    square_side_length = -1
    cliques = []

    if puzzle_select == 1:
        (square_side_length,cliques) = Create_Easy_Set()
    elif puzzle_select == 2:
        (square_side_length,cliques) = Create_Medium_Set()
    elif puzzle_select == 3:
        (square_side_length,cliques) = Create_Easy_Set_9x9()
    elif puzzle_select == 4:
        (square_side_length,cliques) = Create_Medium_Set_9x9()
    elif puzzle_select == 5:
        (square_side_length,cliques) = Create_Expert_Set_9x9()
    else:
        print("Give a valid num")
        return

    KenKen_Prob = KenKen(square_side_length,cliques)

    print("Please Enter the number of the algorithm you want to solve the puzzle:\n\
    1. Backtracking \n\
    2. Backtracking + MRV\n\
    3. Forward Checking\n\
    4. Forward Checking + MRV\n\
    5. MAC\n\
    6. Minimum Conflicts\n")

    solution_algorithm = int(input())

    if solution_algorithm == 1:
        start_time = time.time()
        
        KenKen_Prob.kenken_backtrack()
        
        print("\n\nSolved in %f seconds" % (time.time() - start_time))
        print("Happened %d assignments." % (KenKen_Prob.nassigns))
        print("Constraint function called %d times." % (KenKen_Prob.constraint_fn_called))
        return

    if solution_algorithm == 2:
        start_time = time.time()
        
        KenKen_Prob.kenken_backtrack_mrv()

        print("\n\nSolved in %f seconds" % (time.time() - start_time))
        print("Happened %d assignments." % (KenKen_Prob.nassigns))
        print("Constraint function called %d times." % (KenKen_Prob.constraint_fn_called))
        return

    if solution_algorithm == 3:
        start_time = time.time()
        
        KenKen_Prob.kenken_forward__checking()
        
        print("\n\nSolved in %f seconds" % (time.time() - start_time))
        print("Happened %d assignments." % (KenKen_Prob.nassigns))
        print("Constraint function called %d times." % (KenKen_Prob.constraint_fn_called))
        return

    if solution_algorithm == 4:
        start_time = time.time()
        
        KenKen_Prob.kenken_forward__checking_mrv()
        
        print("\n\nSolved in %f seconds" % (time.time() - start_time))
        print("Happened %d assignments." % (KenKen_Prob.nassigns))
        print("Constraint function called %d times." % (KenKen_Prob.constraint_fn_called))
        return

    if solution_algorithm == 5:
        start_time = time.time()
        
        KenKen_Prob.kenken_forward__checking_mrv()
        
        print("\n\nSolved in %f seconds" % (time.time() - start_time))
        print("Happened %d assignments." % (KenKen_Prob.nassigns))
        print("Constraint function called %d times." % (KenKen_Prob.constraint_fn_called))
        return

    if solution_algorithm == 6:
        start_time = time.time()
        
        KenKen_Prob.kenken_minConflicts()
        
        print("\n\nSolved in %f seconds" % (time.time() - start_time))
        print("Happened %d assignments." % (KenKen_Prob.nassigns))
        print("Constraint function called %d times." % (KenKen_Prob.constraint_fn_called))
        return

    else:
        print("Give a valid num")
        return   

if __name__ == "__main__":
    main()