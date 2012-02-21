from sympy import *
from sympy.stats import *
X = Die(6)
Y = Die(6)
print "P(X>3)   = ", P(X>3)
print "E(X+Y)   = ", E(X+Y)
print "E(2*X)   = ", E(2*X)
print "Var(X+3) = ", Var(X+3)

density_map = {'heads': .5, 'tails':.5}
coin = FiniteRV(density_map)
print "Density(coin) = ", Density(coin)


