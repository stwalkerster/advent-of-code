namespace AdventOfCode2021
{
    using System;
    using System.IO;
    using System.Linq;

    public class Day7
    {
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day7/main.txt").First().Split(',').Select(int.Parse).ToList();
            var minFuel = int.MaxValue;

            for (int i = input.Min(); i <= input.Max(); i++)
            {
                minFuel = Math.Min(minFuel, input.Select(x => Math.Abs(x - i))
                    .Aggregate(0, (t, n) => t + n));
            }

            Console.WriteLine(minFuel);
        }
        
        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day7/main.txt").First().Split(',').Select(int.Parse).ToList();
            var minFuel = int.MaxValue;

            for (int i = input.Min(); i <= input.Max(); i++)
            {
                minFuel = Math.Min(minFuel, input.Select(x => Math.Abs(x - i))
                    .Select(x => x * (x + 1) / 2)
                    .Aggregate(0, (t, n) => t + n));
            }

            Console.WriteLine(minFuel);
        }
    }
}