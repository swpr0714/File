/*  INPUT NAMESPACE BEFORE CODING  */

using System;
using System.Diagnostics;
namespace HW_Random
{
    class Program
    {
        static void Main(String[] args)
        {
            const int time = 1000000;
            Random rand = new Random();             
            int[] remain = new int[10] {0,0,0,0,0,0,0,0,0,0};
            for (int i=0;i<time;i++)
            {
                int rem = rand.Next() % 10;
                remain[rem]++;
            }
            
            for (int i=0;i<remain.Length;i++)
            {
                Console.WriteLine("餘數是{0}的有{1}個數",i,remain[i]);
            }
            Console.WriteLine("");
            Console.WriteLine("每一個*代表5000個數");
            for (int i=0;i<remain.Length;i++)
            {
                int star = remain[i]/5000;
                Console.Write(" {0}.",i);
                for (int t=0;t<star;t++)
                {
                    Console.Write("*");
                }
                Console.WriteLine("");
            }

        }
    }
}