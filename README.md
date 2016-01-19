# WordBrain solver

This __python 3__ script was build to solve the puzzles given by the __Android app "Wordbrain" by "MAG Interactive"__.

It achieves that by extracting words from the database of http://dict.cc and combining all given characters.

Because of their license, I am not able to include the database in this Repo and you have to download it by yourself. (http://www1.dict.cc/translation_file_request.php)

First execute `extract.py` to extract a unique list of words from the translation database.

Then use `solve.py` to solve the puzzles using the prepared list of words.

I am running this under Ubuntu, so I can not tell, whether it works on Windows.

Additionally the script might focus on German words.

Example usage:
```
$ ./solve.py 
WORDBRAIN solver
Running on 4 cores!
Please enter the characters of each line (. = End)
seyd
tdar
imab
onez
.
Minimum length: 4
Maximum length: 7
Starting to solve... (This may take a while...)
Press CTRL-C to cancel
Estin
Yeti
Dyade
Yard
Dada
daran
darben
damit
Dame
Damen
Dryade
Dram
Drama
Dram
Drama
dran
Team
Tide
Timar
Timar
daran
darben
damit
timen
Dame
Damen
Ayran
Tinea
Dime
Dione
Dinar
Dino
darben
Adar
Adam
damit
Adamin
Dame
Damen
Aram
Aramid
Arame
Arbe
Amid
Idmon
Amida
Amin
Radi
amoi
Radio
Rada
Amen
Rabe
Raben
Made
Rada
Radi
Radio
Mara
Maar
Abra
Rabe
Raben
Mine
Made
Maar
Adar
Adam
Adamin
Mara
Mani
Monade
Bayram
Badam
Aram
Aramid
Arame
Arbe
Omar
Omar
Oman
Amid
Amida
Omen
Amin
amoi
Amen
Abra
Bran
Badam
Anima
Emdet
Animo
Anime
Narbe
Name
Nabe
Bardame
Noma
Nomade
Noma
Nomade
NEMA
NEMA
Bema
Bema
Zadar
Beamte
Beamtin
Zebra
Zebra
Zebrano
Zenit
Found 73 possible solutions in 0:00:01.863262:
Abra
Adam
Adar
Amen
Amid
Amin
amoi
Aram
Arbe
Bema
Bran
Dada
Dame
Dime
Dino
Dram
dran
Maar
Made
Mani
Mara
Mine
Nabe
Name
NEMA
Noma
Oman
Omar
Omen
Rabe
Rada
Radi
Team
Tide
Yard
Yeti
Amida
Anima
Anime
Animo
Arame
Ayran
Badam
Damen
damit
daran
Dinar
Dione
Drama
Dyade
Emdet
Estin
Idmon
Narbe
Raben
Radio
Timar
timen
Tinea
Zadar
Zebra
Zenit
Adamin
Aramid
Bayram
Beamte
darben
Dryade
Monade
Nomade
Bardame
Beamtin
Zebrano
```
