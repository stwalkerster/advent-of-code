namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;

    public class Day9
    {
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day9/main.txt").ToList();

            var ySize = input.Count;
            var xSize = input.First().Length;
            
            var heightmap = new short[xSize, ySize];

            for (int y = 0; y < ySize; y++)
            {
                var line = input[y];
                for (int x = 0; x < line.Length; x++)
                {
                    heightmap[x, y] = short.Parse(""+line[x]);
                }
            }

            var sum = 0;
            for (int y = 0; y < ySize; y++)
            {
                for (int x = 0; x < xSize; x++)
                {
                    // left
                    if (x > 0 && heightmap[x, y] >= heightmap[x-1, y])
                    {
                        // not a high point
                        continue;
                    }
                    
                    // right
                    if (x < (xSize - 1) && heightmap[x, y] >= heightmap[x+1, y])
                    {
                        // not a high point
                        continue;
                    }
                    
                    // up
                    if (y > 0 && heightmap[x, y] >= heightmap[x, y-1])
                    {
                        // not a high point
                        continue;
                    }
                    
                    // down
                    if (y < (ySize - 1) && heightmap[x, y] >= heightmap[x, y + 1])
                    {
                        // not a high point
                        continue;
                    }

                    sum += heightmap[x, y] + 1;
                    Console.WriteLine($"  Found lowpoint at {x},{y} = {heightmap[x, y]}");
                }
            }

            Console.WriteLine(sum);
        }

        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day9/main.txt").ToList();

            var ySize = input.Count;
            var xSize = input.First().Length;

            var heightmap = new short[xSize, ySize];
            var basinmap = new int[xSize, ySize];

            for (int y = 0; y < ySize; y++)
            {
                var line = input[y];
                for (int x = 0; x < line.Length; x++)
                {
                    heightmap[x, y] = short.Parse("" + line[x]);
                    basinmap[x, y] = (int)' ';
                }
            }

            var lastUsed = 0;

            for (int y = 0; y < ySize; y++)
            {
                var equivset = new Dictionary<int, int>();

                for (int x = 0; x < xSize; x++)
                {
                    if (heightmap[x, y] == 9)
                    {
                        basinmap[x, y] = -1;
                        continue;
                    }

                    // up
                    if (y > 0 && basinmap[x, y - 1] > 0)
                    {
                        basinmap[x, y] = basinmap[x, y - 1];

                        // verify left
                        if (x > 0 && basinmap[x - 1, y] > 0 && basinmap[x - 1, y] != basinmap[x, y])
                        {
                            // oops. we've allocated two IDs to one basin. Overwrite one of the IDs.
                            var overwrite = basinmap[x - 1, y];
                            for (int y2 = 0; y2 < ySize; y2++)
                            {
                                for (int x2 = 0; x2 < xSize; x2++)
                                {
                                    if (basinmap[x2, y2] == overwrite)
                                    {
                                        basinmap[x2, y2] = basinmap[x, y];
                                    }
                                }
                            }
                        }

                        continue;
                    }

                    // left
                    if (x > 0 && basinmap[x - 1, y] > 0)
                    {
                        basinmap[x, y] = basinmap[x - 1, y];
                        continue;
                    }

                    basinmap[x, y] = ++lastUsed;
                }
            }
            
            var basins = new int[lastUsed + 1];
            foreach (var i in basinmap)
            {
                if(i == -1){continue;}

                basins[i]++;
            }

            Console.WriteLine(basins.OrderByDescending(x => x).Take(3).ToList().Aggregate(1, (t, c) => t * c));

        }
    }
}