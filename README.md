# WordBrain solver

This __python 3__ script was build to solve the puzzles given by the __Android app "Wordbrain" by "MAG Interactive"__.

It achieves that by extracting words from the database of http://dict.cc and combining all given characters.

Because of their license, I am not able to include the database in this Repo and you have to download it by yourself.

First execute `extract.py` to extract a unique list of words from the translation database.

Then use `solve.py` to solve the puzzles using the prepared list of words.

I am running this under Ubuntu, so I can not tell, whether it works on Windows.

Additionally the script might focus on German words.

Example usage:
```
$ ./solve.py 
Please enter the characters of each line (. = End)
BTP
LUE
UPP
.
Starting to solve... (This may take a while...)
B
Bute
Blut
tue
Tulpe
Pep
Pep
Puppe
Puppe
Pul
Pulpe
Pult
Pub
Pute
Luppe
Lupe
Luppe
Lupe
Lupe
Luppe
Lupe
LTE
U
et
U
Pul
Pult
Pul
Pult
Pub
Pute
Pep
Pep
Pul
Pulpe
Pult
Pub
Pute
Pep
Pep
Found 17 solutions in 66.79791498184204 seconds:
U
B
et
Pep
Pul
LTE
Pub
tue
Pult
Lupe
Blut
Bute
Pute
Luppe
Puppe
Tulpe
Pulpe
```
