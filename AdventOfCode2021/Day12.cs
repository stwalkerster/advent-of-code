namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.IO;
    using System.Linq;

    public class Day12
    {

        [DebuggerDisplay("{DebuggerDisplay,nq}")]
        private class Cave
        {
            public string Name { get; set; }
            public List<Cave> Connections { get; set; } = new();

            public bool IsSmall
            {
                get { return this.Name.ToLower() == this.Name; }
            }

            private string DebuggerDisplay =>
                $"Cave {this.Name} ({string.Join(',', this.Connections.Select(x => x.Name))})";

            public override string ToString()
            {
                return this.Name;
            }
        }
        
        
        public void Part1()
        {
            var datafile = "Data/Day12/main.txt";
            var allCaves = LoadData(datafile);

            var count = 0;

            void Path(Cave current, List<Cave> path)
            {
                if (current == allCaves["end"])
                {
                    count++;
                    Console.WriteLine(string.Join(",", path));
                    return;
                }

                foreach (var nextCave in current.Connections)
                {
                    if (nextCave.IsSmall && path.Contains(nextCave))
                    {
                        // can't go back to a small cave
                        continue;
                    }

                    var localPath = new List<Cave>(path) { nextCave };
                    Path(nextCave, localPath);
                }
            }

            Path(allCaves["start"], new List<Cave> { allCaves["start"] });

            Console.WriteLine(count);
        }

        private static Dictionary<string, Cave> LoadData(string datafile)
        {
            var input = File.ReadAllLines(datafile).ToList();

            var allCaves = new Dictionary<string, Cave>();

            foreach (var line in input)
            {
                var connectedCaves = line.Split('-');

                if (!allCaves.ContainsKey(connectedCaves[0]))
                {
                    allCaves.Add(connectedCaves[0], new Cave { Name = connectedCaves[0] });
                }

                if (!allCaves.ContainsKey(connectedCaves[1]))
                {
                    allCaves.Add(connectedCaves[1], new Cave { Name = connectedCaves[1] });
                }

                allCaves[connectedCaves[0]].Connections.Add(allCaves[connectedCaves[1]]);
                allCaves[connectedCaves[1]].Connections.Add(allCaves[connectedCaves[0]]);
            }

            return allCaves;
        }

        public void Part2()
        {
            var datafile = "Data/Day12/main.txt";
            var allCaves = LoadData(datafile);

            var count = 0;

            void Path(Cave current, List<Cave> path, bool visitedTwice)
            {
                if (current == allCaves["end"])
                {
                    count++;
                    Console.WriteLine(string.Join(",", path));
                    return;
                }

                foreach (var nextCave in current.Connections.Where(x => x.Name != "start"))
                {
                    if (nextCave.IsSmall && path.Contains(nextCave) && visitedTwice)
                    {
                        // can't go back to a small cave
                        continue;
                    }

                    var revisit = nextCave.IsSmall && path.Contains(nextCave);

                    var localPath = new List<Cave>(path) { nextCave };
                    Path(nextCave, localPath, visitedTwice || revisit);
                }
            }

            Path(allCaves["start"], new List<Cave> { allCaves["start"] }, false);

            Console.WriteLine(count);
        }
    }
}