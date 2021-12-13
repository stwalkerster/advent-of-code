namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.IO;
    using System.Linq;
    using System.Text.RegularExpressions;

    public class Day13
    {
        public void Part1()
        {
            var (coords, folds) = this.LoadData("Data/Day13/main.txt");

            foreach (var fold in folds)
            {
                if (fold.Dimension == "y")
                {
                    var newCoords = new List<(int X, int Y)>();
                    foreach (var point in coords)
                    {
                        if (point.Y > fold.Position)
                        {
                            var newY = fold.Position - (point.Y - fold.Position);
                            // Console.WriteLine($"Point {point} moves to y={newY}");
                            
                            newCoords.Add((X: point.X, Y: newY));
                        }
                        else
                        {
                            newCoords.Add(point);
                        }
                    }

                    coords = newCoords;
                    this.Visualise(coords, true);
                }
                else
                {
                    var newCoords = new List<(int X, int Y)>();
                    foreach (var point in coords)
                    {
                        if (point.X > fold.Position)
                        {
                            var newX = fold.Position - (point.X - fold.Position);
                           // Console.WriteLine($"Point {point} moves to x={newX}");
                            
                            newCoords.Add((X: newX, Y: point.Y));
                        }
                        else
                        {
                            newCoords.Add(point);
                        }
                    }

                    coords = newCoords;
                    this.Visualise(coords, true);
                }
            }
            
            this.Visualise(coords, false);
            
        }

        public void Part2()
        {
            // I got carried away with part 1 and realised I had solved the entire thing before reading the question
            // properly...
            this.Part1();
        }
        
        private void Visualise(List<(int X, int Y)> coords, bool onlyVisible)
        {
            var maxX = 0;
            var minX = 0;
            var maxY = 0;
            var minY = 0;
            foreach (var p in coords)
            {
                if (p.X > maxX) maxX = p.X;
                if (p.X < minX) minX = p.X;
                if (p.Y > maxY) maxY = p.Y;
                if (p.Y < minY) minY = p.Y;
            }

            var sizeX = maxX - minX + 1;
            var sizeY = maxY - minY + 1;

            var grid = new bool[sizeX, sizeY];
            foreach (var p in coords)
            {
                grid[p.X + minX, p.Y + minY] = true;
            }

            var visiblePoints = 0;
            for (int y = 0; y < sizeY; y++)
            {
                for (int x = 0; x < sizeX; x++)
                {
                    string point = ".";
                    if (grid[x, y])
                    {
                        if (!onlyVisible)
                        {
                            Console.ForegroundColor = ConsoleColor.White;
                            point = "#";
                        }

                        visiblePoints++;
                    }
                    else
                    {
                        if (!onlyVisible)
                        {
                            Console.ForegroundColor = ConsoleColor.DarkGray;
                        }
                    }

                    if (!onlyVisible)
                    {
                        Console.Write(point);
                    }
                }

                if (!onlyVisible)
                {
                    Console.WriteLine();
                }

            }
            Console.WriteLine($"Visible points: {visiblePoints}");
            Console.WriteLine();
        }
        
        private (List<(int X, int Y)> Coords, List<(string Dimension, int Position)> Folds) LoadData(string datafile)
        {
            var input = File.ReadAllLines(datafile).ToList();

            var coords = input.Take(input.IndexOf("")).Select(l =>
            {
                var strings = l.Split(',', 2);
                return (X: int.Parse(strings[0]), Y: int.Parse(strings[1]));
            }).ToList();

            var foldRegex = new Regex("^fold along (?<dimension>[xy])=(?<position>[0-9]+)$");
            var folds = input.Skip(input.IndexOf("") + 1).Select(
                l =>
                {
                    var match = foldRegex.Match(l);
                    return (Dimension: match.Groups["dimension"].Value, Position: int.Parse(match.Groups["position"].Value));
                }).ToList();

            return (Coords: coords, Folds: folds);
        }
    }
}