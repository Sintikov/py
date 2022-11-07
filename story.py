import random
from time import sleep

print(" Which category stories would you like to read? ")
print(" 1 - Fantasy , 2 - Horror, 3 - Marvel Comics " )
one = input()

print("Let's choose main characters:")
if one == '1':
    mainChar = input("Cat name:")
    rivalName = input("Rival's name:")
    activity = input("Daily activity:")
    posAdj =input("Positive adjective (e.g. funny,happy) : ")
    negAdj = input("Negative adjective (e.g. Careless,Dishonest) : ")

    word1 = ['words', 'paintings', 'comments']
    word2 = ['penguins', 'programmer jokes', 'dogs', 'another amazing humans']
    word3 = ['New York', 'Texas', 'Astana', "Mars"]
    word4 = ['liked', 'disliked', 'reported', 'deleted']

    Sentance = [ " My cat," , 'mainChar', " is the best poker partner I've ever had. "
                "Hands down—no pun intended."
                "Don't let those old Coolidge" ,'word1', "fool you;", 'word2', "really don't know what the hell they're doing once you sit them on that rickety ladder back chair, and their paws just aren't made for holding the cards steady. "
                "Trust me: If you want a reliable means of collusion in a game of", 'word3' ,"hold 'em, British Shorthairs are the way to go."
                "Of course, it also helps that", 'mainChar' , " can talk now."
                 "Last month my boyfriend" , 'rivalName', "came into the living room while I was", 'activity',". He didn't sit, which was the first red flag. "
                    "The second came in the hushed form of those infamous four words: " , 'posAdj',',', 'negAdj',',','word4',',','bottle',"."
                 "I said: 'What is that mean?' He said: ...."]

    for item in Sentance:
        if item == "activity":
            Sentance[Sentance.index(item)] = activity
        elif item == "mainChar":
            Sentance[Sentance.index(item)] = mainChar
        elif item == "rivalName":
            Sentance[Sentance.index(item)] = rivalName
        elif item == "posAdj":
            Sentance[Sentance.index(item)] = posAdj
        elif item == "negAdj":
            Sentance[Sentance.index(item)] = negAdj
        elif item == "word1":
            Sentance[Sentance.index(item)] = random.choice(word1)
        elif item == "word2":
            Sentance[Sentance.index(item)] = random.choice(word2)
        elif item == "word3":
            Sentance[Sentance.index(item)] = random.choice(word3)
        elif item == "word4":
            Sentance[Sentance.index(item)] = random.choice(word4)
        else:
            continue
    story = " ".join(item for item in Sentance)
    print(story)

elif one == '2':
    mainChar = input("Story Teller:")
    rivalName = input("Any animal: ")
    activity = input("Creepy activity:")
    posAdj =input("Positive adjective (e.g. funny,happy) : ")
    negAdj = input("Negative adjective (e.g. Careless,Dishonest) : ")

    word1 = ['basement', 'room', 'bathroom']
    word2 = ['yelled', 'kicks', 'punch']
    word3 = ['feet', 'hand', 'leg', "ear"]
    word4 = ['head', 'knife', 'blood oxygen', 'virus']

    Sentance = ['mainChar', 'told me never to go in the ','word1', ', but I wanted to see what was making that', 'activity','. It kind of sounded like a ','rivalName',', and I wanted to see the', 'rivalName',', so I opened the  door and tiptoed down a bit. I didn’t see a', 'rivalName', 'and then','mainChar' ,'yanked me out of the ','word1',' and ','word2',' at me. ','mainChar',' had never yelled at me before, and it made me ', 'negAdj' ,' and I cried. Then ' , 'mainChar' ,' told me never to go into the ','word1',' again, and she gave me a ','posAdj','. That made me feel better, so I didn’t ask her why the boy in the ','word1',' was making ','activity',' like a ','rivalName',', or why he had no ','word3',' or ','word4','.']

    for item in Sentance:
        if item == "activity":
            Sentance[Sentance.index(item)] = activity
        elif item == "mainChar":
            Sentance[Sentance.index(item)] = mainChar
        elif item == "rivalName":
            Sentance[Sentance.index(item)] = rivalName
        elif item == "posAdj":
            Sentance[Sentance.index(item)] = posAdj
        elif item == "negAdj":
            Sentance[Sentance.index(item)] = negAdj
        elif item == "word1":
            Sentance[Sentance.index(item)] = random.choice(word1)
        elif item == "word2":
            Sentance[Sentance.index(item)] = random.choice(word2)
        elif item == "word3":
            Sentance[Sentance.index(item)] = random.choice(word3)
        elif item == "word4":
            Sentance[Sentance.index(item)] = random.choice(word4)
        else:
            continue
    story = " ".join(item for item in Sentance)
    print(story)
elif one == '3':
    mainChar = input("Hero name:")
    rivalName = input("Villian: ")
    activity = input("Superpowers:")
    posAdj =input("How he became a superhero? ")
    negAdj = input("Tell villian background: ")

    word1 = ['one day', '6 a.m', 'street']
    word2 = ['Whats that?', 'WTF?', 'Hell no?']
    word3 = ['beat each others', 'dancing', 'playing chess', "eat"]
    word4 = ['home to watch movie', 'toilet', 'GYM, and started to training']

    Sentance = [ 'Once upon a time was a','mainChar','. He has a very greatfull power like a ', 'activity','.',
                 'At','word1','he saw something above him. And he said:', 'word2', 'It turned out it was', 'rivalName', '. And he started to tell him:', 'negAdj' , '. This time he started to tell about yourself:', 'posAdj', 'So then they started to', 'word3', 'and go to the', 'word4', '.' ]

    for item in Sentance:
        if item == "activity":
            Sentance[Sentance.index(item)] = activity
        elif item == "mainChar":
            Sentance[Sentance.index(item)] = mainChar
        elif item == "rivalName":
            Sentance[Sentance.index(item)] = rivalName
        elif item == "posAdj":
            Sentance[Sentance.index(item)] = posAdj
        elif item == "negAdj":
            Sentance[Sentance.index(item)] = negAdj
        elif item == "word1":
            Sentance[Sentance.index(item)] = random.choice(word1)
        elif item == "word2":
            Sentance[Sentance.index(item)] = random.choice(word2)
        elif item == "word3":
            Sentance[Sentance.index(item)] = random.choice(word3)
        elif item == "word4":
            Sentance[Sentance.index(item)] = random.choice(word4)
        else:
            continue
    story = " ".join(item for item in Sentance)
    print(story)

else:
    "This type of story not added yet."

print('Good story telling Program :3')









