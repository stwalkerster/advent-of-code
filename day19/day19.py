from termcolor import colored
import re


class Item:
    def __init__(self, groups):
        self.x = int(groups["x"])
        self.m = int(groups["m"])
        self.a = int(groups["a"])
        self.s = int(groups["s"])

    def __repr__(self):
        return f"[{self.x}/{self.m}/{self.a}/{self.s}]"

    def value(self):
        return self.x + self.m + self.a + self.s

class Workflow:
    def __init__(self, groups, rule_pattern):
        self.label = groups["label"]
        self.fallback = groups["final"]
        self.rules = [Rule(rule_pattern.match(r).groupdict()) for r in groups["rules"].split(",")]

        if len(self.rules) == 1 and self.rules[0].target == self.fallback:
            self.rules = []

    def __repr__(self):
        return f"[{self.label}: {len(self.rules)} rules -> {self.fallback}]"

    def get_result(self, item: Item) -> str:
        for rule in self.rules:
            if rule.match(item):
                return rule.target

        return self.fallback

class Rule:
    def __init__(self, groups):
        self.attribute = groups["attribute"]
        self.value = int(groups["value"])
        self.operator = groups["operator"]
        self.target = groups["target"]

    def __repr__(self):
        return f"[{self.attribute} {self.operator} {self.value} -> {self.target}]"

    def match(self, item: Item) -> bool:
        target_value = 0
        if self.attribute == "x":
            target_value = item.x
        elif self.attribute == "m":
            target_value = item.m
        elif self.attribute == "a":
            target_value = item.a
        elif self.attribute == "s":
            target_value = item.s
        else:
            raise Exception("Unknown target attr")

        if self.operator == "<":
            return target_value < self.value
        elif self.operator == ">":
            return target_value > self.value
        else:
            raise Exception("Unknown operation")


def part1(input_file):
    data = [line for line in open(input_file).read().split('\n\n') if line != ""]

    workflow_pattern = re.compile(r"^(?P<label>[a-z]+)\{(?P<rules>.*?),(?P<final>[a-z]+|R|A)}$")
    item_pattern = re.compile(r"^\{x=(?P<x>[0-9]+),m=(?P<m>[0-9]+),a=(?P<a>[0-9]+),s=(?P<s>[0-9]+)}$")
    rule_pattern = re.compile(r"^(?P<attribute>[xmas])(?P<operator>[<>])(?P<value>[0-9]+):(?P<target>A|R|[a-z]+)$")

    workflows = {w.label: w for w in [Workflow(workflow_pattern.match(d).groupdict(), rule_pattern) for d in data[0].split('\n') if d != ""]}
    items = [Item(item_pattern.match(d).groupdict()) for d in data[1].split('\n') if d != ""]

    accepted = []
    for i in items:
        next_wf = "in"
        while next_wf not in ("A", "R"):
            next_wf = workflows[next_wf].get_result(i)

        if next_wf == 'A':
            accepted.append(i)

    print(sum([i.value() for i in accepted]))

def part2(input_file):
    data = [line for line in open(input_file).read().split('\n') if line != ""]


if __name__ == '__main__':
    part1("input.txt")
