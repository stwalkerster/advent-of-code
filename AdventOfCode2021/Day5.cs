namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Text.RegularExpressions;

    public class Day5
    {
        public void Part1()
        {
            var lines = this.LoadDataset();

            var maxX = lines.SelectMany(x => new[] { x.Item1.X, x.Item2.X }).Max();
            var maxY = lines.SelectMany(x => new[] { x.Item1.Y, x.Item2.Y }).Max();

            var field = new int[maxX + 1, maxY + 1];

            foreach (var coordsTuple in lines.Where(t => t.Item1.X == t.Item2.X || t.Item1.Y == t.Item2.Y))
            {
                if (coordsTuple.Item1.X == coordsTuple.Item2.X)
                {
                    for (int y = Math.Min(coordsTuple.Item1.Y, coordsTuple.Item2.Y); y <= Math.Max(coordsTuple.Item1.Y, coordsTuple.Item2.Y); y++)
                    {
                        field[coordsTuple.Item1.X, y]++;
                    }
                }
                
                if (coordsTuple.Item1.Y == coordsTuple.Item2.Y)
                {
                    for (int x = Math.Min(coordsTuple.Item1.X, coordsTuple.Item2.X); x <= Math.Max(coordsTuple.Item1.X, coordsTuple.Item2.X); x++)
                    {
                        field[x, coordsTuple.Item1.Y]++;
                    }
                }
            }

            this.PrintField(maxY, maxX, field);

            var count = 0;
            for (int y = 0; y <= maxY; y++)
            {
                for (int x = 0; x <= maxX; x++)
                {
                    if (field[x, y] > 1)
                    {
                        count++;
                    }
                    
                }
            }

            Console.WriteLine(count);
        }

        public void Part2()
        {
            var lines = this.LoadDataset();

            var maxX = lines.SelectMany(x => new[] { x.Item1.X, x.Item2.X }).Max();
            var maxY = lines.SelectMany(x => new[] { x.Item1.Y, x.Item2.Y }).Max();

            var field = new int[maxX + 1, maxY + 1];

            foreach (var coordsTuple in lines)
            {
                if (coordsTuple.Item1.X == coordsTuple.Item2.X)
                {
                    for (int y = Math.Min(coordsTuple.Item1.Y, coordsTuple.Item2.Y); y <= Math.Max(coordsTuple.Item1.Y, coordsTuple.Item2.Y); y++)
                    {
                        field[coordsTuple.Item1.X, y]++;
                    }
                }
                else if (coordsTuple.Item1.Y == coordsTuple.Item2.Y)
                {
                    for (int x = Math.Min(coordsTuple.Item1.X, coordsTuple.Item2.X); x <= Math.Max(coordsTuple.Item1.X, coordsTuple.Item2.X); x++)
                    {
                        field[x, coordsTuple.Item1.Y]++;
                    }
                }
                else
                {
                    var dX = coordsTuple.Item2.X - coordsTuple.Item1.X; 
                    var dY = coordsTuple.Item2.Y - coordsTuple.Item1.Y;
                    var xMin = Math.Min(coordsTuple.Item1.X, coordsTuple.Item2.X);
                    var xMax = Math.Max(coordsTuple.Item1.X, coordsTuple.Item2.X);
                    var directionY = 1;
                    
                    if (dX < 0)
                    {
                        directionY *= -1;
                    }

                    if (dY < 0)
                    {
                        directionY *= -1;
                    }

                    var offsetX = xMin;
                    var offsetY = xMin == coordsTuple.Item1.X ? coordsTuple.Item1.Y : coordsTuple.Item2.Y;
                    
                    
                    var iLimit = xMax - xMin + 1;
                    
                    for (int i = 0; i < iLimit; i++)
                    {
                        var x = i + offsetX;
                        var y = offsetY + (directionY * i);
                        field[x, y]++;
                    }
                }
            }
            
            this.PrintField(maxY, maxX, field);

            var count = 0;
            for (int y = 0; y <= maxY; y++)
            {
                for (int x = 0; x <= maxX; x++)
                {
                    if (field[x, y] > 1)
                    {
                        count++;
                    }
                    
                }
            }

            Console.WriteLine(count);
        }
        
        private void PrintField(int maxY, int maxX, int[,] field)
        {
            for (int y = 0; y <= maxY; y++)
            {
                for (int x = 0; x <= maxX; x++)
                {
                    Console.Write(field[x, y] == 0 ? "." : field[x, y]);
                }

                Console.WriteLine();
            }

            Console.WriteLine();
        }

        private List<((int X, int Y), (int X, int Y))> LoadDataset()
        {
            var input = File.ReadAllLines("Data/Day5/main.txt").ToList();

            var parseRegex = new Regex("(?<ax>[0-9]+),(?<ay>[0-9]+) -> (?<bx>[0-9]+),(?<by>[0-9]+)");

            var lines = input.Select(
                    x =>
                    {
                        var match = parseRegex.Match(x);

                        if (!match.Success)
                        {
                            throw new Exception("parse fail.");
                        }

                        return ((X: int.Parse(match.Groups["ax"].Value), Y: int.Parse(match.Groups["ay"].Value)),
                            (X: int.Parse(match.Groups["bx"].Value), Y: int.Parse(match.Groups["by"].Value)));
                    })
                .ToList();
            return lines;
        }
    }
}