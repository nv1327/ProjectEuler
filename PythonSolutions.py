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




  
#All Problems
#Multiplesof3and5()     #Problem 1
#EvenFibonacci()        #Problem 2
#LargestPrimeFactor()   #Problem 3
#LargestPalindrome()    #Problem 4
#SmallestMultiple()     #Problem 5
#SumSquareDifference()  #Problem 6
#TenThousandthPrime()   #Problem 7
LargestSeriesProduct() #Problem 8
