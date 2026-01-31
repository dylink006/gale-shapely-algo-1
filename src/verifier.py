def read_input(path):
    lines = []
    for line in open(path).read().splitlines():
        if line.strip():
            lines.append(line.strip())
    
    try:
        n = int(lines[0])
    except ValueError:
        raise ValueError("first line of input must be an integer")

    if len(lines) != 1 + (2 * n):
        raise ValueError("wrong number of lines")

    hospitals = {}
    applicants = {}

    for i in range(n):
        hospital_prefs = lines[i + 1].split()
        applicant_prefs = lines[i + 1 + n].split()
        if len(hospital_prefs) != n or len(applicant_prefs) != n:
            raise ValueError("each preference line must have n integers")
        
        hospitals[i + 1] = [int(p) for p in hospital_prefs]
        applicants[i + 1] = [int(p) for p in applicant_prefs]

    return n, hospitals, applicants

def read_output(path, n):
    lines = []
    for line in open(path).read().splitlines():
        if line.strip():
            lines.append(line.strip())
    
    if len(lines) != n:
        raise ValueError("Wrong number of output lines")

    hospitals_to_applicants = {}
    applicants_to_hospitals = {}

    for line in lines:
        matching = line.split()
        if len(matching) != 2:
            raise ValueError("each output line must have 2 integers")

        h = int(matching[0])
        a = int(matching[1])
        if h < 1 or h > n:
            raise ValueError("hospital ids out of range")
        elif a < 1 or a > n:
            raise ValueError("applicant ids out of range")

        if h in hospitals_to_applicants:
            raise ValueError(f"hospital {h} appears more than once")
        if a in applicants_to_hospitals:
            raise ValueError(f"applicant {a} appears more than once")
        
        hospitals_to_applicants[h] = a
        applicants_to_hospitals[a] = h
    
    return hospitals_to_applicants, applicants_to_hospitals

def verifier(input_path, output_path):
    try:
        n, hospitals, applicants = read_input(input_path)
        hospitals_to_applicants, applicants_to_hospitals = read_output(output_path, n)

        applicant_ranks = {}
        for a, prefs in applicants.items():
            ranking = {}
            for i, h in enumerate(prefs):
                ranking[h] = i
            applicant_ranks[a] = ranking

        hospital_ranks = {}
        for h, pref in hospitals.items():
            ranking = {}
            for i, a in enumerate(pref):
                ranking[a] = i
            hospital_ranks[h] = ranking

        for a in range(1, n + 1):
            if a not in applicants_to_hospitals:
                raise ValueError(f"Applicant {a} unmatched")
        
        for h in range(1, n + 1):
            if h not in hospitals_to_applicants:
                raise ValueError(f"Hospital {h} unmatched")
        
        for a, assigned_h in applicants_to_hospitals.items():
            assigned_rank = applicant_ranks[a][assigned_h]
            for preferred_h, rank in applicant_ranks[a].items():
                if rank >= assigned_rank:
                    continue
                assigned_a = hospitals_to_applicants[preferred_h]
                if hospital_ranks[preferred_h][a] < hospital_ranks[preferred_h][assigned_a]:
                    print("UNSTABLE: blocking pair found: Applicant {a} prefers hospital {preferred_h} over {assigned_h} & hospital {preferred_h} prefers applicant {a} over {assigned_a}")
        print("VALID STABLE")
    except ValueError as e:
        print(f"INVALID: {e}")