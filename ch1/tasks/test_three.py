"""Test the Task data type."""

from collections import namedtuple

import pytest

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


@pytest.mark.run_these_please
def test_member_access():
    """Check .field functionality of named tuple."""
    t = Task('buy milk', 'joey')
    assert t.summary == 'buy milk'
    assert t.owner == 'joey'
    assert (t.done, t.id) == (False, None)
