from dogsheet import *
from time import sleep
# THIS SOFTWARE IS AT 1.0 VERSION!

# Labrador Retriever
labradorRetriever = Dogs()
labradorRetriever.fur = 2
labradorRetriever.ears = 2
labradorRetriever.height = 2
labradorRetriever.length = 2
labradorRetriever.uniCharacteristic = "Looks like the dog from Marley & Me"
labradorRetrieverCont = 0

# German Shepherd Dog
gShepherdDog = Dogs()
gShepherdDog.fur = 2
gShepherdDog.ears = 1
gShepherdDog.height = 2
gShepherdDog.length = 2
gShepherdDog.uniCharacteristic = "Most common police dogs"
gShepherdDogCont = 0

# Golden Retriever
goldenRetriever = Dogs()
goldenRetriever.fur = 3
goldenRetriever.ears = 2
goldenRetriever.height = 2
goldenRetriever.length = 2
goldenRetriever.uniCharacteristic = "Dog from Air Bud (1997)"
goldenRetriever.uniCharacteristic2 = "Usually seen as item catchers and sportists"
goldenRetrieverCont = 0

# French Bulldog
frenchBulldog = Dogs()
frenchBulldog.fur = 1
frenchBulldog.ears = 1
frenchBulldog.height = 1
frenchBulldog.length = 1
frenchBulldog.uniCharacteristic = "Darker and shorter snout"
frenchBulldog.uniCharacteristic2 = "French"
frenchBulldogCont = 0

# Bulldog
bulldog = Dogs()
bulldog.fur = 1
bulldog.ears = 2
bulldog.height = 1
bulldog.length = 1
bulldog.uniCharacteristic = "Darker and shorter snout"
bulldog.uniCharacteristic2 = "Presidents like them"
bulldogCont = 0

# Poodle 
poodle = Dogs()
poodle.fur = 3
poodle.ears = 2
poodle.height = 2
poodle.length = 2
poodle.uniCharacteristic = "Rounded fur"
poodle.uniCharacteristic2 = "Very calm"
poodleCont = 0

# Beagle
beagle = Dogs()
beagle.fur = 1
beagle.ears = 2
beagle.height = 1
beagle.length = 1
beagle.uniCharacteristic = "White tail tip"
beagle.uniCharacteristic2 = "President Lyndon Johnson had three"
beagleCont = 0

# Rottweilers	
rottweiler = Dogs()
rottweiler.fur = 1
rottweiler.ears = 2
rottweiler.height = 2
rottweiler.length = 2
rottweiler.uniCharacteristic = "Usually their fur is black and brown"
rottweiler.uniCharacteristic2 = "Once a Roman Drover Dog"
rottweilerCont = 0

# German Shorthaired Pointer
gSPointer = Dogs()
gSPointer.fur = 1
gSPointer.ears = 2
gSPointer.height = 2
gSPointer.length = 2
gSPointer.uniCharacteristic = "Very skinny and versatile"
gSPointerCont = 0

# Pembroke Welsh Corgi
pWCorgi = Dogs()
pWCorgi.fur = 2
pWCorgi.ears = 1
pWCorgi.height = 1
pWCorgi.length = 1
pWCorgi.uniCharacteristic = "Queen Elizabeth II was the most notable responsible for his popularity"
pWCorgiCont = 0 

# Dachshunds	
dachshund = Dogs()
dachshund.fur = 1
dachshund.ears = 2
dachshund.height = 1
dachshund.length = 3
dachshund.uniCharacteristic = "Popularly known as the sausage dog"
dachshund.uniCharacteristic2 = "It's the dog from Toy Story movie franchise"
dachshundCont = 0

# Yorkshire Terrier
yorkshireTerrier = Dogs()
yorkshireTerrier.fur = 3
yorkshireTerrier.ears = 1
yorkshireTerrier.height = 1
yorkshireTerrier.length = 1
yorkshireTerrier.uniCharacteristic = "Loves lap"
yorkshireTerrier.uniCharacteristic2 = "They're classified as a toy breed"
yorkshireTerrierCont = 0

# Boxer
boxer = Dogs()
boxer.fur = 1
boxer.ears = 1
boxer.height = 2
boxer.length = 2
boxer.uniCharacteristic = "Skinny but muscular"
boxer.uniCharacteristic2 = "Usually brown on the top and white on the bottom"
boxerCont = 0

# Siberian Husky
siberianHusky = Dogs()
siberianHusky.fur = 2
siberianHusky.ears = 1
siberianHusky.height = 2
siberianHusky.length = 2
siberianHusky.uniCharacteristic = "They're wolfy alike snowy dogs"
siberianHuskyCont = 0

# Saint Bernard
saintBernard = Dogs()
saintBernard.fur = 2
saintBernard.ears = 2
saintBernard.height = 2
saintBernard.length = 2
saintBernard.uniCharacteristic = "It's the dog from Beethoven (1992)"
saintBernardCont = 0

# Pug
pug = Dogs()
pug.fur = 1
pug.ears = 2
pug.height = 1
pug.length = 1
pug.uniCharacteristic = "Their short noses causes breathing issues"
pugCont = 0

# Chihuahua
chihuahua = Dogs()
chihuahua.fur = 1
chihuahua.ears = 1
chihuahua.height = 1
chihuahua.length = 1
chihuahua.uniCharacteristic = "They're angry and aggressive dogs"
chihuahuaCont = 0

# Basset 
basset = Dogs()
basset.fur = 1
basset.ears = 2
basset.height = 1
basset.length = 3
basset.uniCharacteristic = "Tired face, lazy and long ears"
bassetCont = 0

# Attributes function:
def addAttributes():
    dogs.fur = int(input("Your dog fur is [1] Slight, [2] Medium or [3] Volumous? "))
    dogs.ears = int(input("Your dog ears are [1] Pointed and up or [2] Rounded and down? "))
    dogs.height = int(input("Your dog height is [1] Tiny, [2] Medium or [3] Tall? (Tall dogs are very rare, so don't vote three if your dog isn't extremely tall) "))
    dogs.length = int(input("Your dog length is [1] Short, [2] Medium or [3] Long? (Proportionally to the height) "))

addAttributes()

# Fur aggregator:
if dogs.fur == 1:
    frenchBulldogCont +=1
    boxerCont += 1
    dachshundCont += 1
    gSPointerCont += 1
    rottweilerCont += 1
    beagleCont += 1
    poodleCont += 1
    bulldogCont += 1
    pugCont += 1
    chihuahuaCont += 1
    bassetCont += 1
elif dogs.fur == 2:
    labradorRetrieverCont += 1
    gShepherdDogCont += 1
    pWCorgiCont += 1
    siberianHuskyCont += 1
    saintBernardCont += 1
elif dogs.fur == 3:
    yorkshireTerrierCont += 1
    poodleCont += 1
    goldenRetrieverCont += 1

# Ears aggregator
if dogs.ears == 1:
    frenchBulldogCont += 1
    pWCorgiCont += 1
    yorkshireTerrierCont += 1
    boxerCont += 1
    siberianHuskyCont += 1
    gShepherdDogCont += 1
    chihuahuaCont += 1
elif dogs.ears == 2:
    labradorRetrieverCont += 1
    goldenRetrieverCont += 1
    bulldogCont += 1
    poodleCont += 1
    beagleCont += 1
    rottweilerCont += 1
    gSPointerCont += 1
    dachshundCont += 1
    saintBernardCont += 1
    pugCont +=1
    bassetCont += 1 

# Height aggregator
if dogs.height == 1:
    frenchBulldogCont += 1
    bulldogCont += 1
    beagleCont += 1
    yorkshireTerrierCont += 1
    dachshundCont += 1
    pWCorgiCont += 1
    pugCont += 1
    chihuahuaCont += 1
    bassetCont += 1


elif dogs.height == 2:
    labradorRetrieverCont += 1
    gShepherdDogCont += 1
    goldenRetrieverCont += 1
    poodleCont += 1
    rottweilerCont += 1
    gSPointerCont += 1
    boxerCont += 1
    siberianHuskyCont += 1
    saintBernardCont += 1
    

# length aggregator:
if dogs.length == 1:
    frenchBulldogCont += 1
    bulldogCont += 1
    beagleCont += 1
    pWCorgi += 1
    yorkshireTerrierCont += 1
    pugCont += 1
    chihuahuaCont += 1
    
elif dogs.length == 2:
    siberianHuskyCont += 1
    boxerCont += 1
    gSPointerCont += 1
    rottweilerCont += 1
    poodleCont += 1
    goldenRetrieverCont += 1
    gShepherdDogCont += 1
    labradorRetrieverCont += 1
    saintBernardCont += 1

elif dogs.length == 3:
    dachshundCont += 1
    bassetCont += 1

# Characteristics aggregator:
def uniCharacteristicPrint():
    sleep(1)
    print('='*30)
    print(f'1 - {labradorRetriever.uniCharacteristic} \n')
    print(f'2 - {gShepherdDog.uniCharacteristic} \n')
    print(f'3 - {goldenRetriever.uniCharacteristic} \n')
    print(f'4 - {goldenRetriever.uniCharacteristic2} \n')
    print(f'5 - {frenchBulldog.uniCharacteristic} \n')
    print(f'6 - {bulldog.uniCharacteristic} \n')
    print(f'7 - {bulldog.uniCharacteristic2} \n')
    print(f'8 - {poodle.uniCharacteristic} \n')
    print(f'9 - {poodle.uniCharacteristic2} \n')
    print(f'10 - {beagle.uniCharacteristic} \n')
    print(f'11 - {beagle.uniCharacteristic2} \n')
    print(f'12 - {rottweiler.uniCharacteristic} \n')
    print(f'13 - {rottweiler.uniCharacteristic2} \n')
    print(f'14 - {gSPointer.uniCharacteristic} \n')
    print(f'15 - {pWCorgi.uniCharacteristic} \n')
    print(f'16 - {dachshund.uniCharacteristic} \n')
    print(f'17 - {dachshund.uniCharacteristic2} \n')
    print(f'18 - {yorkshireTerrier.uniCharacteristic} \n')
    print(f'19 - {yorkshireTerrier.uniCharacteristic2} \n')
    print(f'20 - {boxer.uniCharacteristic} \n')
    print(f'21 - {boxer.uniCharacteristic2} \n')
    print(f'22 - {siberianHusky.uniCharacteristic} \n')
    print(f'23 - {saintBernard.uniCharacteristic} \n')
    print(f'24 - {pug.uniCharacteristic} \n')
    print(f'25 - {chihuahua.uniCharacteristic} \n')
    print(f'26 - {frenchBulldog.uniCharacteristic2} \n')
    print(f'27 - {basset.uniCharacteristic} ')
    print('='*40)

uniCharacteristicPrint()

sleep(1)
for char in range(1, 3):
    char = int(input("Choose 2 characteristics of your dog: "))
    if char == 1:
        labradorRetrieverCont += 2
    elif char == 2:
        gShepherdDogCont += 1
    elif char == 3:
        goldenRetrieverCont += 2
    elif char == 4:
        goldenRetrieverCont += 1
    elif char == 5 or 26:
        frenchBulldogCont += 1
    elif char == 6 or 7:
        bulldogCont += 1
    elif char == 8 or 9:
        poodleCont += 1
    elif char == 10:
        beagleCont += 1
    elif char == 11:
        beagleCont += 2
    elif char == 12:
        rottweilerCont += 1
    elif char == 13:
        rottweilerCont += 2
    elif char == 14:
        gSPointerCont += 1
    elif char == 15:
        pWCorgiCont += 2
    elif char == 16:
        dachshundCont += 1
    elif char == 17:
        dachshundCont += 2
    elif char == 18 or 19:
        yorkshireTerrierCont += 1
    elif char == 20 or 21:
        boxerCont += 1
    elif char == 22:
        siberianHuskyCont += 2
    elif char == 23:
        saintBernardCont += 2
    elif char == 24:
        pugCont += 1
    elif char == 25:
        chihuahuaCont += 1
    

result = {'Siberian Husky': siberianHuskyCont, 'Boxer': boxerCont, 'Yorkshire Terrier': yorkshireTerrierCont, 'Dachshund': dachshundCont, 
'Pembroke Welsh Corgi': pWCorgiCont, 'German Shorthaired Pointer': gSPointerCont, 'Rottweiler': rottweilerCont, 'Beagle': beagleCont,  'Poodle': poodleCont, 'Bulldog': bulldogCont, 'French Bulldog': frenchBulldogCont, 
'Golden Retriever': goldenRetrieverCont, 'German Shepherd Dog': gShepherdDogCont, 'Labrador Retriever': labradorRetrieverCont, 'Chihuahua': chihuahuaCont, 'St Bernard': saintBernardCont, 'Pug': pugCont, 'Basset': bassetCont}

for k, v in result.items():
    print(f"Dog {k} pointed {v}")

