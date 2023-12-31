from pathlib import Path

import numpy.random as np_rand


def create_roll_word_dict() -> dict[str, str]:
    filepath_large_wordlist = Path(__file__).parent / "eff_large_wordlist.txt"

    with open(filepath_large_wordlist) as file:
        # using dictionary comprehension to read the file's lines into a dict
        roll_word_pair: dict[str, str] = {
            roll: word
            for line in file
            for (roll, word) in [line.strip().split(None, 1)]
        }

    return roll_word_pair


def rollit() -> str:
    # using default_rng with PCG64DXSM to generate 5 random integers between 1 and 6 - our roll
    random_gen = np_rand.default_rng(np_rand.PCG64DXSM())
    np_roll = random_gen.integers(low=1, high=7, size=5)

    return "".join(str(value) for value in np_roll)


def generate_passphrase(number: int, separator: str) -> str:
    r_w_dict: dict = create_roll_word_dict()
    passphrase: str = ""

    for _ in range(number):
        passphrase += r_w_dict[rollit()] + separator

    return passphrase[:-1]
