# Programming Assignment 1: Stable Matching (Gale-Shapley)

This repo implements the Gale-Shapley stable matching algorithm for hospitals and students. It also includes a verifier and a benchmark script for scalability plots.

## Author

Dylan McGarry (UFID: 66318896)

## Input Format

The input describes complete strict rankings. All preferences separated by spaces and on the same line in most-preferred to least-preferred order.
```
n
<hospital 1 preferences>
<hospital 2 preferences>
...
<hospital n preferences>
<student 1 preferences>
<student 2 preferences>
...
<student n preferences>
```

- n is the number of hospitals and students.
- Each preference line has exactly n integers.
- Hospitals and students are labeled 1..n.

Example (n = 3):
```
3
1 2 3
2 3 1
2 1 3
2 1 3
1 2 3
1 2 3
```

## Output Format

Output is written as pairs, one per line, in the form:
```
hospita;_id applicant_id
```
Example:
```
1 2
2 3
3 1
```

## Setup

Before running the benchmark/plotting parts, make sure matplotlib is installed.

```
python3 -m pip install matplotlib
```

## Running

To run Gale-Shapely on an input file:
```
python3 run.py -gs input.in
```
This produces input.out in the current directory (same name with the extension removed). This works based on relative path so if you want to test an input file that lives in the data direcotry the input.in parameter in the CLI would say data/[input.in]
If you would like to run without an input file and put the input into the command line, you will input all the lines that input.in would have (with preferences separated by spaces) it will write to output.out with you only needing to type the following:
```
python3 run.py -gs
```
If you want to run Gale-Shapley with an input file and verify the result, run
```
python3 run.py -gs -v input.in
```
To verify the validity and stability of an input/output file pair, run the following:
```
python3 run.py -v input.in output.out
```
The verifier will read both files and print whether the matching is valid and stable

## Benchmark

benchmark.py generates random test instances, runs Gale-Shapley, then runs the verifier. It plots runtime vs n.

```
python3 benchmark.py
```

Generated input/output files are written to ./data.
Plots are saved as: gs_chart.png and verifier_chart.png.

## Files

gale_shapely.py contains the Gale-Shapley implementation and parsing and output writing
verifier.py is the file-based verifier
run.py is the CLI wrapper for running Gale-Shapley, the solver, and the verifier
benchmark.py handles data generation and runtime benchmarking
runtime_analysis.py is a plot generator
