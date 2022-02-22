import random, time
from datetime import datetime
from .Trivial_Algorithms.BackTrack import BackTrack
from .Trivial_Algorithms.dfs import dfs
from .Forward_Checking.ForwardChecking import ForwardChecking

from .ArcConsistency.Arc_Consistent_Backtracking import ArcConsistent_MRV_LCV


class CSP:
    def __init__(self, variables, solution_path = None, problem_name = 'CSP'):
        random.seed(datetime.now())
        self.variables = variables
        self.domains = [set() for i in range(variables + 1)]
        self.graph = [set() for i in range(variables + 1)]
        self.value = [None for i in range(variables + 1)]
        self.givenValue = [False for i in range(variables + 1)]
        self.domainHelp = [[] for i in range(variables + 1)]
        self.graphConstraints = [dict() for i in range(variables + 1)]
        self.multivariateGraph = [[] for i in range(variables + 1)]
        self.AllConstraints = []
        self.stop = 0
        self.problem_name = problem_name
        self.multivariate = False
        self.currentHelp = 1
        self.variableConversion = dict()
        for i in range(1,variables + 1):
            self.variableConversion[i] = i
        if solution_path: self.solution_path = solution_path
    
    def commonDomain(self, domain = []):
        """
        To set same domain for all variables
        """
        for value in domain:
            for i in range(1,self.variables+1):
                self.domains[i].add(value)
                self.domainHelp[i].append(value)

    def addConstraint(self, constraint):
        """
        Enforce constraints
        pass comparison as string
        """
        numbers, prev, cur = [], False, ""
        for i in constraint:
            if i == ' ':
                continue
            if i == '[':
                prev = True
                continue
            if i == ']':
                prev = False
                if not cur.isnumeric() and cur not in self.variableConversion:
                    print(cur, self.currentHelp)
                    self.variableConversion[cur] = self.currentHelp
                    self.variableConversion[self.currentHelp] = cur
                    self.currentHelp += 1
                elif cur.isnumeric(): 
                    self.variableConversion[cur] = int(cur)
                    self.variableConversion[int(cur)] = int(cur)
                numbers.append(self.variableConversion[cur])
                cur = ""
                continue
            if prev:
                cur += i
        for key in self.variableConversion:
            if str(key).isnumeric(): continue
            constraint = constraint.replace(str(key), str(self.variableConversion[key]))
        constraint = compile(constraint, "<string>", "eval")
        if len(numbers) > 2:
            self.multivariate = True
        for i in range (len(numbers)):
            n1 = numbers[i]
            for j in range(i + 1, len(numbers)):
                n2 = numbers[j];
                self.multivariateGraph[n1].append((constraint, numbers))
                self.multivariateGraph[n2].append((constraint, numbers))
                if n2 in self.graphConstraints[n1]:
                    self.graphConstraints[n1][n2].add(constraint)
                else:
                    self.graphConstraints[n1][n2] = {constraint}
                if n1 in self.graphConstraints[n2]:
                    self.graphConstraints[n2][n1].add(constraint)
                else:
                    self.graphConstraints[n2][n1] = {constraint}
                self.graph[n1].add(n2)
                self.graph[n2].add(n1)
        self.AllConstraints.append(constraint)

    def solve_dfs(self, timeout = 10):
        self.reset()
        start = time.time()
        dfs(self, timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'dfs_Solution.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("dfs timed out")
                wr += "dfs timed out"
            elif self.stop == 0:
                print("DFS: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by dfs: ", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_BackTrack(self, timeout = 10):
        self.reset()
        start = time.time()
        BackTrack(self, timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'BackTrack_Solution.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("BackTrack timed out")
                wr += "BackTrack timed out"
            elif self.stop == 0:
                print("BackTrack: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by BackTrack: ", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_ForwardChecking(self, timeout = 10):
        self.reset()
        start = time.time()
        ForwardChecking(self, timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'ForwardChecking_Solution.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("ForwardChecking timed out")
                wr += "ForwardChecking timed out"
            elif self.stop == 0:
                print("Forward Checking: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by ForwardChecking: ", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()


    def solve_ArcConsistent_BackTracking(self, timeout = 10):
        self.reset()
        start = time.time()
        ArcConsistent_MRV_LCV(obj = self, timeout = timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'ArcConsistent_BackTracking.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("Arc Consistent BackTracking timed out")
                wr += "Arc Consistent BackTracking timed out"
            elif self.stop == 0:
                print("No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by Arc Consistent BackTracking:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    
  
    def reset(self):
        self.stop = 0
        self.value = [None for i in range(self.variables + 1)]
        self.givenValue = [False for i in range(self.variables + 1)]
        self.domains = [set(self.domainHelp[i]) for i in range(self.variables + 1)]