import pytest
from raiseSysExit import raise_sys_exit

def test_exit():
    with pytest.raises(SystemExit):
        raise_sys_exit()
