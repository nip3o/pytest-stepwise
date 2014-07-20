Introduction
============

pytest-stepwise is a plugin for `pytest <http://pytest.org/>`_ that run
all tests until a test fails, and then continue next test run from where
the last run failed. You may think of it as a combination of the  ``-x``
option, which exits the test run after a failing test, and the ``--lf``
option from pytest-cache, which only runs failing tests.

pytest-stepwise depends on pytest-cache, which will be installed as a
dependency.


How to use it?
==============

0. Install the plugin - ``pip install pytest-stepwise``.
1. Run ``py.test --stepwise`` (you can also use the alias ``--sw``).
2. Watch the test fail and fix it.
3. Run ``py.test --stepwise`` again. The test suite will continue to run
   right from where it was.


When is this useful?
====================

pytest-stepwise was written for use when a large part of the test suite
is failing. In this case, pytest-stepwise allows you to focus on fixing
one test at the time instead of being overwhelmed by all failing
tests. It should however be noted that all tests need to be re-run after
to make sure that any changes made when fixing one test has not broken
some other test.\\

Please send me a tweet if you have any suggestions regarding the
usefulness of pytest-stepwise.\\


Changelog
=========

* 0.1 - Initial version.
* 0.2 - Clear cache after test run when the plugin is not active.
  Added  ``--skip`` option.
