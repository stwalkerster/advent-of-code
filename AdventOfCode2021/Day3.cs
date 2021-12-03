namespace AdventOfCode2021
{
    using System;
    using System.IO;
    using System.Linq;

    public class Day3
    {
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day3/main.txt").ToList();

            var gamma = 0;
            var epsilon = 0;
            
            var ints = input.Select(x => Convert.ToInt32(x, 2)).ToList();

            for (var i = 0; i < input.First().Length; i++)
            {
                var filter = (int)Math.Pow(2, i);

                if (ints.Count(x => (x & filter) == filter) > (input.Count / 2))
                {
                    gamma |= filter; 
                }
                else
                {
                    epsilon |= filter;
                }
            }
            
            Console.WriteLine($"Gamma: {gamma}, Epsilon: {epsilon}, Result: {gamma * epsilon}");
        }
        
        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day3/main.txt").ToList();

            var ints = input.Select(x => Convert.ToInt32(x, 2)).ToList();

            var oxygenSearchList = ints.ToList();
            var scrubberSearchList = ints.ToList();
            
            for (var i = input.First().Length - 1; i >= 0; i--)
            {
                var filter = (int)Math.Pow(2, i);
                
                var oxyOnes = oxygenSearchList.Count(x => (x & filter) == filter);
                var scrubOnes = scrubberSearchList.Count(x => (x & filter) == filter);
                
                if (oxygenSearchList.Count > 1)
                {
                    oxygenSearchList = oxygenSearchList.Where(x => (x & filter) == (oxyOnes >= oxygenSearchList.Count / 2f ? filter : 0)).ToList();
                }

                if (scrubberSearchList.Count > 1)
                {
                    scrubberSearchList = scrubberSearchList.Where(x => (x & filter) == (scrubOnes < scrubberSearchList.Count / 2f ? filter : 0)).ToList();
                }

                if (scrubberSearchList.Count == 1 && oxygenSearchList.Count == 1)
                {
                    break;
                }
            }
            
            Console.WriteLine($"Oxygen: {oxygenSearchList.First()}, Scrubber: {scrubberSearchList.First()}, RESULT: {oxygenSearchList.First() * scrubberSearchList.First()}");
        }
    }
}