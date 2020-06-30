|||
---|---|
|Author| Erika Leonor Basurto Munguia|
|Version| 1.0.0|
|Date| 25/06/2020|

# Test Heruglon Language
Their alphabet, in order, is: `sxocqnmwpfyheljrdgui`.

### Letter Classification
letters u, d, x, s, m, p, f are called "foo letters" while the other letters are called "bar letters".

### Prepositions
The prepositions are the words of exactly 6 letters which end in a foo letter and do not contain the letter u .
### Verbs
Verbs are words of 6 letters or more that end in a bar letter. Furthermore, if a verb starts in a bar letter,
then the verb is inflected in its subjunctive form.
### Numbers
Words also represent numbers given in base 20, where each letter is a
digit. The digits are ordered from the least significant to the most significant, which is the
opposite of our system. 

Heruglons consider a number to be pretty if it satisfies all of the following properties:
- it is greater than or equal to 81827
- it is divisible by 3

### Output
```txt
1) There are <n> prepositions in the text
2) There are <n> verbs in the text
3) There are <n> subjunctive verbs in the text
4) Vocabulary list: <words>
5) There are <n> distinct pretty numbers in the text
```

### How to run the script?
```bash
python -m source.Main
```