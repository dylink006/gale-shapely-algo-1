import sys
import queue

class Hospital:
    id: None
    prefs = [],
    matched_applicant = None,
    highest_proposal = None

    def __init__(self, id, prefs):
        self.id = id
        self.prefs = prefs

def parse_input(input_path=None):
    if input_path:
        input_lines = []
        for line in open(input_path).read().splitlines():
            if line.strip():
                input_lines.append(line.strip())
    else:
        input_lines = []
        try:
            n = int(input().strip())
        except ValueError:
            raise ValueError("First input must be an integer.")
        input_lines.append(str(n))
        for i in range(2 * n):
            line = input().strip()
            prefs = line.split()
            if len(prefs) != n:
                raise ValueError("Each preference line bust have n integers")
            input_lines.append(line)
    
    try:
        n = int(input_lines[0])
    except ValueError:
        raise ValueError("First line must be an integer.")
    
    if len(input_lines) != (2 * n) + 1:
        raise ValueError("Wrong number of lines.")
    
    for line in input_lines[1:]:
        if len(line.split()) != n:
            raise ValueError("Each preference line must have n integers separated by spaces.")

    hospitals = {}
    applicants = {}

    for i in range(n):
        hospital_prefs = [int(pref) for pref in input_lines[i + 1].split()]
        applicant_prefs = [int(pref) for pref in input_lines[i + n + 1].split()]
        hospitals[i + 1] = hospital_prefs
        applicants[i + 1] = applicant_prefs

    return hospitals, applicants


def gale_shapely(hospitals, applicants):
    applicant_ranks = {}
    for applicant, pref in applicants.items():
        hospital_to_rank = {}
        for i, hospital in enumerate(pref):
            hospital_to_rank[hospital] = i
        applicant_ranks[applicant] = hospital_to_rank

    unmatched_hospitals = queue.Queue()
    for h, plist in hospitals.items():
        hospital_to_add = Hospital(h, plist)
        unmatched_hospitals.put(hospital_to_add)

    matched_applicants = {}
    while unmatched_hospitals.qsize() > 0:
        curr_hospital = unmatched_hospitals.get()

        if curr_hospital.highest_proposal != None:
            start_index = 1 + curr_hospital.highest_proposal
        else:
            start_index = 0

        for i, a in enumerate(curr_hospital.prefs[start_index:]):
            if a not in matched_applicants:
                curr_hospital.matched_applicant = a
                curr_hospital.highest_proposal = i + start_index
                matched_applicants[a] = curr_hospital
                break

            if applicant_ranks[a][curr_hospital.id] < applicant_ranks[a][matched_applicants[a].id]:
                unmatched_hospitals.put(matched_applicants[a])
                curr_hospital.matched_applicant = a
                curr_hospital.highest_proposal = i + start_index
                matched_applicants[a] = curr_hospital
                break
    return matched_applicants

def write_out(matched_applicants, output_path):
    matches = []
    for a, h in matched_applicants.items():
        matches.append((h.id, a))
    matches.sort()
    lines = []
    for h, a in matches:
        curr_line = f"{h} {a}"
        lines.append(curr_line)
    with open(output_path, "w") as f:
        f.write("\n".join(lines))