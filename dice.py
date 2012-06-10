from sympy import *
from sympy.stats import *
X = Die('X', 6)
Y = Die('Y', 6)
print "P(X>3)   = ", P(X>3)
print "E(X+Y)   = ", E(X+Y)
print "E(2*X)   = ", E(2*X)
print "variance(X+3) = ", variance(X+3)

density_map = {'heads': .5, 'tails':.5}
coin = FiniteRV('coin', density_map)
print "Density(coin) = ", density(coin)


