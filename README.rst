Introduction
============

pytest-stepwise is a plugin for `pytest <http://pytest.org/>`_ that run
all tests until a test fails, and then continue next test run from where
the last run failed. You may think of it as a combination of the  ``-x``
option, which exits the test run after a failing test, and the ``--lf``
option from pytest-cache, which only runs failing tests.

pytest-stepwise depends on pytest-cache, which will be installed by pip.


How to use it?
==============

1. Run ``py.test --stepwise`` (you can also use the alias ``--sw``).
2. Watch the test fail and fix it.
3. Run ``py.test --stepwise`` again. The test suite will continue to run
   right from where it was.


Changelog
=========

* 0.1 - Initial version.
