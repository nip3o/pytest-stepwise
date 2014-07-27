import pytest
from pytest_cache import Cache
from pytest import Session

__version__ = '0.2'


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption('--sw', action='store_true', dest='stepwise',
                    help='ignore')
    group.addoption('--stepwise', action='store_true', dest='stepwise',
                    help='exit on test fail and continue from last failing test next time')
    group.addoption('--skip', action='store_true', dest='skip')


@pytest.mark.tryfirst
def pytest_configure(config):
    config.cache = Cache(config)
    config.pluginmanager.register(StepwisePlugin(config), 'stepwiseplugin')


class StepwisePlugin:
    def __init__(self, config):
        self.config = config
        self.active = config.getvalue('stepwise')

        if self.active:
            self.lastfailed = config.cache.get('cache/stepwise', set())
            self.skip = config.getvalue('skip')

    def pytest_collection_modifyitems(self, session, config, items):
        if not self.active or not self.lastfailed:
            return

        # Make a list of all tests that has been runned before the last failing one.
        already_passed = []
        for item in items:
            if item.nodeid in self.lastfailed:
                break
            else:
                already_passed.append(item)

        for item in already_passed:
            items.remove(item)

        config.hook.pytest_deselected(items=already_passed)

    def pytest_runtest_logreport(self, report):
        # Skip this hook if plugin is not active, the test has not run yet, or the test is xfailed.
        if not self.active or report.when != 'call' or 'xfail' in report.keywords:
            return

        if report.failed:
            if self.skip:
                # Remove test from the skipped ones and unset the skip option
                # to make sure the following tests will not be skipped.
                self.lastfailed.discard(report.nodeid)
                self.skip = False
            else:
                # Mark test as the last failing and interrupt the test session.
                self.lastfailed.add(report.nodeid)
                raise Session.Interrupted('Test failed, continuing from this test next run.')
        else:
            self.lastfailed.discard(report.nodeid)

    def pytest_sessionfinish(self, session):
        if self.active:
            self.config.cache.set('cache/stepwise', self.lastfailed)
        else:
            # Clear the list of failing tests if the plugin is not active.
            self.config.cache.set('cache/stepwise', set())
