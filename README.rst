Introduction
============

pytest-stepwise is a plugin for `pytest <http://pytest.org/>`_ that run
all tests until a test fails, and then continue next test run from where
the last run failed. You may think of it as a combination of the  ``-x``
option (which exits the test run after a failing test) and the ``--lf``
option from pytest-cache (which only runs failing tests), except that
it does not restart the test run from the beginning as soon as a test
passes.

pytest-stepwise depends on pytest-cache, which will be installed as a
dependency.


How to use it?
==============

0. Install the plugin - ``pip install pytest-stepwise``.
1. Run ``py.test --stepwise`` (you can also use the alias ``--sw``).
2. Watch the test fail and fix it.
3. Run ``py.test --stepwise`` again. The test suite will continue to run
   right from where it was.

Use the ``--skip`` option to ignore one failing test and stop the
test execution on the second failing test instead. This is useful if you
get stuck on a failing test and just want to ignore it until later.


When is this useful?
====================

pytest-stepwise was written for use when a large part of the test suite
is failing. In this case, pytest-stepwise allows you to focus on fixing
one test at the time instead of being overwhelmed by all failing
tests. It should however be noted that all tests need to be re-run after
to make sure that any changes made when fixing one test has not broken
some other test.

Please submit an issue if you have any suggestions regarding use cases
of pytest-stepwise.


Compatibility
=============

pytest-stepwise is compatible with pytest 2.2 -> 2.8.
For pytest 2.7 and earlier, ``pytest-cache`` is required as a dependency.


Changelog
=========

* 0.1 - Initial version.
* 0.2 - Clear cache after test run when the plugin is not active.
  Added  ``--skip`` option.
* 0.3 - Fixed issue when failing tests are removed.
  Fixed compatibility with ``--pdb`` option.
  Stop on errors as well as on test failures.
* 0.4 - Refactoring, pytest 2.8 compatiblity. Stop test execution on
  collection errors.
