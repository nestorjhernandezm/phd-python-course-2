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
:math:`\mathcal{R}(c) = 5000 \times \mathcal{I}(c) 5000` points. This is
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
In the ``mandelbrot.py`` the ``\\@profile`` decorator is included, but
commented, if a developer wants to profile a code that calls the function
of given method. For example, if it is desited to profile the methods
when using ``my_script.py``, this can be made by doing::

  kernprof -l -v my_script.py

.. Getting Started
.. ---------------
.. As a first step, once having decompressed the ``.zip`` file or cloning
.. the repository, you can generate all the examples data by doing::

..   cd ~/phd-python-2/
..   python generate_mandelbrot_datasets.py 8

.. This creates a CSV file named ``data.csv`` locally at
.. ``~/phd-python-1/lorenz``. The structure of this file is described in
.. the docstring of the ``save_data`` function in the
.. ``~/phd-python-1/lorenz/filehandling.py`` module. Basically, the idea
.. is to vertically stack all the parameters and states, available
.. ``data`` input variable and store them as CSV.

.. Basic Parameters
.. ----------------
.. To generate all the solutions, we simply used the initial conditions:
.. ``x0 = 0.01``, ``y0 = 0`` and ``z0 = 0``. For the Euler-based solver,
.. we used a total number of points and step size of: ``N = 5000`` and
.. ``t_delta = 0.01``. This generated all our solutions properly and
.. in a reasonable amount of time.


.. Plotting
.. --------
.. For plotting the data for a given testcase, simply do::

..   cd ~/phd-python-1/cases
..   python testcase1.py  # For example for the testcase 1
..   python testcase2.py  # For example for the testcase 2 and so on..

.. Those scripts simply call a generic ``caseX.py`` script in the same
.. ``~/phd-python-1/cases`` that checks for the required parameters from
.. a dictionary and call the Python Pandas API for simple plotting.
.. The plotting scripts and other related plotting functionalities are
.. available in ``plot.py``. Once a testcase X is ran, you should observe
.. a new folder called ``caseX_files`` in the ``~/phd-python-1/cases``
.. that contains all the required 2D and 3D plots.

.. Also, you can test to run these testcases without running ``run.py``.
.. Here, if the ``caseX.py`` notices that the file is not available, it
.. simply creates a ``data_caseX.csv`` and stores it in the respective
.. folder.

.. Unit Testing
.. ------------
.. A basic functionality for unit testing the solver is included in
.. ``~/phd-python-1/test/test.py``. For simplicity, it is only included
.. for the solver to show its purpose and functionality. You can check this by running (and observing)::

..   cd ~/phd-python-1/test
..   python test.py
..   test_initial_condition (__main__.TestComputeStates) ... ok
..   test_known_outputs (__main__.TestComputeStates) ... ok
..   test_zero_output (__main__.TestComputeStates) ... ok

..    ----------------------------------------------------------------------
..    Ran 3 tests in 0.000s

..    OK

.. Final comment
.. -------------
.. The mini-project source code and structure was intended to be as easy and
.. self-explanatory as possible, with proper inline comments added for
.. non-obvious commands. I hope that you find it easy as well.

.. Happy reading!
.. Best,
.. Nestor J. Hernandez M.
