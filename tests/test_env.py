from env import PROJECT_ROOT, TEST_ROOT, SRC_ROOT
from pathlib import Path


def test_env():
    tr = Path(TEST_ROOT)
    assert str(tr.parent.absolute()) == PROJECT_ROOT

    sr = Path(SRC_ROOT)
    assert str(sr.parent.absolute()) == PROJECT_ROOT
