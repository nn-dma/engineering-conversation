
import polars as pl
import main as ct


def test_count_milestones():
    actual = ct.count(pl.DataFrame({}))
    assert actual == 0
