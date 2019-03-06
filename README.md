# Countdown

In a Countdown letters game, contestants form the longest anagram they can from a scramble of nine somewhat random letters (including at least three vowels and four consonants). No letter may be used more often than it appears in the scramble. More information on the rules (and controversies!) of the game can be found [here](https://en.wikipedia.org/wiki/Countdown_(game_show)#Letters_round) and [here](http://wiki.apterous.org/Letters_game). This script takes a nine letter string from the user and prints out a list of anagrams for the longest three lengths. For example, for the input `qwertyuio` the script prints:
```
7 letter words: quoiter, torquey
6 letter words: equity, quiety, quoter, requit, roquet, ryotei, torque, towery
5 letter words: ourey, ourie, outer, outie, outre, owrie, query, quiet, quire, quirt, quite, quoit, quote, rioty, roque, rouet, route, rowet, royet, ruote, ryoti, toque, tower, towie, uteri, write, wrote
Time taken: 0.3727662639994378s
```

## Word list

The dictionary used in this script contains 122160 unique words sourced from the spreadsheet [here](https://countdownresources.wordpress.com/2018/10/13/complete-list-of-words-ordered-by-how-useful-they-are-for-countdown/). A copy of that 32.6 MB spreadsheet is also available in this repository, called [dictionary-original.xlsx](dictionary-original.xlsx). A second 17.2 MB spreadsheet, [dictionary.xlsx](dictionary.xlsx) has had redundant worksheets removed leaving only the `overall` worksheet. Even so, the [lookup.py](lookup.py) script still takes over 15 seconds to produce the word list file, [dictionary.txt](dictionary.txt), but this isn't too much of a problem because it only needed to be ran once.

The [lookup.py](lookup.py) script iterates over the rows in a column and adds them to the `words` list. In the spreadsheet words that are anagrams are stored in the same cell. For example, the `C9` cell has value `RODENTIA/RATIONED/ORDINATE/NADORITE/DERATION`, the script separates this into the lowercase set: `{'rodentia', 'rationed', 'ordinate', 'nadorite', 'deration'}` and appends these values to the `words` list. The script then adds the all list to [dictionary.txt](dictionary.txt).