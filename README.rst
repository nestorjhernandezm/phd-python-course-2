Introduction
------------
This structure contains the mini-project for the course
"Scientific Computing using Python, part 2", held at Aalborg University,
May 2016. The main and only author of this source code is Nestor J.
Hernandez M. The structure is stored and sent as a ``.zip`` file, but also
available at: https://bitbucket.org/nestorjhernandezm/phd-python-2/

You can get access to this repository by cloning it, by doing
in a terminal::

  git clone git@bitbucket.org:nestorjhernandezm/phd-python-2.git

Or, if you don't have SSH, by doing::

  git clone https://nestorjhernandezm@bitbucket.org/nestorjhernandezm/phd-python-2.git

Please, be sure that you have the necessary setting for either SSH or HTTPS
to clone the repository. If something does not work, let the author know.

For simplicity, we assume that you have clone or stored your repository
in ``~/phd-python-2/``. The mini-project is based in the Mandelbrot set.
This set contains all the elements for which the equation :math:`z_{i+1} = z_i^2 + c,\ i \in [0,1, \ldots, I]`, with :math:`c \in \mathbb{C}` the
tested number does not diverge. A good introductory description can be
found in [1_].

.. _1: https://en.wikipedia.org/wiki/Mandelbrot_set

For this project, the initial point is :math:`z_{0} = 0` and maximum number
of iterations per point is :math:`I = 100`. To verify the convergence,
we check that every iteration is below a given threshold, e.g.
:math:`z_{i} < T = 10`. In the mini-project, we refer to this variable
simply as ``threshold``.

The purpose of the mini-project is to calculate the set and plot it.
To do so, we calculate if a point belongs to the set for a grid of
:math:`\mathcal{R}(c) = 5000 \times \mathcal{I}(c) = 5000` points. This is
made by picking 5000 points equally spaced from
:math:`-2 \leq \mathcal{R}(c) \leq 1` and the same for
:math:`-1.5 \leq \mathcal{I}(c) \leq 1.5`.

In principle, this is a heavy computation given the amount of points,
but fortunately highly parallelizable since the computation of
a given point does not depend on the others. A major objective of this
mini-project is to present and verify different computational methods
that optimize a basic naïve algorithm. In what follows, we provide a short
description of the mini-project.

Project Structure
-----------------
The project has a simple structure where all the files and scripts need
to be allocated in a single folder. The functionalities of the mini-project
have been separated in different scripts and single module ``mandelbrot.py``
that contains the different tested methods. In both the repository and
sent ``.zip`` file, we have included all this source code that:
(i) generates the datasets of each method (in
``generate_mandelbrot_datasets.py``), (ii) plots the data for each set (in
``plot.py``), verifies the correctness of a method with unit test functionality
(in ``test``), benchmarks the time for each method to compute a solution
(in ``benchmark.py``) and includes a simple script that show the speed
gain when employing multiprocessing. For simplicity, details about
the algorithm have omitted since it is basic and known.

Computational Methods
---------------------
Five methods with different tools are considered for the mini-project:
Naîve, Vectorized, Numba, Cython and Multiprocessing. For the last one,
we include a variable number of cores to be included as an input argument.
All the used methods are defined in the ``mandelbrot.py`` module, except
the Cython one which is defined in the ``miniproject_mandelbrot.pyx`` file.
In the ``mandelbrot.py`` the ``profile`` decorator is included, but
commented, in case a developer wants to profile a code that calls the function
of given method. For example, if it is desired to profile the methods
when using ``my_script.py``, this can be made by uncommenting the
the decorators in ``mandelbrot.py`` and doing::

  cd ~/phd-python-2/
  kernprof -l -v my_script.py

About the Numba Method
----------------------
A short disclaimer is that, the ``.zip`` file sent for the mini-project
evaluation does not contain the data related to the Numba method since
the computer where the methods where tested did not have neither Numba
nor Conda installed. However, the Numba was tested in another computer
and its functionality was verified for both the method, plotting and
its tests. So, you should be able to try this method without any issues.
If you find problem with this method, please contact the author.

Cython binaries
---------------
For the Cython binaries, it is required to generate the library according
your architecture, Python and NumPy distributions. To do so, before
starting with the project, run::

  cd ~/phd-python-2/
  python setup.py build_ext --inplace

This should properly create the ``mandelbrot_c.so`` binary generated from
the ``miniproject_mandelbrot.c`` file and the ``build`` folder. These
two files and that folder are all the required items to properly use the
Cython method. Once this is done, it is now possible to generate all
the datasets.

Getting Started
---------------
Once having decompressed the ``.zip`` file or cloning
the repository, you can generate all the datasets by doing::

  cd ~/phd-python-2/
  python generate_mandelbrot_datasets.py CORES

Where ``CORES`` is the number of cores that you want to pass to the
multiprocessing function, for example:
``python generate_mandelbrot_datasets.py 8``. This creates 5 ``.npz`` files
named ``mandelbrot_[method]_data.npz`` for each of the mentioned methods
that stores the computed datasets. The dataset is a simple 2D numpy array
that contains the computed point stability of the given method. Each data
file is barely more than 200 MB since an array of 25.000.000 elements, each
of 64 bits is stored. The total to generate datasets is around 6 minutes in
an Intel i7 computer of 8 cores (without including the Numba method).

Plotting
--------
For plotting the data for all the datasets, simply do::

  cd ~/phd-python-2/
  python plot.py

The plotting functionality is available in ``plot.py`` and the plots
are stored locally. The ``imshow`` function from ``matplotlib.pyplot``
was adapted to store the resulting PDF image files. To control the image
resolution, the ``dpi`` parameter is used when storing an image.

Unit Testing
------------
A functionality for unit testing the sets computation is included in
``~/phd-python-1/test/test.py``. To test the accuracy of a given method,
the percentual relative error of all the points against
the naïve implementation is calculated. Then, all points within a 5% error
are considered good. If the total amount of correct points is more than
the 99.95%, we consider that the method test and implementation is correct.
The tests take around 13 minutes in an Intel i7 computer of 8 cores
(without including the Numba method). You can check this by running and
observing, for example::

  cd ~/phd-python-2/
  python test.py 8
  test_mandelbrot_cython (__main__.TestMandelbrot) ... 100.0% of correct values
  ok
  test_mandelbrot_multiprocessing (__main__.TestMandelbrot) ... Cores for test:   8. 100.0% of correct values
  ok
  test_mandelbrot_vectorized (__main__.TestMandelbrot) ... 100.0% of correct   values
  ok

  ----------------------------------------------------------------------
  Ran 3 tests in 777.144s

  OK

Benchmarks
----------
The methods processing time are done ``benchmark.py``. To run and observe
the benchmark results (similarly like the example shown below), simply type::

  cd ~/phd-python-2/
  python benchmark.py 8
  Points per axis = 5000
  mnb.mandelbrot_set_naive(Re_c, Im_c) :   2.36e+02 [s]
  mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c) :   1.37e+01 [s]
  mandelbrot_set_cython(Real_c + 1j * Imaginary_c) :   4.08e+01 [s]
  mnb.mandelbrot_set_multiprocessing(Real_c, Imaginary_c, 8) :   1.19e+01 [s]


Speed Processing Gain of Multiprocessing
----------------------------------------
The gain of multiprocessing against the vectorized method is shown by running
(and observing something similar to:) ::
  cd ~/phd-python-2/
  python multiprocessing_gain.py 8
  mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c) :   1.32e+01 [s]
  Speed gain computation...
  Cores for Multiprocessing, 1                              :   1.52e+01 [s]
  Cores for Multiprocessing, 2                              :   1.29e+01 [s]
  Cores for Multiprocessing, 3                              :   1.25e+01 [s]
  Cores for Multiprocessing, 4                              :   1.24e+01 [s]
  Cores for Multiprocessing, 5                              :   1.22e+01 [s]
  Cores for Multiprocessing, 6                              :   1.21e+01 [s]
  Cores for Multiprocessing, 7                              :   1.20e+01 [s]
  Cores for Multiprocessing, 8                              :   1.20e+01 [s]

At the end of this computation, there should be ``multiprocessing_gain.pdf``
file showing a plot of the gain. At the time of this writing, it has been
noticed that the multiprocessing implementation does not specifically fix
the number of cores but the number of processes used in the computation
instead.

Final comment
-------------
As with the first mini-project, the source code and structure of this project
was intended to be as easy as possible. I hope that you find it easy as well.
Finally, I want to highly thank the course instructors Postdoc
Tobias Lindstrøm Jensen and Prof. Thomas Arildsen for their help during
the submission of this mini-project.

Happy reading!
Best,
Nestor J. Hernandez M.
