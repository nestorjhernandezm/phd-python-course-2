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
This set contains all the elements for which the equation :math:`z_{i+1} = z_i^2 + c,\ i \in [0,\ldots, i_{max}]`, with :math:`c \in \mathbb{C}` the
tested number does not diverge. A good introductory description can be
found in [1_].

.. _1: https://en.wikipedia.org/wiki/Mandelbrot_set

Typically, the initial point is :math:`z_{0} = 0`.


.. Normally, for these equations, we are given a set initial conditions
.. and parameters to compute the states all times. We achieve this in
.. the mini-project by computing the states (ODE solver) of the discretized
.. version of [1_] by the Euler method [2_]. For the mini-project, it was
.. required to plot the states in XYZ space and the planes: XY, XZ and YZ.
.. In our case, this is made by storing each of these plots in a PDF file.

.. .. _2: https://en.wikipedia.org/wiki/Euler_method

.. In what follows, we provide a short description of the mini-project.

.. Project Structure
.. -----------------
.. The project has the structure from the boilerplate suggested originally
.. at the course. Thus, we make use of the same ``lorenz``, ``cases`` and
.. ``test`` folders. In each of use, we have included all the source code
.. required to compute the solutions (in ``lorenz``), plot the data for
.. each testcase (in ``cases``) and make use of a basic unit test functionality
.. to verify simply correct outputs of the ODE solver (in ``test``).

.. The basic files from the boilerplate were modified to have all the
.. required functionalities from the project while keeping the same structure.
.. For the implemented functions, all the documentation has been added through
.. very descriptive Python docstrings. For each function, its docstring
.. describes: the returned value, behaviour and input parameters of the
.. function are described.

.. Getting Started
.. ---------------
.. As a first step, once having decompressed the ``.zip`` file or cloning
.. the repository, you can generate all the examples data by doing::

..   cd ~/phd-python-1/lorenz
..   python run.py

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
