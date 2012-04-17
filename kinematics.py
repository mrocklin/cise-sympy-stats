from sympy import *
from sympy.stats import *

# Symbols for position, velocity, angle, time, gravity
x0, y0, yf, v, theta, t, g = symbols('x0 y0 y_f v theta t g')
# x and y positions as a function of time
x = x0 + v*cos(theta)*t
y = y0 + v*sin(theta)*t + g/2*t**2
# Solve y = yf for time to obtain the duration of the flight
t_impact = solve(y-yf, t)[1]
# Final x value of cannon ball on impact
xf = x0 + v*cos(theta)*t_impact

print "\n\nsymbolic xf = ", xf

xf_num = xf.subs({g: -Rational(98,10), v: 10, theta: pi/4, x0: 0, y0: 10,
                  yf: 0})

print "\n\nnumeric xf = ", xf_num
print "numeric xf = ", xf_num.evalf()

# 4.1
y0_uncertain = Normal(10,1)
xf_uncertain = xf.subs({g: -Rational(98,10), v: 10, theta: pi/4, x0: 0,
                        y0: y0_uncertain, yf: 0})

print "\n\nexpecatation and variance of xf when y0 is uncertain"
print "E(xf)   = ", E(xf_uncertain, evaluate=False)
print "        = ", E(xf_uncertain).evalf()
print "Var(xf) = ", variance(xf_uncertain).evalf()

# 4.2
v_uncertain = Uniform(9, 11.5)
theta_uncertain = Normal(pi/4, pi/20)
xf_uncertain = xf.subs({g: -Rational(98,10), v: v_uncertain,
                        theta: theta_uncertain, x0: 0, y0: y0_uncertain, yf: 0})

print "\n\nComplex probability"
print "P(theta>pi/4 given xu>16) = ", P(theta_uncertain>pi/4, xf_uncertain>16, numsamples=1000)
