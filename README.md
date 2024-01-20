# rollit: a dice-based passphrase generator

## What
Rollit is a Diceware-based strong passphrase generator that utilizes NumPy's Pseudo-Random Number Generator and the EFF's wordlists.

- Diceware is a method proposed by Arnold G. Reinhold, to choose a secure passphrase using 'Diceware wordslists.'

- With Numpy, we can employ the updated version of the permuted congruential generator-64 algorithm (the PCG64DXSM) to generate our (pseudo) random values.

- The Electronic Frontier Foundation offers different wordlists to use along the Diceware technique to generate passphrases.

## Why
Sometimes, we need to quickly and easily generate a strong passphrase for security purposes, for example, when using tools like OpenPGP. Rollit provides a user-friendly way to do it from the command line.

## How
Run `rollit` command without any options. It will display a four-word passphrase, separated by '-'

If you want to generate more words, use the option `--number` (`-n`):

`rollit -n 6`

`rollit --number 6`

To change the default separator, use the option `--separator` (`-s`):

`rollit -n 6 -s _`

`rollit --number 6 --separator _`

## References
Diceware: http://diceware.com

PCG algorithms: https://www.pcg-random.org/

EFF Dice-Generated Passphrases: https://www.eff.org/dice

