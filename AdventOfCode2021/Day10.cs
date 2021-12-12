namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.IO;
    using System.Linq;

    public class Day10
    {
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day10/main.txt").ToList();

            var scoreLookup = new Dictionary<char, int> { { ')', 3 }, { ']', 57 }, { '}', 1197 }, { '>', 25137 } };
            var score = 0;
            
            foreach (var line in input)
            {
                Stack<char> closing = new Stack<char>();

                foreach (var c in line.ToCharArray())
                {
                    if (c == '(')
                    {
                        closing.Push(')');
                        continue;
                    }

                    if (c is '{' or '<' or '[')
                    {
                        closing.Push((char)(c + 2));
                        continue;
                    }

                    if (c == closing.Peek())
                    {
                        closing.Pop();
                        continue;
                    }

                    score += scoreLookup[c];
                    break;
                }
            }
            
            Console.WriteLine(score);
        }

        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day10/main.txt").ToList();

            var scoreLookup = new Dictionary<char, ulong> { { ')', 1 }, { ']', 2 }, { '}', 3 }, { '>', 4 } };

            var scores = new List<ulong>();
            
            foreach (var line in input)
            {
                var lineScore = 0ul;
                var corrupt = false;
                Stack<char> closing = new Stack<char>();

                foreach (var c in line.ToCharArray())
                {
                    if (c == '(')
                    {
                        closing.Push(')');
                        continue;
                    }

                    if (c is '{' or '<' or '[')
                    {
                        closing.Push((char)(c + 2));
                        continue;
                    }

                    if (c == closing.Peek())
                    {
                        closing.Pop();
                        continue;
                    }

                    corrupt = true;
                    break;
                }

                if (corrupt)
                {
                    continue;
                }

                while (closing.Count > 0)
                {
                    var c = closing.Pop();

                    lineScore *= 5;
                    lineScore += scoreLookup[c];
                    
                    Console.Write(c);
                }
                Console.WriteLine($": {lineScore}");

                scores.Add(lineScore);
            }
            
            var median = scores.OrderBy(x => x).Skip(scores.Count/2).First();

            Console.WriteLine(median);
        }
    }
}