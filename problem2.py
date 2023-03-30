#If T-Rex is angry, hungry, and bored he will eat the Triceratops.
#Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
#Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
#Otherwise if T-Rex is tired, he goes to sleep.
#Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
#Otherwise if T-Rex is angry or bored, he roars.
#Otherwise T-Rex gives a toothy smile.

angry = True
bored = True
hungry = False
tired = False
if angry:
    if hungry and bored:
        print("Triceratops will be his food!")
    elif bored:
        print("T-Rex rage war againts Velociraptor!")
    elif hungry:
        print("T-Rex: rawwwwwaawww!")
    else:
        print("T-Rex gives everyone a toothy smile.")
elif tired:
    if hungry:
        print("Iguanadon will be his food!")
    else:
        print("T-Rex's bed time")
elif hungry and bored: #other conditions
    print("Stegasaurus will be his food!")
elif angry or bored:
    print("T-Rex: rawwwwwaawww!")
else:
    print("T-Rex gives everyone a toothy smile.")
