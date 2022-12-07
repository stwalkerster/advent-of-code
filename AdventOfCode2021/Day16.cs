namespace AdventOfCode2021
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.Design;
    using System.Diagnostics;
    using System.IO;
    using System.Linq;

    public class Day16
    {
        public void Part1()
        {
            var data = "A0016C880162017C3686B18A3D4780";
            data = File.ReadAllLines("Data/Day16/main.txt").First();

            var databin = "";
            for (var i = 0; i < data.Length; i+=2)
            {
                databin += Convert.ToString(Convert.ToInt32("" + data[i] + data[i + 1], 16), 2).PadLeft(8, '0');
            }

            var packet = Packet.Parse(ref databin);

            var toParse = new Queue<Packet>( );
            toParse.Enqueue(packet);
            var versionSum = 0;
            while (toParse.Any())
            {
                var p = toParse.Dequeue();
                versionSum += p.Version;

                if (p is OperatorPacket operatorPacket)
                {
                    foreach (var child in operatorPacket.SubPackets)
                    {
                        toParse.Enqueue(child);
                    }
                }
            }

            Console.WriteLine(versionSum);
        }

        public abstract class Packet
        {
            public int Version { get; set; }
            public int Type { get; set; }

            public abstract ulong Value { get; }
            
            public static Packet Parse(ref string binaryData)
            {
                var version = Convert.ToInt32(binaryData.Substring(0, 3),2);
                var type = Convert.ToInt32(binaryData.Substring(3, 3),2);

                Packet newPacket;
                if (type == 4)
                {
                    newPacket = new LiteralPacket();
                }
                else
                {
                    newPacket = new OperatorPacket();
                }
            
                binaryData = newPacket.ParsePacket(binaryData.Substring(6));

                newPacket.Version = version;
                newPacket.Type = type;

                return newPacket;
            }
            
            public abstract string ParsePacket(string data);
        }

        [DebuggerDisplay("Literal: {Value}")]
        public class LiteralPacket : Packet
        {
            private ulong value;

            public override ulong Value => this.value;

            public override string ParsePacket(string data)
            {
                var lastGroup = false;
                string number = "";
                while (!lastGroup)
                {
                    var groupData = data.Substring(0, 5);
                    data = data.Substring(5);

                    if (groupData[0] == '0')
                    {
                        lastGroup = true;
                    }

                    number += groupData.Substring(1);
                }

                this.value = Convert.ToUInt64(number, 2);
                
                return data;
            }
        }

        [DebuggerDisplay("Operator {Type}: {SubPackets.Count} children")]
        public class OperatorPacket : Packet
        {
            public List<Packet> SubPackets { get; } = new List<Packet>();
            
            public override string ParsePacket(string data)
            {
                var lengthType = data[0];
                data = data.Substring(1);

                if (lengthType == '0')
                {
                    var bitLength = Convert.ToInt32(data.Substring(0, 15), 2);
                    data = data.Substring(15);

                    var subPacketsData = data.Substring(0, bitLength);
                    data = data.Substring(bitLength);

                    while (subPacketsData != string.Empty)
                    {
                        this.SubPackets.Add(Parse(ref subPacketsData));
                    }
                }
                else
                {
                    var packets = Convert.ToInt32(data.Substring(0, 11), 2);
                    data = data.Substring(11);

                    for (int i = 0; i < packets; i++)
                    {
                        this.SubPackets.Add(Parse(ref data));
                    }
                }
                
                return data;
            }

            public override ulong Value
            {
                get
                {
                    switch (this.Type)
                    {
                        case 0:
                            return this.SubPackets.Aggregate(0ul, (t, c) => t + c.Value);
                        case 1:
                            return this.SubPackets.Aggregate(1ul, (t, c) => t * c.Value);
                        case 2:
                            return this.SubPackets.Aggregate(ulong.MaxValue, (t, c) => Math.Min(t, c.Value));
                        case 3:
                            return this.SubPackets.Aggregate(0ul, (t, c) => Math.Max(t, c.Value));
                        case 5:
                            return this.SubPackets[0].Value > this.SubPackets[1].Value ? 1ul : 0ul;
                        case 6:
                            return this.SubPackets[0].Value < this.SubPackets[1].Value ? 1ul : 0ul;
                        case 7:
                            return this.SubPackets[0].Value == this.SubPackets[1].Value ? 1ul : 0ul;
                        default:
                            throw new ArgumentOutOfRangeException();
                    }
                }
            }
        }

        
        
        public void Part2()
        {          
            var data = "04005AC33890";
            data = File.ReadAllLines("Data/Day16/main.txt").First();

            var databin = "";
            for (var i = 0; i < data.Length; i+=2)
            {
                databin += Convert.ToString(Convert.ToInt32("" + data[i] + data[i + 1], 16), 2).PadLeft(8, '0');
            }

            var packet = Packet.Parse(ref databin);

            Console.WriteLine(packet.Value);
          
        }
    }
}