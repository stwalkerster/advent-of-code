namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;

    public class Day6
    {
        public void Part1()
        {
            var input = File.ReadAllLines("Data/Day6/main.txt").First().Split(',').Select(int.Parse).ToList();

            for (var day = 1; day <= 80; day++)
            {
                var newFish = 0;
                for (var i = 0; i < input.Count; i++)
                {
                    if (input[i] == 0)
                    {
                        input[i] = 6;
                        newFish++;
                    }
                    else
                    {
                        input[i]--;
                    }
                }

                var newFishAges = new int[newFish];
                Array.Fill(newFishAges, 8);

                input.AddRange(newFishAges);
            }

            Console.WriteLine(input.Count);
        }
        
        public void Part2()
        {
            var input = File.ReadAllLines("Data/Day6/main.txt").First().Split(',').Select(int.Parse).ToList();

            var fish = new Dictionary<int, ulong>
                { { 0, 0 }, { 1, 0 }, { 2, 0 }, { 3, 0 }, { 4, 0 }, { 5, 0 }, { 6, 0 }, { 7, 0 }, { 8, 0 } };

            foreach (var t in input)
            {
                fish[t]++;
            }

            for (var day = 1; day <= 256; day++)
            {
                // back up the number of "willing" fish.
                var willingFish = fish[0];

                // drop all ages
                for (int fishAge = 0; fishAge < 8; fishAge++)
                {
                    fish[fishAge] = fish[fishAge + 1];
                }
                
                // spawn new fish
                fish[8] = willingFish;

                // reset the adults
                fish[6] += willingFish;
                
                Console.WriteLine($"{day};{fish[0]};{fish[1]};{fish[2]};{fish[3]};{fish[4]};{fish[5]};{fish[6]};{fish[7]};{fish[8]}");
            }

            Console.WriteLine(fish.Aggregate(0ul, (c, n) => c + n.Value));
        }
    }
}
