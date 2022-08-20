/*  INPUT NAMESPACE BEFORE CODING  */

using System;
using System.Diagnostics;
namespace  ArrayFuncTest
{
    class Program
    {
        static void Main(String[] args)
        {
            int[] array = new int[5]{10,22,53,64,25};
            for (int i=0;i<array.Length;i++)
            {
                Console.Write(array[i]);
            }
            Console.Write("\nReverse\n");
            Array.Reverse(array);
            for (int i=0;i<array.Length;i++)
            {
                Console.Write(array[i]);
            }

            Array.Sort(array);
            Console.Write("\nSort\n");
            for (int i=0;i<array.Length;i++)
            {
                Console.Write(array[i]);
            }
            Array.Clear(array);
            Console.Write("\nClear\n");
            for (int i=0;i<array.Length;i++)
            {
                Console.Write(array[i]);
            }

        }
    }
}