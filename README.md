# A dynamic model identification package for the da Vinci Research Kit (under development)

There are parallelograms, springs, tendon couplings, cables, and counterweight in da Vinci Research Kit (dVRK)
so that we can not use existing tools to identify the dynamic parameters of it.
This software framework was developed to solve these problems.
Although this package was initially developed for the dVRK, it is also very easy to use it to identify the dynamic
parameters of other robots.


## Procedure

<p align="center">
  <img src="https://github.com/wangyanhit/dyn_ident_sympy/blob/master/design/workflow.png" width="500" title="hover text">
</p>

## Features
### Finished
* Symbolic dynamic modelling based on DH parameters and geometric tree
    * Geometrical modelling
    * Dynamic modelling
    * Base parameter generation using QR decomposition
* Optimal excitation trajectory generation based on fourier-series

* Data processing
    * Derive velocity and acceleration from position measurements
    * Zero-phase low-pass filter for original data
    * Remove the data whose velocity is close to zero to decrease the noise for Coulomb friction
* Identification
    * Joint cable torque identification
    * Ordinary Least Square (OLS)
    * Weighted Least Square (WLS)
    * Convex Optimization
* Excitation of robots, using [dVRK ROS stack](https://github.com/jhu-dvrk/dvrk-ros)
### Yet to be done
* Output of the identified parameters to files
* Output of C++ or Python code of identified dynamic model for control use 
* Regularize output print

## Requirements
* Python 2.7
* Python modules
    * NumPy, SciPy, SymPy, CvxOpt, Matplotlib, PyOpt, cloudpickle


Anaconda is recommended.


## Examples
* [Master Tool Manipulator (MTM)](https://github.com/wangyanhit/dyn_ident_sympy/blob/master/main_mtm.ipynb)

* [Patient Side Manipulator (PSM)](https://github.com/wangyanhit/dyn_ident_sympy/blob/master/main_psm.ipynb)

## Author
Yan Wang and Radian Gondokaryono, from [WPI AIM Lab](http://aimlab.wpi.edu/) 

## Reference
When developing this work, we referred a lot from the following places:
* [SymPyBotics](https://github.com/cdsousa/SymPyBotics)
* [FloBaRoID](https://github.com/kjyv/FloBaRoID)

## Some problems
When I was using PyOpt, I found some problems with it. In pySLSQP.py file, these changes should be made to make it work.
```
gg = numpy.zeros([la], numpy.float) ==> gg = numpy.zeros(la, numpy.float)

dg = numpy.zeros([la,n+1], numpy.float) ==> dg = numpy.zeros([la[0], n + 1], numpy.float)

w = numpy.zeros([lw], numpy.float) ==> w = numpy.zeros(lw, numpy.float)

jw = numpy.zeros([ljw], numpy.intc) ==> jw = numpy.zeros(ljw, numpy.intc)
```

		
