namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Text;

    public class Day14
    {
        public void Part1()
        {
            const int IterCount = 10;
            var (template, insertionRules) = this.LoadData("Data/Day14/main.txt");

            for (var i = 1; i <= IterCount; i++)
            {
                var sb = new StringBuilder();
                for (var p = 1; p < template.Length; p++)
                {
                    sb.Append(template[p - 1]);
                    sb.Append(insertionRules[template.Substring(p - 1, 2)]);
                }

                sb.Append(template[^1]);
                template = sb.ToString();
            
                Console.WriteLine($"{i}: Length: {template.Length}");
            }

            var frequency = template.ToCharArray()
                .Aggregate(
                    new Dictionary<char, int>(),
                    (ints, c) =>
                    {
                        if (!ints.ContainsKey(c))
                        {
                            ints.Add(c, 0);
                        }

                        ints[c]++;
                        return ints;
                    });

            var result = frequency.Max(x => x.Value) - frequency.Min(x => x.Value);
            Console.WriteLine(result);
        }

        public void Part2()
        {
            const int IterCount = 40;
            var (template, insertionRules) = this.LoadData("Data/Day14/example.txt");

            for (var i = 1; i <= IterCount; i++)
            {
                var sb = new StringBuilder();
                for (var p = 1; p < template.Length; p++)
                {
                    sb.Append(template[p - 1]);
                    sb.Append(insertionRules[template.Substring(p - 1, 2)]);
                }

                sb.Append(template[^1]);
                template = sb.ToString();
            
                Console.WriteLine($"{i}: Length: {template.Length}");
            }

            var frequency = template.ToCharArray()
                .Aggregate(
                    new Dictionary<char, ulong>(),
                    (ints, c) =>
                    {
                        if (!ints.ContainsKey(c))
                        {
                            ints.Add(c, 0);
                        }

                        ints[c]++;
                        return ints;
                    });

            var result = frequency.Max(x => x.Value) - frequency.Min(x => x.Value);
            Console.WriteLine(result);
        }
        
        private (string Template, Dictionary<string, string> InsertionRules) LoadData(string datafile)
        {
            var input = File.ReadAllLines(datafile).ToList();

            var template = input.First();

            var insertionRules = input.Skip(2).Select(x => x.Split(' ')).ToDictionary(k => k[0], v => v[2]);

            return (Template: template, InsertionRules: insertionRules);
        }
    }
}