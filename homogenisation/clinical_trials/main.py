import polars as pl
import click


@click.command()
@click.option("-i", "--input-path", "input_path", required=True, type=str, help="csv with the clinical trials data")
def main(input_path: str):
    trials_raw = read_trials(input_path)
    result = homogenise(trials_raw)
    print(result)


def read_trials(path: str) -> pl.DataFrame:
    return pl.read_csv(path)


def count(trials: pl.DataFrame) -> int:
    return 0


def homogenise(trials: pl.DataFrame) -> pl.DataFrame:
    # Here be interesting code
    return trials


if __name__ == "__main__":
    main()
