import random
import time
import os

from gale_shapely import parse_input, gale_shapely, write_out
from verifier import verifier
from runtime_analysis import create_data_plot

sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 640, 768, 896, 1024, 1280, 1536, 1792, 2048]

def write_input_file(n, path):
    hospitals = []
    for i in range(n):
        row = random.sample(range(1, n + 1), n)
        hospitals.append(row)
    
    students = []
    for i in range(n):
        row = random.sample(range(1, n + 1), n)
        students.append(row)

    lines = [str(n)]
    for row in hospitals:
        lines.append(" ".join(str(n) for n in row))
    for row in students:
        lines.append(" ".join(str(n) for n in row))

    with open(path, "w") as f:
        f.write("\n".join(lines))

def main():
    random.seed(0)

    data_dir = "data"
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    gs_times = []
    verify_times = []

    for n in sizes:
        in_path = f"{data_dir}/{n}.in"
        out_path = f"{data_dir}/{n}.out"

        write_input_file(n, in_path)

        start = time.perf_counter()
        hospitals, applicants = parse_input(in_path)
        matched = gale_shapely(hospitals, applicants)
        write_out(matched, out_path)
        gs_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        verifier(in_path, out_path)
        verify_times.append(time.perf_counter() - start)

    create_data_plot(sizes, gs_times, verify=False)
    create_data_plot(sizes, verify_times, verify=True)

if __name__ == "__main__":
    main()