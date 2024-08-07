from pathlib import Path


def read_file(file: Path) -> list[str]:
    with open(file) as f:
        return [line.strip() for line in f.readlines()]


def calculate(prediction: list[str], final: list[str]) -> int:

    assert set(prediction) == set(final)

    position_diffs = sum(
        abs(index - final.index(team))
        for index, team in enumerate(prediction)
    )

    champion_bonus = 10 if prediction[0] == final[0] else 0
    relegation_bonus = 5 * len(set(prediction[-3:]).intersection(final[-3:]))
    top4_bonus = 5 * len(set(prediction[:4]).intersection(final[:4]))

    return position_diffs - champion_bonus - relegation_bonus - top4_bonus


def main() -> None:

    final_table = read_file(Path("final_table.txt"))

    predictions: dict[str, list[str]] = {
        file.stem: read_file(file)
        for file in Path("predictions").glob("*.txt")
    }

    for user in predictions:
        print(f"{user}: {calculate(predictions.get(user), final_table)}")


if __name__ == "__main__":
    main()
