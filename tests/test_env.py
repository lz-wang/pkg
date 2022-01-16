from pathlib import Path

from env import PROJECT_ROOT, TEST_ROOT, SRC_ROOT


def test_env():
    tr = Path(TEST_ROOT)
    assert str(tr.parent.absolute()) == PROJECT_ROOT

    sr = Path(SRC_ROOT)
    assert str(sr.parent.absolute()) == PROJECT_ROOT
