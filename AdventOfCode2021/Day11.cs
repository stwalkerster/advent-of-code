namespace AdventOfCode2021
{
    using System;
    using System.IO;
    using System.Linq;

    public class Day11
    {
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day11/main.txt").ToList();

            var grid = new int[10, 10];
            
            for (int y = 0; y < 10; y++)
            {
                for (int x = 0; x < 10; x++)
                {
                    grid[x,y] = input[y][x] - '0';
                }
            }

            var flashCount = 0;
            for (int i = 0; i < 100; i++)
            {
                var flashLog = new bool[10, 10];
                
                // inc all
                LoopAll((x, y) => grid[x, y]++);
                
                LoopAll(
                    (x, y) =>
                    {
                        DoFlash(grid, flashLog, x, y);
                        
                    });
                
                
                // reset to zero
                LoopAll(
                    (x, y) =>
                    {
                        if (flashLog[x, y])
                        {
                            grid[x, y] = 0;
                        }
                    });

                Console.WriteLine($"\n{i + 1}:");
                // PrintGrid(grid);
                LoopAll((x, y) => flashCount = flashLog[x, y] ? flashCount + 1 : flashCount);
                Console.WriteLine($"  {flashCount} flashes");
            }
        }

        private void DoFlash(int[,] grid, bool[,] flashLog, int x, int y)
        {
            if (x is < 0 or > 9 || y is < 0 or > 9)
            {
                return;
            }

            if (grid[x, y] > 9 && !flashLog[x, y])
            {
                flashLog[x, y] = true;
                if (x > 0)
                {
                    if (y > 0)
                    {
                        grid[x - 1, y - 1]++;
                    }

                    grid[x - 1, y]++;
                    
                    if (y < 9)
                    {
                        grid[x - 1, y + 1]++;
                    }
                }

                if (y > 0)
                {
                    grid[x, y - 1]++;
                }

                if (y < 9)
                {
                    grid[x, y + 1]++;
                }

                if (x < 9)
                {
                    if (y > 0)
                    {
                        grid[x + 1, y - 1]++;
                    }

                    grid[x + 1, y]++;

                    if (y < 9)
                    {
                        grid[x + 1, y + 1]++;
                    }
                }

                this.DoFlash(grid, flashLog, x - 1, y - 1);
                this.DoFlash(grid, flashLog, x - 1, y );
                this.DoFlash(grid, flashLog, x - 1, y + 1);
                this.DoFlash(grid, flashLog, x  , y - 1);
                this.DoFlash(grid, flashLog, x  , y + 1);
                this.DoFlash(grid, flashLog, x + 1, y - 1);
                this.DoFlash(grid, flashLog, x + 1, y);
                this.DoFlash(grid, flashLog, x + 1, y + 1);
            }
        }

        static void LoopAll(Action<int, int> action)
        {
            for (int y = 0; y < 10; y++)
            {
                for (int x = 0; x < 10; x++)
                {
                    action(x, y);
                }    
            }
        }

        private void PrintGrid(int[,] grid)
        {
            for (int y = 0; y < 10; y++)
            {
                for (int x = 0; x < 10; x++)
                {
                    if (grid[x, y] == 0)
                    {
                        Console.ForegroundColor = ConsoleColor.White;
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Gray;
                    }
                    
                    Console.Write(grid[x, y] + " ");
                }

                Console.WriteLine();
            }
        }

        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day11/main.txt").ToList();

            var grid = new int[10, 10];
            
            for (int y = 0; y < 10; y++)
            {
                for (int x = 0; x < 10; x++)
                {
                    grid[x,y] = input[y][x] - '0';
                }
            }

            var flashCount = 0;
            for (int i = 0; flashCount != 100; i++)
            {
                flashCount = 0;
                var flashLog = new bool[10, 10];
                
                // inc all
                LoopAll((x, y) => grid[x, y]++);
                
                LoopAll(
                    (x, y) =>
                    {
                        DoFlash(grid, flashLog, x, y);
                        
                    });
                
                
                // reset to zero
                LoopAll(
                    (x, y) =>
                    {
                        if (flashLog[x, y])
                        {
                            grid[x, y] = 0;
                        }
                    });

                Console.WriteLine($"\n{i + 1}:");
                PrintGrid(grid);
                LoopAll((x, y) => flashCount = flashLog[x, y] ? flashCount + 1 : flashCount);
                Console.WriteLine($"  {flashCount} flashes");
            }
        }
    }
}