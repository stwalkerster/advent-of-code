namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Text.RegularExpressions;

    public class Day4
    {
        class Board
        {
            private readonly bool[,] boardMarks = new bool[5, 5];
            public int[,] BoardNumbers { get; init; }
            public bool Won { get; set; } = false;

            public bool DoDraw(int number)
            {
                for (int x = 0; x < 5; x++)
                {
                    var exit = false;
                    for (int y = 0; y < 5; y++)
                    {
                        if (number == BoardNumbers[x, y])
                        {
                            // Thoughts: what happens if the same number appears twice on one card?
                            this.boardMarks[x, y] = true;
                            exit = true;
                            break;
                        }
                    }

                    if (exit)
                    {
                        break;
                    }
                }
                
                // check for win
                for (int x = 0; x < 5; x++)
                {
                    var success = true;
                    for (int y = 0; y < 5; y++)
                    {
                        success &= this.boardMarks[x, y];
                        if (!success) break;
                    }

                    if (success)
                    {
                        this.Won = true;
                        return true;
                    }
                }
                
                for (int y = 0; y < 5; y++)
                {
                    var success = true;
                    for (int x = 0; x < 5; x++)
                    {
                        success &= this.boardMarks[x, y];
                        if (!success) break;
                    }

                    if (success)
                    {
                        this.Won = true;
                        return true;
                    }
                }
                
                return false;
            }

            public int GetScore(int number)
            {
                int total = 0;
                for (int x = 0; x < 5; x++)
                {
                    for (int y = 0; y < 5; y++)
                    {
                        if (!this.boardMarks[x, y])
                        {
                            total += this.BoardNumbers[x, y];
                        }
                    }
                }

                return total * number;
            }

            public void PrintBoard()
            {
                var original = Console.ForegroundColor;
                for (int y = 0; y < 5; y++)
                {
                    for (int x = 0; x < 5; x++)
                    {
                        if (this.boardMarks[x, y])
                        {
                            Console.ForegroundColor = ConsoleColor.White;
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Gray;
                        }
                        
                        Console.Write(BoardNumbers[x,y].ToString().PadLeft(3));
                    }
                    Console.WriteLine();
                }
                Console.WriteLine();
                Console.ForegroundColor = original;
            }
        }
        
        (List<int>, List<int[,]>) LoadDatafile()
        {
            var input = File.ReadAllLines("Data/Day4/main.txt").ToList();
            var draws = input.First().Split(',').Select(int.Parse).ToList();
            
            input = input.Skip(1).ToList();
            var boards = new List<int[,]>();
            
            var regex = new Regex("^([0-9 ]{2}) ([0-9 ]{2}) ([0-9 ]{2}) ([0-9 ]{2}) ([0-9 ]{2})$");

            for (int i = 0; i < input.Count; i += 6)
            {
                var board = new int[5, 5];

                for (int y = 0; y < 5; y++)
                {
                    var match = regex.Match(input[i+y+1]);

                    for (int x = 0; x < 5; x++)
                    {
                        board[x, y] = int.Parse(match.Groups[x + 1].Value.Trim());
                    }
                }

                boards.Add(board);
            }

            return (draws, boards);
        }
        
        public void Part1()
        {
            var (draws, rawBoards) = this.LoadDatafile();

            var boards = rawBoards.Select(x => new Board { BoardNumbers = x }).ToList();

            foreach (var draw in draws)
            {
                foreach (var board in boards)
                {
                    var win = board.DoDraw(draw);
                    if (win)
                    {
                        board.PrintBoard();
                        
                        Console.WriteLine(board.GetScore(draw));
                        return;
                    }
                }
            }
        }
        
        public void Part2()
        {
            var (draws, rawBoards) = this.LoadDatafile();

            var boards = rawBoards.Select(x => new Board { BoardNumbers = x }).ToList();

            foreach (var draw in draws)
            {
                foreach (var board in boards)
                {
                    var win = board.DoDraw(draw);

                    if (win && boards.Count == 1)
                    {
                        board.PrintBoard();
                        
                        Console.WriteLine(board.GetScore(draw));
                        return;
                    }
                }

                boards = boards.Where(x => !x.Won).ToList();
            }
        }
    }
}