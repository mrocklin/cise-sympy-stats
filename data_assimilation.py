from sympy import *
from sympy.stats import *

T = Normal('T', 30, 3)
print "P(T>33) = ", P(T>33, evaluate=False)
print "        = ", P(T>33)
print "        = ", P(T>33).evalf()

noise = Normal('eta', 0, 1.5)
observation = T + noise

T_posterior = given(T, Eq(observation, 26))

x = Symbol('x')
print "density(T given T+noise==26) = ", density(T_posterior)(x)
