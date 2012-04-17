from sympy import *
from sympy.stats import *

T = Normal(30,3)
print "P(T>33) = ", P(T>33, evaluate=False)
print "        = ", P(T>33)
print "        = ", P(T>33).evalf()

noise = Normal(0, 1.5)
observation = T + noise

T_posterior = given(T, Eq(observation, 26))

print "density(T given T+noise==26) = ", density(T_posterior)
