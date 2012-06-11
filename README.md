This repository contains examples from the article 

"Symbolic Statistics with SymPy"
by
M. Rocklin and A. Terrel

to appear in Computations in Science and Engineering

These examples depend on the development version of SymPy

SymPy.stats has developed since the printing of this article. As a result some
slight syntax differences exist

 * Functions that transform stochastic expressions into deterministic ones
 such as Density, Var, Sample have been lower-cased so to density, variance,
 sample

 * Functions that create random variables now explicitly require a symbol name.
   I.e `T = Normal(30, 3)` is now written `T = Normal('T', 30, 3)`
