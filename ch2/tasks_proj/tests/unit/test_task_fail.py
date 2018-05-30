"""Use the Task type to show test failures."""
from tasks import Task


def test_task_equality():
    """Different tasks should not be equal."""
    t1 = Task('sit there', 'joey')
    t2 = Task('do something', 'hu')
    assert t1 == t2


def test_dict_equality():
    """Different tasks compared as dicts should not be equal."""
    t1_dict = Task('make sandwich', 'hu')._asdict()
    t2_dict = Task('make sandwich', 'hv')._asdict()
    assert t1_dict == t2_dict