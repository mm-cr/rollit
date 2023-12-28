import numpy
import numpy as np
from numpy.random import PCG64DXSM


class Generator:
    def create_roll_word_dict(self) -> dict[str, str]:
        with open("eff_large_wordlist.txt") as file:
            # using dictionary comprehension to read the file's lines into a dict
            roll_word_pair: dict[str, str] = {
                roll: word
                for line in file
                for (roll, word) in [line.strip().split(None, 1)]
            }

        return roll_word_pair

    def rollit(self) -> str:
        # using default_rng with PCG64DXSM to generate 5 random integers between 1 and 6 - our roll
        random_gen = np.random.default_rng(PCG64DXSM())
        np_roll = random_gen.integers(low=1, high=7, size=5)

        return "".join(str(v) for v in np_roll)
