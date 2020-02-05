import math

#Problem 1
def Multiplesof3and5():
  sum = 0

  for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  print (sum)

#Problem 2
def EvenFibonacci():
  sum = 0
  first = 1
  second = 2
  counter = 2 #I did this because my code skips over the first even number in the sequence, which is 2. In a normal scenario, counter = 0

  while (second < 4000000):
    sum = first + second
    first = second
    second = sum
    if second % 2 == 0:
      counter += second
    
  print(counter)

#Problem 3
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i==0:
            return False
    return True



def LargestPrimeFactor():
  number = 600851475143
  prime = False

  for i in range(3, number, 2): #loops down odd numbers bc no even number is prime
    if number % i == 0:  #checks if number is a factor
      result = number / i
      print (result)
      prime = isPrime(result)
    if prime == True:
      #print (str(result) + " is the GPF")
      break

#Problem 4
def reverse(num):
  result = int(str(num)[::-1])
  return result

def isPalindrome(originalInteger):

  reversedInteger = reverse(originalInteger)

  if originalInteger == reversedInteger:
    #To use this, comment out return True and return False
    #and leave print(1) and print(0) to test
    return True
    #print(1)
  return False
  #print(0)


def LargestPalindrome():
  product = 0
  currentlargest = 0
  for i in range(1000, 0, -1):
    for x in range(1000, 0, -1):
      product = i * x
      #print(product)
      result = isPalindrome(product)
      if result == True:
        #print (product)
        if product > currentlargest:
          currentlargest = product
          print (currentlargest)
          #the last one it prints should be the result

#Problem 5
def SmallestMultiple():
  for i in range(100000000, 999999999999, 20): #it must be divisible by 20 so we can jump by 20 to guarantee that it'll be divisible by the greatest one
    counter = 0
    for x in range(3, 20):  #since we're increasing by 20 we know all of them are divisible by 1, 2, and 20, so we can start loop at 3 and go to 19 - also since it ends in 0 we know it's divisible by 2 so we can jump by 2 in the loop
      if i % x != 0:
        break
      if i % x == 0:
        counter += 1
      if counter == 17:
        print (i)
        break
#problem: I know I can make it faster by cutting the inner loop
#by jumping by 2, but it gives weird results
#also the program doesn't end after print (i) so you have to stop it manually bc it only breaks the inner for loop

#Problem 6
def SumSquareDifference():
  finalResult = 0
  
  sumOfSquares = 0
  y = 0
  for x in range(101):
    y = x
    y = y * y
    sumOfSquares += y

  squareOfSum = 0
  for i in range(101):
    squareOfSum += i
  squareOfSum = squareOfSum * squareOfSum

  finalResult = squareOfSum - sumOfSquares
  print (finalResult)


#Problem 7
def TenThousandthPrime():
  counter = 0
  for i in range(2, 10000000):
    prime = isPrime(i)
    if prime == True:
      counter += 1
      prime = False
    if counter == 10001:
      print (i)
      break


#Problem 8
def LargestSeriesProduct():
  number1 = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482)

  number2 = str(839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
  #This is a thousand digit number split in 2 parts(almost evenly)
  #So instead of adding them as integer, I converted to strings and concatenated them into one number, which is number 3
  number3 = number1 + number2
  
  numberlist = []

  for char in number3:
    char = int(char)
    numberlist.append(char)

  currentmax = 0
  for i in range(0, len(numberlist) - 12):
    product = numberlist[i] * numberlist[i+1] * numberlist[i+2] * numberlist[i+3] * numberlist[i+4] * numberlist[i+5] * numberlist[i+6] * numberlist[i+7] * numberlist[i+8] * numberlist[i+9] * numberlist[i+10] * numberlist[i+11] * numberlist[i+12]
    #I made it 12 because it messes up once it gets to the end of the list, so i cut it off once numberlist[i+12] is the last element in the list, which is the last digit in the number
    if product > currentmax:
      currentmax = product
  print (currentmax)


#Problem 9
def PythTriplet():
  for x in range(1, 550):
    for y in range(1, 550):
      num1 = x * x
      num2 = y * y
      num3 = math.sqrt(num1 + num2) #needs to be a float or Python begins to round numbers which leads to incorrect results
      if x + y + num3 == 1000:
        print (x, y, num3)
        product = x * y * num3
        print (product)


#Problem 10
def PrimeSum():
  sum = 2 #I'm doing this bc I want to skip even numbers so I skipped over 2 in the for loop, so this should be 0 to start but I'm including 2 in the sum
  for i in range(3, 2000000, 2):
    prime = isPrime(i)
    if prime == True:
      sum += i
  print (sum)


#Problem 11
def LargestGridProduct():
  number = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

  numberlist = []
  number = number.replace(" ", "")

  for i in range(0, len(number)-1, 2):
    x = number[i]
    y = number[i+1]
    char = x + y
    numberlist.append(char)

  grid = [ [ 0 for j in range(20) ] for k in range(20) ] 
  
  numbercounter = 0
  for d in range(20):
    for e in range(20):
      grid[d][e] = int(numberlist[numbercounter])
      numbercounter += 1

  #Now just use coordinates to reference individual points and check them

  currentmax = 0
  temp = 0

  #this is just for upper left corner, I need to put these all in a for loop that adjusts the [0] up to a 17 possible
  for a in range(20):
    for r in range(17):  #horizontal right
        temp = grid[a][r] * grid[a][r+1] * grid[a][r+2] * grid[a][r+3]
        if temp > currentmax:
          currentmax = temp
    for v in range(17):  #vertical down
      temp = grid[v][a] * grid[v+1][a] * grid[v+2][a] * grid[v+3][a]
      if temp > currentmax:
          currentmax = temp
    """
    for f in range(3, 20, -1): #vertical up
      temp = grid[f-3][a] * grid[f-2][a] * grid[f-1][a] * grid[f][a]
      print(temp)
      if temp > currentmax:
          currentmax = temp
    """
  for w in range(17): #diagonal down right all the way
    temp = grid[w][w] * grid[w+1][w+1] * grid[w+2][w+2] * grid[w+3][w+3]
    if temp > currentmax:
      currentmax = temp

  for b in range(17): #diagonal down right? i think this works for all other diagonal down rights
    for c in range(16):
      temp = grid[b][c+1] * grid[b+1][c+2] * grid[b+2][c+3] * grid[b+3][c+4]
      if temp > currentmax:
        currentmax = temp

  #So far I only cover 3 directions: horizontal right, vertical down, diagonal right

  #grid[vertical][horizontal]

  
  #print(grid)
  #print(currentmax)

#Problem 12
def TriangularNumber():
  triangle = 0
  for i in range(1, 100000000000):
    triangle += i
    counter = 0
    #print(triangle)
    for x in range(1, int(triangle ** 0.5) + 1):
      if triangle % x == 0:
        counter += 1
      if counter >= 250:
        print(triangle) #the first one it prints is correct


#Problem 13
def LargeSum():
  num1 = "37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951"
  
  num2 = "62176457141856560629502157223196586755079324193331649063524627419049291014324458138226633479447581789257586771833721766196375159057923972824559883840758203565325359399008402633568948830189458628227828801811993848262820142781941399405675871511700943903539866437282711265382998724078447305319010429358686515506006295864861532075273371959191420517255829716938887077154664991155934876035329217149700569385437007057682668462462149565007647178729443837760453282654108756828443191190634694037855217779295145"

  num3 = "36123272525000296071075082563815656710885258350721458765761724109764473391106072182652368772236360451742370690585186066044820762120981328786073396941281142660418086830619328460811191061556940512689692519343254517283886419180470492932150586425630494836246722164843507620172791803994469300473295634069115732444386908125794514089057706229429197107928209550376875256787730918625407449698445083303936821261833638482533015468619612434876768129753437594651580386287592878490201521685554828717201219257766954"

  num4 = "78182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275"

  num5 = "88902802571733229619176668713819931811048770190271252676802760780030136786809925254634010616328665263627021854049770558562994658063623799314074625596224074486908231174977792365466257246923322810917141914302881971032885978066697608929386382850253334033441306557801612781592181500556186883646842009047023053081172816430487623791969842487255036638784583114876969321549028104240201383351244621814417734706378329949063625966649858761822122522551248676453367720186971698544312419572409913959008952310058822"

  num6 = "95548255300263520781532296796249481641953868218774760853271322857231104248034561248676970645079952363777424253541129168427686553892620502491032657296723701913275725675285653248258265463092207058596522297988602722583319131263751473419948895347657455011849570145487928898485682772607771372140379887971538298203783031473527721580348144513491373226651381348295438291999181802789165224310273922511228695394095795306640523263253804410005965493915987959363529746152185502371307642255121183693803580388584903"

  num7 = "41698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886"

  num8 = "75506164965184775180738168837861091527357929701337621778427521926234019423996391680449839931733127313292418570714734956691667468763466091503591467750499518671430235219628894890102423325116913619626622732674608005915474718307983928685352069469445407247684182252467441716151403642798227334805555621481897142617910342598647204516893989422179826088076852877836461827993463137677543078093633330189826420901084880252167467088321512018588354322381287695278671329612474782464538636993009049310363619763878039"

  num9 = "62184073572399794223406235393808339651327408011116666278919814880877979418768761442300309844908514116066182629368283676474477923918033511098906979071485786944089552990653640447425576083659976645795096660243964099053896071201982199760475994901972302976491398268003297315603712004137790378556608508925216730939319872750275468906903707539413042652315011948093772450487951509541009216458637547105984367917863916702118749243199570064191796977759902830069915368713711936614952811305876380278410754449733078"

  num10 = "40789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690"

  number = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10

  #print(number)

  numberlist = []

  sequence = 0
  counter = 0
  for j in range(len(number)):
    e = int(number[j])
    sequence += (e * (10 ** (49 - counter)))
    counter += 1
    if counter % 50 == 0:
      numberlist.append(sequence)
      sequence = 0
      counter = 0

  sum = 0
  for i in range(len(numberlist)):
    sum += numberlist[i]

  sum = str(sum)
  for k in range(10):
    print(sum[k])


#Problem 14
def CollatzSeq():
  
  currentmax = 0
  maxstarting = 0

  for i in range(2, 1000000):
    starting = i
    num = starting

    counter = 0

    check = True
    while check == True:
      if num == 1:
        check = False
      elif num % 2 == 0:
        num = num / 2
      else:
        num = 3 * num + 1
      counter += 1

    if counter > currentmax: #if this sequence is the longest
      currentmax = counter #should see which starting has the longest one
      maxstarting = starting
    if starting % 10000 == 0:
      print(starting, currentmax, maxstarting) #prints starting term and current maximum length of sequence and the last starting number that had that maximum length sequence
  print(maxstarting) #this should be the number that has the longest sequence

#Problem 15
def PicksTheorem(gridside):
  #gridside = 2  #set this to 2 for a 2 x 2 grid
  area = gridside * gridside
  externalpoints = gridside * 4
  halfexternalpoints = externalpoints / 2
  interiorpoints = area - halfexternalpoints + 1
  
  totalpoints = externalpoints + interiorpoints
  print(totalpoints)
  #this math also can work for any shape, not just lattices, but then the code would need to be adjusted


def LatticePaths():

  gridsize = 2  #this is for a 2x2 lattice

  grid = [ [ 0 for j in range(gridsize+1) ] for k in range(gridsize+1) ] 
  #all possible points are labeled with "0" - this is for a 2x2 grid - this works bc there are 9 points in a 2x2 grid
  #so with my 20x20 lattice i would just make a 21x21 2D array
  #go all the way down and change 0 to 1

  #Combinations
  counter = 0
  """
  #makes a path all the way down and right for any size grid
  for i in range(gridsize + 1):
    grid[i][0] = 1
    grid[gridsize][i] = 1
  print(grid)
  counter += 1
  
  print(" ")
  grid = [ [ 0 for j in range(gridsize+1) ] for k in range(gridsize+1) ] #this just resets it to all 0, I could change it later
  
  #makes a path all the way right and down
  for j in range(gridsize + 1):
    grid[0][j] = 1
    grid[j][gridsize] = 1
  print(grid)
  counter += 1
  """
  #Now i need a function that does all possible combinations of down and right, and uses range to detect that
  for e in range(gridsize, 0, -1):
    for d in range(gridsize, 0, -1):
      grid[0][0] = 1
      for w in range(gridsize+1):
        grid[0][w] = 1
        print (grid)
  #if [d-1][e] or [e-1][d] != 1, then don't print 1 because I can only make one if 
      
      
  

  print(" ")
  print("# of paths is: ", counter)


#Problem 16
def PowerDigitSum():
  power = 1000
  base = 2
  sum = 0
  result = str(base ** power)
  for i in result:
    character = int(i)
    sum += character
  print(sum)


#Problem 17
def NumberLetterCounts():
  #Number of letters in each word
  result = ""
  sum = 0
  
  oneslist = [0, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  
  tenslist = [0, "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

  teens = [0, "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

  one = 1
  two = 2
  three = 3
  four = 4
  five = 5

  onesdigit = 0
  tensdigit = 0
  hundredsdigit = 0

  for i in range(1,1001):
    if i < 10:
      result = oneslist[i]
    elif i % 10 == 0 and i < 100:
      tensdigit = int((i % 100) / 10)
      result = tenslist[tensdigit]
    elif 10 < i < 20:
      onesdigit = i % 10
      result = teens[onesdigit]
    elif 20 < i < 100:
      tensdigit = int((i % 100) / 10)
      onesdigit = i % 10
      result = tenslist[tensdigit] + oneslist[onesdigit]
    elif 99 < i < 1000:
      hundredsdigit = int((i % 1000) / 100)
      tensdigit = int((i % 100) / 10)
      onesdigit = i % 10
      if onesdigit == 0 and tensdigit == 0:
        result = str(oneslist[hundredsdigit]) + "hundred"
      elif tensdigit == 0:
        result = str(oneslist[hundredsdigit]) + "hundred" + "and" + str(oneslist[onesdigit])
      elif tensdigit == 1 and onesdigit != 0:
        result = str(oneslist[hundredsdigit]) + "hundred" + "and" + str(teens[onesdigit])
      elif tensdigit == 1 and onesdigit == 0:
        result = str(oneslist[hundredsdigit]) + "hundred" + "and" + str(tenslist[tensdigit])
      elif onesdigit == 0:
        result = str(oneslist[hundredsdigit]) + "hundred" + "and" + str(tenslist[tensdigit])
      else:
        result = str(oneslist[hundredsdigit]) + "hundred" + "and" + str(tenslist[tensdigit]) + str(oneslist[onesdigit])
    elif i == 1000:
      result = "onethousand"
    sum += len(result)
  print(sum)
      

#Problem 18
def MaxPathSum1():
  sum = 0
  rows = 4

  currentnum = ""
  numbers = "3 7 4 2 4 6 8 5 9 3 " #detect, if space, then take that number and insert it into the array
  #important: the last number must have a space after it or it will be left out
  numberlist = []
  numbertracker = []

  for e in numbers:
    if e == " ":
      e = ""
      numberlist.append(currentnum)
      currentnum = ""
    currentnum += e

  grid = [ [ 0 for j in range(rows) ] for k in range(rows)]

  w = 0
  counter = 0
  for i in range(rows):
    grid[i][w] = 1
    w += 1
    for a in range(w):
      grid[i][a] = int(numberlist[counter])
      counter += 1
  print(grid)

  sum = 0
  y = 0
  #start at grid[0][0]
  #can only check grid[1][0] and [1][1]
  #each block can only check [i+1][j] and [i+1][j+1] from itself
  for x in range(rows):
    sum += grid[x][y]
    #here, it can only check y = y or y = y + 1
    

  #should try all possible and then print the numbers that it used

  #print(sum + grid[0][0])


  #(2^15) / 2 = 16384 possible routes
  #15 rows in the triangle
  #i could make a 2D array where each iteration increases array size by 1 - so top array has size 1, next array has size 2, etc. then I can reference where the selected term is in the array (by using number[i]) and then comparing it to the next array and being like ok, if I selected number[3], then I can only select number[3] or number[4] in the next array to move to

  #I can use lower triangular matrix for this

#Problem 19
def CountingSundays():
  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  dayspermonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  #every 4 years, dayspermonth[1] += 1 because of leap year

  daysofweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  daycounter = 2
  yearcounter = 1900
  daytotal = 0
  sundaycounter = 0

  #Jan 1, 1900 is a Monday, but Jan 1, 1901 isn't!!! Jan 1, 1901 is a Wednesday. That's why daycounter = 2
  
  for j in range(yearcounter, 2001):  #set max to 2001 if you want to check up to the year 2000
    if j % 4 == 0:   #we already know that 2000 is divisible by 400 so I'm not going to make another function to check for leap years
      dayspermonth[1] = 29
    for i in range(len(months)):
      print(months[i], dayspermonth[i], yearcounter)
      for y in range(1, dayspermonth[i] + 1):
        print(daysofweek[daycounter], y)
        if daysofweek[daycounter] == "Sunday" and y == 1:
          sundaycounter += 1
          print(sundaycounter)
        daycounter += 1
        daytotal += 1
        if daycounter == len(daysofweek):
          daycounter = 0

    dayspermonth[1] = 28
    yearcounter += 1

  print(sundaycounter)

  #Python has a function to get date, but this is my manual version for it. Also I didn't realize there was a DateTime()

  
#Problem 20
def FactorialDigitSum():
  product = 1
  n = 100   #so if n = 3, then it will solve for 3!, which is 6
  for i in range(1, n + 1):
    product *= i
  
  sum = 0
  temp = ""
  product = str(product)
  for j in range(len(product)):
    temp = int(product[j])
    sum += temp
  print(sum)
  



#All Problems
#Multiplesof3and5()     #Problem 1
#EvenFibonacci()        #Problem 2
#LargestPrimeFactor()   #Problem 3
#LargestPalindrome()    #Problem 4
#SmallestMultiple()     #Problem 5
#SumSquareDifference()  #Problem 6
#TenThousandthPrime()   #Problem 7
#LargestSeriesProduct() #Problem 8
#PythTriplet()          #Problem 9
#PrimeSum()             #Problem 10
#LargestGridProduct()   #Problem 11 - NOT COMPLETE
#TriangularNumber()     #Problem 12
#LargeSum()             #Problem 13
#CollatzSeq()           #Problem 14
#LatticePaths()         #Problem 15 - NOT COMPLETE
#PowerDigitSum()        #Problem 16
#NumberLetterCounts()   #Problem 17
#MaxPathSum1()          #Problem 18 - NOT COMPLETE
#CountingSundays()      #Problem 19
FactorialDigitSum()    #Problem 20
