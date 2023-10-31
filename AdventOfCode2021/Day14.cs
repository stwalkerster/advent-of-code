using System.Diagnostics;

namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Text;
    using CC = System.Collections.Generic.Dictionary<char, ulong>;

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

        [DebuggerDisplay("{DebuggerDisplay,nq}")]
        class InsertionRule
        {
            public char Left { get; set; }
            public char Right { get; set; }
            public char Result { get; set; }
            
            public InsertionRule LeftResult { get; set; }
            public InsertionRule RightResult { get; set; }

            public string DebuggerDisplay => $"{Left}{Right} -> {Result}";
        }
        
        public void Part2()
        {
            const int IterCount = 40;
            var (template, insertionRules) = this.LoadData("Data/Day14/main.txt");

            var rules = insertionRules.ToDictionary(k => k.Key, x => new InsertionRule
            {
                Left = x.Key[0],
                Right = x.Key[1],
                Result = x.Value[0]
            });

            var globalCharCounts = new CC();
            var charCountsCache = new Dictionary<string, CC>();
            
            foreach (var r in rules)
            {
                globalCharCounts.TryAdd(r.Value.Left, 0);
                globalCharCounts.TryAdd(r.Value.Right, 0);
                globalCharCounts.TryAdd(r.Value.Result, 0);

                r.Value.LeftResult = rules[r.Value.Left.ToString() + r.Value.Result];
                r.Value.RightResult = rules[r.Value.Result.ToString() + r.Value.Right];
            }

            CC WalkTree(InsertionRule pair, int depth)
            {
                var charCounts = new CC { { pair.Result, 1 } };

                if (depth >= IterCount)
                {
                    return charCounts;
                }
                
                CC l;
                var lKey = $"{pair.LeftResult.Left}{pair.LeftResult.Right}/{depth + 1}";
                if (!charCountsCache.ContainsKey(lKey))
                {
                    l = WalkTree(pair.LeftResult, depth+1);
                    charCountsCache.TryAdd(lKey, l);
                }
                else
                {
                    l = charCountsCache[lKey];
                }
                
                CC r;
                var rKey = $"{pair.RightResult.Left}{pair.RightResult.Right}/{depth + 1}";
                if (!charCountsCache.ContainsKey(rKey))
                {
                    r = WalkTree(pair.RightResult, depth+1);
                    charCountsCache.TryAdd(rKey, r);
                }
                else
                {
                    r = charCountsCache[rKey];
                }

                foreach (var kvp in l)
                {
                    if (charCounts.ContainsKey(kvp.Key))
                    {
                        charCounts[kvp.Key] += kvp.Value;
                    }
                    else
                    {
                        charCounts.Add(kvp.Key, kvp.Value);
                    }
                }
                
                foreach (var kvp in r)
                {
                    if (charCounts.ContainsKey(kvp.Key))
                    {
                        charCounts[kvp.Key] += kvp.Value;
                    }
                    else
                    {
                        charCounts.Add(kvp.Key, kvp.Value);
                    }
                }

                return charCounts;
            }

            globalCharCounts[template[0]]++;
            for (var i = 1; i < template.Length; i++)
            {
                Console.WriteLine($"[{DateTime.UtcNow.ToLongTimeString()}]: {i} / {template.Length -1}");
                globalCharCounts[template[i]]++;
                var result = WalkTree(rules[template.Substring(i-1, 2)], 1);
                
                foreach (var kvp in result)
                {
                    if (globalCharCounts.ContainsKey(kvp.Key))
                    {
                        globalCharCounts[kvp.Key] += kvp.Value;
                    }
                    else
                    {
                        globalCharCounts.Add(kvp.Key, kvp.Value);
                    }
                }
            }
            
            Console.WriteLine(globalCharCounts.Values.Min());
            Console.WriteLine(globalCharCounts.Values.Max());
            Console.WriteLine(globalCharCounts.Values.Max() - globalCharCounts.Values.Min());
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