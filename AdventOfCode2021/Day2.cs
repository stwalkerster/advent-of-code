namespace AdventOfCode2021
{
    using System;
    using System.IO;
    using System.Linq;

    public class Day2
    {
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day2/main.txt").ToList();

            var posX = 0;
            var depthY = 0;

            foreach (var line in input)
            {
                var values = line.Split(' ', 2);

                var command = values[0];
                var value = int.Parse(values[1]);

                switch (command)
                {
                    case "down":
                        depthY += value;
                        break;
                    case "up":
                        depthY -= value;
                        break;
                    case "forward":
                        posX += value;
                        break;
                }
            }

            Console.WriteLine(depthY * posX);
        }

        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day2/main.txt").ToList();

            var posX = 0;
            var aimY = 0;
            var depthY = 0;

            foreach (var line in input)
            {
                var values = line.Split(' ', 2);

                var command = values[0];
                var value = int.Parse(values[1]);

                switch (command)
                {
                    case "down":
                        aimY += value;
                        break;
                    case "up":
                        aimY -= value;
                        break;
                    case "forward":
                        posX += value;
                        depthY += (value * aimY);
                        break;
                }
            }

            Console.WriteLine(depthY * posX);
        }
    }
}