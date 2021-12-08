namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;

    public class Day8
    {
        /*
         * 1: 2 seg (unique)
         * 7: 3 seg (unique)
         * 4: 4 seg (unique)
         * 8: 7 seg (unique)
         * 9: 6 seg (includes 4)
         * 0: 6 seg (includes 7, but not 4)
         * 6: 6 seg (includes neither 7 nor 4)
         * 3: 5 seg (includes 1)
         * 5: 5 seg (included in 6 and 9)
         * 2: 5 seg
         */
        
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day8/main.txt").ToList();

            var inputData = input.Select(x => x.Split('|'))
                .Select(
                    x => (Digits: x[0].Split(' ', StringSplitOptions.RemoveEmptyEntries), DisplayValue: x[1].Split()))
                .ToList();

            var result = inputData.Aggregate(0, (t, c) => t + c.DisplayValue.Count(x => x.Length is 2 or 3 or 4 or 7));
            
            Console.WriteLine(result);
        }
        
        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day8/main.txt").ToList();

            var inputData = input.Select(x => x.Split('|'))
                .Select(
                    x => (Digits: x[0].Split(' ', StringSplitOptions.RemoveEmptyEntries), DisplayValue: x[1].Split(' ', StringSplitOptions.RemoveEmptyEntries)))
                .ToList();

            var total = 0;
            foreach (var inputTuple in inputData)
            {
                var digits = UnscrambleDigits(inputTuple.Digits).ToList();

                var value = 0;
                foreach (var inputDigit in inputTuple.DisplayValue)
                {
                    var sortedDigit = string.Join("", inputDigit.ToCharArray().OrderBy(x => x));
                    value = 10 * value +  digits.FindIndex(x => x == sortedDigit);
                }

                total += value;
            }
            
            Console.WriteLine(total);
        }

        private static string[] UnscrambleDigits(string[] scrambledDigits)
        {
            var rawDigits = scrambledDigits.Select(x => x.ToCharArray().OrderBy(c => c).Select(c => c).ToList()).ToList();
            var discoveredDigits = new List<char>[10];

            var digits = new string[10];

            int idx = -1;

            idx = rawDigits.FindIndex(x => x.Count == 2);
            discoveredDigits[1] = rawDigits[idx];
            digits[1] = string.Join("", rawDigits[idx]);
            rawDigits.RemoveAt(idx);

            idx = rawDigits.FindIndex(x => x.Count == 3);
            discoveredDigits[7] = rawDigits[idx];
            digits[7] = string.Join("", rawDigits[idx]);
            rawDigits.RemoveAt(idx);

            idx = rawDigits.FindIndex(x => x.Count == 4);
            discoveredDigits[4] = rawDigits[idx];
            digits[4] = string.Join("", rawDigits[idx]);
            rawDigits.RemoveAt(idx);

            idx = rawDigits.FindIndex(x => x.Count == 7);
            discoveredDigits[8] = rawDigits[idx];
            digits[8] = string.Join("", rawDigits[idx]);
            rawDigits.RemoveAt(idx);

            idx = rawDigits.FindIndex(x => x.Count == 6);
            while (idx != -1)
            {
                if (string.Join("", rawDigits[idx].Intersect(discoveredDigits[4]))
                    == string.Join("", discoveredDigits[4]))
                {
                    discoveredDigits[9] = rawDigits[idx];
                    digits[9] = string.Join("", rawDigits[idx]);
                    rawDigits.RemoveAt(idx);
                }
                else
                {
                    if (string.Join("", rawDigits[idx].Intersect(discoveredDigits[7]))
                        == string.Join("", discoveredDigits[7]))
                    {
                        discoveredDigits[0] = rawDigits[idx];
                        digits[0] = string.Join("", rawDigits[idx]);
                        rawDigits.RemoveAt(idx);
                    }
                    else
                    {
                        discoveredDigits[6] = rawDigits[idx];
                        digits[6] = string.Join("", rawDigits[idx]);
                        rawDigits.RemoveAt(idx);
                    }
                }

                idx = rawDigits.FindIndex(x => x.Count == 6);
            }

            idx = rawDigits.FindIndex(x => x.Count == 5);
            while (idx != -1)
            {
                if (string.Join("", rawDigits[idx].Intersect(discoveredDigits[1]))
                    == string.Join("", discoveredDigits[1]))
                {
                    discoveredDigits[3] = rawDigits[idx];
                    digits[3] = string.Join("", rawDigits[idx]);
                    rawDigits.RemoveAt(idx);
                }
                else
                {
                    if (string.Join("", discoveredDigits[6].Intersect(rawDigits[idx]))
                        == string.Join("", rawDigits[idx]))
                    {
                        discoveredDigits[5] = rawDigits[idx];
                        digits[5] = string.Join("", rawDigits[idx]);
                        rawDigits.RemoveAt(idx);
                    }
                    else
                    {
                        discoveredDigits[2] = rawDigits[idx];
                        digits[2] = string.Join("", rawDigits[idx]);
                        rawDigits.RemoveAt(idx);
                    }
                }

                idx = rawDigits.FindIndex(x => x.Count == 5);
            }

            return digits;
        }
    }
}