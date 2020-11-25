
def hmwrk():
    import time
    alex_sentence = (input("Good Morning Mr Marzan. Please enter a sentence: "))
    time.sleep(1.5)
    print ("Thank you Mr Marzan.\nThe number of characters in your sentence is:", len(alex_sentence))
    time.sleep(2)
    print ("What's more, this is your sentence in reverse: " + alex_sentence[::-1])
    time.sleep(3.2)
    sp = 0
    for space in alex_sentence:
        
        if space == " ":
            sp += 1
    print ("Also, you seem to have", sp, "spaces in your sentence.\nImpressive stats! Have a good day Alex!")
   


hmwrk()






#or chara in range ():







