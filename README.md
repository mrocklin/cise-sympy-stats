This repository contains examples from the article 

["Symbolic Statistics with SymPy"](http://www.computer.org/csdl/mags/cs/2012/03/mcs2012030088-abs.html)

by

[M. Rocklin](http://matthewrocklin.com/) and [A. Terrel](http://andy.terrel.us)

In the June 2012 issue of Computations in Science and Engineering

These examples depend on the development version of
[SymPy](http://github.com/sympy/sympy)

SymPy.stats has developed since the printing of this article. As a result some
slight syntax differences exist

 * Functions that transform stochastic expressions into deterministic ones
 such as Density, Var, Sample have been lower-cased to density, variance,
 sample. P and E remain upper-cased.

 * Functions that create random variables now explicitly require a symbol name.
   I.e `T = Normal(30, 3)` is now written `T = Normal('T', 30, 3)`
