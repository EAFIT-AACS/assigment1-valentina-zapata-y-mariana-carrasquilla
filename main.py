import os

def read_input_from_file():
    filename = os.path.join(os.path.dirname(__file__), "dfa_input.txt")
    with open(filename, "r") as file:
        lines = file.readlines()
    
    index = 0
    c = int(lines[index].strip())
    index += 1
    cases = []
    
    for _ in range(c):
        n = int(lines[index].strip())
        index += 1
        alphabet = lines[index].strip().split()
        index += 1
        final_states = set(map(int, lines[index].strip().split()))
        index += 1
        transitions = [list(map(int, lines[i].strip().split())) for i in range(index, index + n)]
        index += n
        cases.append((n, alphabet, final_states, transitions))
    
    return cases

def find_equivalent_states(n, final_states, transitions):
    distinguishable = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if (i in final_states) != (j in final_states):
                distinguishable[i][j] = True
    
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                if not distinguishable[i][j]:
                    for symbol_idx in range(len(transitions[i])):
                        t1, t2 = transitions[i][symbol_idx], transitions[j][symbol_idx]
                        if t1 != t2 and distinguishable[min(t1, t2)][max(t1, t2)]:
                            distinguishable[i][j] = True
                            changed = True
                            break
    
    equivalent_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not distinguishable[i][j]:
                equivalent_pairs.append((i, j))
    
    return equivalent_pairs

def main():
    cases = read_input_from_file()
    
    for n, alphabet, final_states, transitions in cases:
        equivalent_states = find_equivalent_states(n, final_states, transitions)
        print(" ".join(f"({p},{q})" for p, q in sorted(equivalent_states)))

if __name__ == "__main__":
    main()  
