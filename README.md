
# BIP39 checksum word-finder


## file name 
bip39checksumFinder.py


## description 
BIP-39 tool. 
This code finds all possible checksum words for a 12 or 24 mnemonic (seed phrase)

BIP-39 enables storing your private keys as a set of words instead of a binary string.
For more info see the [BIP39 spec](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) 

This code allows you to choose the first 11 or 23 seed words and returns a list of all possible checksum words, so you can choose from that list the 12th or 24th word for your mnemonic / seed.


## requirements
Python 2.7 or Python 3.x


## dependencies

```
pip3 install mnemonic
```


## how to run

- `$ git clone REPO`
- `$ pip3 install mnemonic`
- `$ python3 bip39checksumFinder.py`
- 
- Enter the 11 or 23 words sequence (single line, words separed by a space) you want to test
- You will get a list of all 12th or 24th words bip39 that validate the checksum
	- 128 possible words for a 12 word seed
	- 8 possible words for a 24 word seed


## WARNING

#### This script should be run on an air-gapped computer to prevent malware and key loggers from reading your mnemonic. For valuable seeds, it is highly recommended to run the code from an offline computer.


## Example:

For a 24 word phrase, we would only supply 23 words and see what legal words are possible for the 24th.

```
$ python3 bip39checksumFinder.py

Enter your seed (11 or 23 words):

abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress

And your checksum words are:

blanket climb frozen hill mushroom piano seed truck

```

We can pick ```frozen``` as the final word to make our phrase:

```
abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress frozen
```


Lets try with a 12 word phrase. We only supply 11 words:

```
$ python3 bip39checksumFinder.py

Enter your seed (11 or 23 words):

abandon ability able about above absent absorb abstract absurd abuse access

And your checksum words are:

ability actress aisle alert analyst any arrive august avoid banner better blade blur breeze brother burden canal casual century check circle cliff clump company coyote crazy cross damp decorate depend develop dilemma doctor drill dust either emerge engine ethics excuse fabric fame female fitness flight foam foster garbage ghost glow good gravity hat health hobby hover impose income inspire jealous judge kind lab leaf length list lunch manage matter melody minor modify muscle mutual nice note oblige orange oven paddle pattern person planet pole potato program punch purchase ramp record remove rescue reveal romance rural salt sea sentence shift shock situate slab social soon spare stable staff stool suffer sustain tackle teach theme timber tomato track true turtle umbrella used vapor vicious vintage warfare weird wine woman wrap

```

By picking ```turtle``` as the final word, our 12-word phrase becomes:

```
abandon ability able about above absent absorb abstract absurd abuse access turtle

```


## Other Languages

Make sure the language words are under ```wordlist``` directory
You can find all available languages here: https://github.com/bitcoin/bips/tree/master/bip-0039

You can set your language changing it on the code line:

```python
m = mnemonic.Mnemonic("english")
```

ex.

```python
m = mnemonic.Mnemonic("spanish")
```


## donate:
If you liked this code, you can donate to: https://getalby.com/p/pingtospace


## license:
[WTFPL](http://www.wtfpl.net/) 


## addendum:
#### dont trust - verify

Before using a new seed, always verify it's validity.
You can use Ian Coleman's and/or Kimbatt's code for checking the seed and derive addresses and keys

https://iancoleman.io/bip39/
https://github.com/iancoleman/bip39 

https://kimbatt.github.io/btc-address-generator/?page=mnemonic-seed
https://github.com/Kimbatt/btc-address-generator


*WARNING!!! Always do all of this on an air-gapped computer.
Both Ian Coleman's and Kimbatt's are HTML code for download!
You must save the website by pressing CTRL-S or right click -> Save website (or something)

**Recomended:
You can also use both codes to add the Passphrase an then derive and check addresses


----

