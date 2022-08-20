/*  INPUT NAMESPACE BEFORE CODING  */

using System;
using System.Diagnostics;
namespace Enum
{
    enum SeasonType : byte
    {
        Spring = 1,
        Summer = 2,
        Autumn = 3,
        Winter = 4,
        Null = 5
    }
    
    class Program
    {
        static void Main(String[] args)
        {
            Console.Write("\n請輸入月份:\n");
            int month = Convert.ToInt32(Console.ReadLine());
            SeasonType Season;
            Season = SeasonType.Null;
            if(month>=1&&month<=3){Season=SeasonType.Spring;}
            else if(month>=4&&month<=6){Season=SeasonType.Summer;}
            else if(month>=7&&month<=9){Season=SeasonType.Autumn;}
            else if(month>=10&&month<=12){Season=SeasonType.Winter;}
            else {}
            
            switch (Season)
            {
                case SeasonType.Spring: 
                    Console.WriteLine("{0}月是春天",month);
                    break;
                case SeasonType.Summer: 
                    Console.WriteLine("{0}月是夏天",month);
                    break;
                case SeasonType.Autumn: 
                    Console.WriteLine("{0}月是秋天",month);
                    break;
                case SeasonType.Winter: 
                    Console.WriteLine("{0}月是冬天",month);
                    break;
                default: 
                    Console.WriteLine("輸入錯誤");
                    break;
                
            }
        }
    }
}