import pytest

import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # This is where the testing happens.
    yield

    # Teardown: stop db
    tasks.stop_tasks_db()


def test_count_returns_zero_for_empty_database():
    """tasks.count() should return zero for an empty database."""
    # GIVEN an initialized tasks db
    # WHEN count is call
    # THEN zero should be returned
    assert tasks.count() == 0


def test_count_returns_one_for_database_with_one_task():
    """tasks.count() should return one for a database with one task."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    #   AND count is called
    # THEN one should be returned
    tasks.add(Task('do something'))
    assert tasks.count() == 1


def test_count_returns_two_for_database_with_two_tasks():
    """tasks.count() should return two for a database with two tasks."""
    # GIVEN an initialized tasks db
    # WHEN two tasks are added
    #   AND count is called
    # THEN one should be returned
    tasks.add(Task('do something'))
    tasks.add(Task('do something else'))
    assert tasks.count() == 2