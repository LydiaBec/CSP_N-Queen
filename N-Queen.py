import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

def print_solution(N_Queens):
    if N_Queens.stop == 1:
        for val in range(1,n + 1):
            print('|', sep='', end='')
            for va in range(1,n + 1):
                if val == N_Queens.value[va]:
                    print('Q', end='')
                else :
                    print('.', end='')
                print('|', sep='', end='')
            print()

n = 6
N_Queens = CS.CSP(n, problem_name='N-Queens', solution_path='./Solutions/')
N_Queens.commonDomain([i for i in range(1,n + 1)])

for i in range(1,N_Queens.variables+1):
    for j in range(i+1,N_Queens.variables+1):
        N_Queens.addConstraint('value['+str(i)+'] != value['+str(j)+']')
        N_Queens.addConstraint('abs(value['+str(j)+'] - value['+str(i)+']) != '+str(j)+'-'+str(i))
print (f'Solution for {n} queens')
N_Queens.solve_dfs(timeout = 120)
print_solution(N_Queens)
N_Queens.solve_BackTrack(timeout = 120)
print_solution(N_Queens)
N_Queens.solve_ForwardChecking(timeout = 120)
print_solution(N_Queens)
N_Queens.solve_ArcConsistent_BackTracking(timeout = 120)
print_solution(N_Queens)
