OK, this is an odd one.

I threw the data into GraphViz to visualise the connectivity
between modules. That showed me it's in four rough groups of
chained flipflops that looks kinda-but-not-quite like a binary
counter.

My part 2 code iterates over one of the modules to get a sense
of what it does, and to my surprise it counts 4001 distinct
values before resetting, not the 4096 I'd expect from a 12-bit
counter.

I then did some by-hand analysis and figured out that any module
which outputs to the central conjunction node (except the first)
will be set the iteration before a reset. Working that out as a
binary number for my first module gives 4000:

```
               i iiiii
          ooooo o    o 
ks->gm : b111110100000 = d4000
```

Note how the lowest digit both inputs and outputs - I treated
this as zero due to how the reset works. The reset sends a 1 to
every flipflop that's not set, then one more 1 to the lowest
digit to force a rollover and reset to zero.

Calculating the rest in the same way gave me 3910, 4012, and 3850

Adding 1 to each (to get the total values available rather than 
the zero-indexed maximum value), then throwing them into an
lcm(...) calculation on Wolfram Alpha revealed the solution.
