def verifier(applicant_ranks, matched_applicants, hospital_prefs):
    if len(matched_applicants) != len(applicant_ranks):
        print("INVALID: not every applicant matched")
        return
    
    matched_hospitals = {}
    for a, h in matched_applicants.items():
        if h is None:
            print(f"INVALID: applicant {a} unmatched")
            return
        elif h.matched_applicant != a:
            print(f"INVALID: mismatch for hospital {h.id}")
            return
        elif h.id in matched_hospitals:
            print(f"INVALID: hospital {h.id} appears more than once")
            return
        matched_hospitals[h.id] = a
    
    if len(matched_hospitals) != len(matched_applicants):
        print("INVALID: number of matched applicants does not match number of matched hospitals")

    hospital_ranks = {}
    for hospital, pref in hospital_prefs.items():
        applicant_to_rank = {}
        for i, a in enumerate(pref):
            applicant_to_rank[a] = i
        hospital_ranks[hospital] = applicant_to_rank

    for a, h in matched_applicants.items():
        current_rank = applicant_ranks[a][h]

        for id, rank in applicant_ranks[a].items():
            if rank >= current_rank:
                continue

            matched_applicant = matched_hospitals[id]
            if matched_applicant is None:
                print(f"INVALID: hospital {id} is unmatched")
                return
            
            if hospital_ranks[id][a] < hospital_ranks[id][matched_applicant]:
                print(f"UNSTABLE: blocking pair found: Applicant {a} prefers hospital {id} over {h} & hospital {id} prefers applicant {a} over {matched_applicant}")
                return

    print("OK: matching is valid and stable")     
    return