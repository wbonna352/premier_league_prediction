from pathlib import Path


def read_file(file: Path) -> list[str]:
    with open(file) as f:
        return [line.strip() for line in f.readlines()]


def calculate(prediction: list[str], final: list[str]) -> int:

    assert set(prediction) == set(final), "prediction and final must contain the same set of teams"

    position_diffs = sum(
        abs(index - final.index(team))
        for index, team in enumerate(prediction)
    )

    bonuses: dict[str, int] = dict(
        champion=10 if prediction[0] == final[0] else 0,
        relagtion=5 * len(set(prediction[-3:]).intersection(final[-3:])),
        top4=5 * len(set(prediction[:4]).intersection(final[:4])),
        top6=3 * len(set(prediction[:6]).intersection(final[4:6]))
    )

    return position_diffs - sum(bonuses.values())


def main() -> None:

    final_table = read_file(Path("final_table.txt"))

    prediction_files = Path("predictions").glob("*.txt")

    predictions: dict[str, list[str]] = {
        file.stem: read_file(file)
        for file in prediction_files
    }

    for user, prediction in predictions.items():
        score = calculate(prediction, final_table)
        print(f"{user}: {score}")


if __name__ == "__main__":
    main()
