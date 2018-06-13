import pytest

import tasks
from tasks import Task


@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup: start db.
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # This is where the testing happens.

    #Teardown: stop db.
    tasks.stop_tasks_db()


# Reminder of Task constructor interface
# Task(summar=None, owner=None, done=False, id=None)
# summary is required
# owner and done are optional
# id is set by database


@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Joey', True),
        Task("Review Joey's code", 'Katie', False),
        Task('Fix what Joey did', 'Michelle', False),
    )


@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),
        Task('Create', 'Michelle'),
        Task('Enspire', 'Michelle'),
        Task('Encourage', 'Michelle'),
        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'),
    )