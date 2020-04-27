# Practice with Google OR tools - solving a simple linear optimization
from ortools.linear_solver import pywraplp

def main():
	solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

	# Defining my decision variables (also introduces constraints on them)
	x = solver.NumVar(0, 1, 'x')
	y = solver.NumVar(0, 1, 'y')
	print(f'The number of variables I have rn are: {solver.NumVariables()}')

	# Defining another constraint: x + y ≤ 2
	ct = solver.Constraint(-solver.infinity(), 2, 'ct')
	ct.SetCoefficient(x, 1)
	ct.SetCoefficient(y, 1)
	print(f'The number of constraints rn is {solver.NumConstraints()}')

	# Creating some objective function
	obj = solver.Objective()
	obj.SetCoefficient(x, 3)
	obj.SetCoefficient(y, 1)
	obj.SetMaximization()

	solver.Solve()

	print(obj.Value())
	print(x.solution_value())
	print(y.solution_value())
if __name__ == '__main__':
	main()

