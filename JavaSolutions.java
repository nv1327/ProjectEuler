import java.util.*;
import java.util.stream.*;
import java.math.BigInteger;
import java.io.*;

public class ProjectEuler
{
    public static void main(String[] args)
    {
        System.out.println(isPalindrome(901109));
        //multiple35();
    }

    //Problem 1
    public static void multiple35()
    {
        int total = 0;
        for (int i = 0; i < 1000; i++)
        {
            if (i % 3 == 0 || i % 5 == 0)
            {
                total += i;
            }
            else
            {
                //
            }
        }
        System.out.println(total);
    }

    //Problem 2
    public static void EvenFibonacci()
    {
        int prevFirst=0;
        int prevSecond=1;
        int bound=4_000_000;
        int evenSum=0;

        boolean exceed=false; //when fib numbers > bound
        while(!exceed){
            int newFib=prevFirst + prevSecond;
            prevFirst = prevSecond;
            prevSecond = newFib;

            if(newFib > bound){
                exceed=true;
                break;
            }

            if(newFib % 2 == 0){
                evenSum += newFib;
            }
        }

        System.out.println(evenSum);

    }

    //Problem 3
    public static void LargestPrimeFactor()
    {
        BigInteger zero = new BigInteger("0");
        BigInteger one = new BigInteger("1");
        BigInteger five = new BigInteger("5");
        BigInteger factor = new BigInteger("0");
        BigInteger result = new BigInteger("0");
        BigInteger three = new BigInteger("3");
        boolean prime = false;

        BigInteger mainNumber = new BigInteger("600851475143");
        BigInteger two = new BigInteger("2");

        for (BigInteger a = three; a.compareTo(mainNumber) <= 0; a = a.add(two))
        {
            //System.out.println(a);
            factor = mainNumber.mod(a);
            //System.out.println(factor);
            if (factor.compareTo(zero) == 0)
            {
                result = mainNumber.divide(a);
                System.out.println(result);
                prime = result.isProbablePrime(1);
            }
            if (prime == true)
            {
                System.out.println(result + " is the GPF");
                break;
            }
        }

    }

    //Problem 4
    public static void LargestPalindrome()
    {
        int reversedInteger = 0;
        int remainder = 0;
        int originalInteger = 0;

        int maxPalindrome=0;
        int current=0;
        for (int i = 999; i > 1; i--)
        {
            for (int j = 999; j > 1; j--)
            {
                int num = i * j;
                //System.out.println(num);
                //originalInteger = num; //store value of num in originalInteger
                if(isPalindrome(num))
                {
                    current=num;
                    if(current>maxPalindrome)
                    {
                        maxPalindrome=current;
                    }
                }
            }
        }
        
        System.out.println(maxPalindrome);
    }

    public static boolean isPalindrome(int num)
    {
        int originalInteger=num;
        int reversedInteger=0;
        while (num != 0)
        {
            int remainder = num % 10;
            reversedInteger = reversedInteger * 10 + remainder;
            num /= 10;
        }
        if (originalInteger == reversedInteger)
        {
            //System.out.println(originalInteger + " is a palindrome");
            return true;
        }
        return false;
    }
    
    //Problem 5
    public static void smallestMultiple()
    {
        //start at 2520 bc we know that's the smallest for 1-10
        //check every 20 numbers bc it must be divisible by 20
        int counter = 0;
        for (int i = 2520; i < 1000000000; i += 20)
        {
            //System.out.println(i);
            for (int j = 1; j < 21; j++)
            {
                if (i % j == 0)
                {
                    counter += 1;
                }
                if (counter == 20)
                {
                    System.out.println(i + " is the SM");
                    break;
                }
            }
            counter = 0;
        }
    }
    
    //Problem 6
    public static void sumSquareDiff()
    {
        int sumOfSquares = 0;
        for (int i = 0; i < 101; i++)
        {
            int x = i;
            x *= x;
            //System.out.println(x);
            sumOfSquares += x;
        }
        //System.out.println(sumOfSquares);
        
        int squareOfSum = 0;
        for (int j = 0; j < 101; j++)
        {
            squareOfSum += j;
            //System.out.println(squareOfSum);
        }
        squareOfSum *= squareOfSum;
        
        int result = squareOfSum - sumOfSquares; 
        System.out.println(result);
    }

    //Problem 7
    public static void thousandFirstPrime()
    {
        BigInteger zero = new BigInteger("0");
        BigInteger one = new BigInteger("1");
        BigInteger two = new BigInteger("2");
        BigInteger three = new BigInteger("3");
        BigInteger five = new BigInteger("5");
        BigInteger factor = new BigInteger("0");
        BigInteger result = new BigInteger("0");
        
        boolean prime = false;
        
        int counter = 1;

        BigInteger mainNumber = new BigInteger("100000000");

        for (BigInteger a = three; a.compareTo(mainNumber) == -1; a = a.add(two))
        {
            prime = a.isProbablePrime(1);
            if (prime == true)
            {
                counter += 1;
                //System.out.println("Prime #" + counter + " is " + a);
            }
            if (counter == 10001)
            {
                System.out.println(a + "is 10001st prime");
                break;
            }
        }
    }
    
    
}
