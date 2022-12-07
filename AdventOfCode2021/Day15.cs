namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;

    public class Day15
    {
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day15/main.txt").ToList();

            var costs = new int[input[0].Length, input.Count];
            
            for (int y = 0; y < input.Count; y++)
            {
                for (int x = 0; x < input[y].Length; x++)
                {
                    costs[x, y] = input[y][x] - '0';
                }
            }
            
            var minPath = this.Dijkstra(costs);

            Console.WriteLine(minPath);
        }

        private int Dijkstra(int[,] costs)
        {
            var visited = new bool[costs.GetLength(0), costs.GetLength(1)];
            var distances = new int[costs.GetLength(0), costs.GetLength(1)];
            for (int y = 0; y < costs.GetLength(1); y++)
            {
                for (int x = 0; x < costs.GetLength(0); x++)
                {
                    visited[x, y] = false;
                    distances[x, y] = int.MaxValue;
                }
            }

            IEnumerable<(int x, int y)> GetUnvisited((int x, int y) current)
            {
                if (current.x > 0 && !visited[current.x - 1, current.y])
                    yield return (current.x - 1, y: current.y);

                if (current.x < visited.GetLength(0) - 1 && !visited[current.x + 1, current.y])
                    yield return (current.x + 1, y: current.y);

                if (current.y > 0 && !visited[current.x, current.y - 1])
                    yield return (x: current.x, current.y - 1);

                if (current.y < visited.GetLength(1) - 1 && !visited[current.x, current.y + 1])
                    yield return (x: current.x, current.y + 1);
            }

            distances[0, 0] = 0;
            var visitQueue = new PriorityQueue<(int x, int y), int>();
            visitQueue.Enqueue((x: 0, y: 0), 0);

            while (visitQueue.Count > 0)
            {
                var current = visitQueue.Dequeue();

                if (current.x == visited.GetLength(0) - 1 && current.y == visited.GetLength(1) - 1)
                {
                    break;
                }

                foreach (var unvNode in GetUnvisited(current))
                {
                    var dist = distances[current.x, current.y] + costs[unvNode.x, unvNode.y];
                    if (distances[unvNode.x, unvNode.y] > dist)
                    {
                        distances[unvNode.x, unvNode.y] = dist;
                        visitQueue.Enqueue(unvNode, dist);
                    }
                }

                visited[current.x, current.y] = true;
            }

            var minPath = distances[distances.GetLength(0) - 1, distances.GetLength(1) - 1];
            return minPath;
        }

        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day15/main.txt").ToList();

            var costs = new int[input[0].Length * 5, input.Count * 5];

            for (int xp = 0; xp < 5; xp++)
            {
                for (int yp = 0; yp < 5; yp++)
                {
                    var xOffset = input[0].Length * xp;
                    var yOffset = input.Count * yp;

                    for (int y = 0; y < input.Count; y++)
                    {
                        for (int x = 0; x < input[y].Length; x++)
                        {
                            var value = input[y][x] - '0' + xp + yp;
                            if (value > 9)
                            {
                                value -= 9;
                            }
                            
                            costs[x + xOffset, y + yOffset] = value;
                        }
                    }
                }
            }

            var minPath = this.Dijkstra(costs);

            Console.WriteLine(minPath);
        }
    }
}