import sys
from gale_shapely import parse_input, gale_shapely, write_out
from verifier import verifier

args = sys.argv[1:]

if len(args) == 0:
    print("Usage:\n python3 run.py -gs [input_file]\n python3 run.py -gs -v [input file]\n python3 run.py -v input_file output_file")
    sys.exit(0)

if args[0] == "-gs":
    input_path = None
    for a in args[1:]:
        if a != "-v":
            input_path = a
            break
    
    if input_path:
        hospitals, applicants = parse_input(input_path)
        input_path_parts = input_path.split(".")
        if len(input_path_parts) > 1:
            output_path = ".".join(input_path_parts[:-1]) + ".out"
        else:
            output_path = input_path + ".out"
    else:
        hospitals, applicants = parse_input()
        output_path = "output.out"

    matched = gale_shapely(hospitals, applicants)
    write_out(matched, output_path)

    if "-v" in args:
        if not input_path:
            print("No input file given for verifier.")
        else:
            verifier(input_path, output_path)
elif args[0] == "-v":
    if len(args) < 3:
        print("Usage:\n python3 run.py -v input_file output_file")
        sys.exit(0)
    verifier(args[1], args[2])
else:
    print("Usage:\n python3 run.py -gs [input_file]\n python3 run.py -gs -v [input file]\n python3 run.py -v input_file output_file")