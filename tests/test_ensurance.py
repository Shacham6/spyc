import pytest
from spyc import ensure, TargetInvalidException


def test_ensure_passes_quitely_when_fits_spec():
    ensure(2, int)


def test_raises_target_invalid_when_not_fits_spec():
    with pytest.raises(TargetInvalidException):
        ensure(2, str)
