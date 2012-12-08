import __init__
import sys
'''
Test cases:
- Common words mispelled
- Concepts mispelled. Context inferable from correct words
- Concepts

'''
sentences = ['I want to go to the beach to sit on a tawel',
             'I wan to go to te beachh to sit on a tawel',
             'I liek to sing udner the rainn',
             'I like to sunbathe at the bech',
             'I like to snbathe at the bech',
             'When we go on bacation we liek to sail in the sey',
             'At the beach it is important to have an umbral',
             'Sail in the sey',
             'Swim in the sey',
             'I want to eta at that restaurant',
             'I want to eta at that restrautant',
             'I liek caek for dessert'

]

if "-i" in sys.argv:
    while True:
        print " "
        sentence = raw_input('Write a sentence: ')
        print "Spellsense: " + __init__.check(sentence)
        print "Enchant: " + __init__.dumbcheck(sentence)
        print " "
else:
    for sentence in sentences:
        print "*"+sentence
        print "Spellsense: " + __init__.check(sentence)
        print "Enchant: " + __init__.dumbcheck(sentence)
        print " "
