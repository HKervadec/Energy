# Energy
Python implementation of:
- Kolmogorov, V., & Zabin, R. (2004). ["What energy functions can be minimized via graph cuts?"](http://ieeexplore.ieee.org/abstract/document/1262177/). IEEE transactions on pattern analysis and machine intelligence, 26(2), 147-159.


I relied heavily on [BK_Matlab](http://vision.csd.uwo.ca/wiki/vision/upload/d/d7/Bk_matlab.zip) by Andrew Delong, mostly for the `energy.h` file and its use in `bk_matlab.cpp`.
This work requires [PyMaxflow](https://github.com/pmneila/PyMaxflow), which can be easily installed with `pip install pymaxflow`, or compiled from sources if necessary.

A few differences remain:
* Not all functions from `energy.h` have been implemented, especially `add_term2` and some variants of `add_term2`.
* The current PyMaxflow does not return the `marked` boolean from `add_tedge`, it is void instead. Therefore, minimization cannot reuse the trees.
    * It can be modified quite easily if needed.

## Use
The easiest way to use this repository is to add its parent folder (where you cloned the repository) to the `PYTHONPATH` environment variable, such as:
```
echo export PYTHONPATH="$PYTHONPATH:~/code" >> ~/.zshrc


>>> from Energy.energy import Energy
```
Or, alternatively:
```
echo export PYTHONPATH="$PYTHONPATH:~/code/Energy" >> ~/.zshrc


>>> from energy import Energy
```