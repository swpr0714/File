/*  INPUT NAMESPACE BEFORE CODING  */

// n=位置且數字正確的數量
// m=數字正確的數量
// Example:
// 謎底4567
// 輸入5566
// 輸出2A4B

using System;
using System.Diagnostics;
namespace nAmB
{
    class Program
    {
        static void Main(String[] args)
        {
            int n=0;
            int m=0;
            int Input=0;
            int[] Guess = new int[4];
            int[] Ans = new int[4];
            
            Random rand = new Random();
            for (int i=0;i<4;i++)
            {
                Ans[i]=rand.Next(0,9);
            } 
            
            while (n!=4)
            {
                n=0;
                m=0;
                Console.WriteLine("請輸入數字");
                Input=Convert.ToInt32(Console.ReadLine());
                //int轉array
                
                int k=3;
                while(Input>0)
                {
                    Guess[k]=Input%10;
                    k--;
                    Input/=10;
                }
                //檢驗n
                for (int i=0;i<4;i++)
                {
                    if (Ans[i]==Guess[i]){n++;}
                }
                //檢驗m
                for (int i=0;i<4;i++)
                {
                    for (int j=0;j<4;j++)
                    {
                        if (Ans[i]==Guess[j]){m++;}
                    }
                }
                Console.WriteLine("{0}n{1}m",n,m);
                // Console.WriteLine("你猜的是");
                // for (int i=0;i<4;i++)
                // {
                //     Console.Write(Guess[i]);
                //     Console.Write(" ");
                // }
                // Console.WriteLine("\n解答為:");
                // for (int i=0;i<4;i++)
                // {
                //     Console.Write(Ans[i]);
                //     Console.Write(" ");
                // }
                // if(n<4){Console.WriteLine("\n呵呵廢物");}
            }
            Console.WriteLine("終於答對了 廢物");
        }
    }
}