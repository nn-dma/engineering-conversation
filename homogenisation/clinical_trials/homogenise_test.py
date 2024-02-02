
import polars as pl
import main as ct


def test_homogenise_milestones():
    actual = ct.homogenise(pl.DataFrame({}))
    assert actual.is_empty()
