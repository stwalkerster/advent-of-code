namespace AdventOfCode2021
{
    using System;
    using System.IO;
    using System.Linq;

    public class Day1
    {
        public void Part1()
        {
            var last = int.MaxValue;
            var count = 0;
            var input = File.ReadAllLines("Data/Day1/main.txt").Select(int.Parse).ToList();

            foreach (var item in input)
            {
                if (item > last)
                {
                    count++;
                }

                last = item;
            }

            Console.WriteLine(count);
        }
    
        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day1/main.txt").Select(int.Parse).ToList();
            var last = int.MaxValue;
            var count = 0;
            
            for (int i = 0; i < input.Count - 2; i++)
            {
                var sum = input[i] + input[i + 1] + input[i + 2];
                
                if (sum > last)
                {
                    count++;
                }

                last = sum;
            }

            Console.WriteLine(count);
        }
    }
}