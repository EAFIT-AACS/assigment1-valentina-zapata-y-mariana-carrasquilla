# DFA Minimization - Assignment 1

## Student Information
**Name:** Mariana Carrasquilla Botero

**Name:** Valentina Zapata Grajales 

**Class Number:** 7309  

## System and Tools Used
- **Operating System:** Windows 10 Pro
- **Programming Language:** Python 3.11
- **Development Environment:** VS Code

## Description
This is a program to minimize Deterministic Finite Automata (DFA) using the table-filling method from Kozen 1997, Lecture 14. The program finds equivalent states and prints them.

## Input Format
The input is read from a file named `dfa_input.txt` and follows this structure:
1. An integer `c > 0`, indicating the number of test cases.
2. For each case:
   - An integer `n > 0`, the number of states in the DFA.
   - A single line containing the alphabet symbols, separated by spaces.
   - A single line with the final states, separated by spaces.
   - `n` lines, each representing the state transition table (one row per state).

### Example Input:
```
4  
6  
a b  
1 2 5  
0 1 2  
1 3 4  
2 4 3  
3 5 5  
4 5 5  
5 5 5  
6  
a b  
3 4 5  
0 1 2  
1 3 4  
2 4 3  
3 5 5  
4 5 5  
5 5 5  
6  
a  
1 4  
0 1  
1 2  
2 3  
3 4  
4 5  
5 0  
4  
a b  
0 1  
0 1 2  
1 1 2  
2 3 1  
3 3 3
```

## Output Format
For each case, the program prints the **equivalent state pairs** in **lexicographical order**, separated by spaces.

### Example Output:
```
(1,2) (3,4)
(1,2) (3,4) (3,5) (4,5)
(0,3) (1,4) (2,5)
(0,1)
```
If no states are equivalent, it prints an empty line.

## How to run in VS Code
1. Open VS Code and navigate to the folder containing your script and `dfa_input.txt.`
2. Open the script `(minimization.py)` in the editor.
3. Click on the Run Button at the top right of the VS Code window.
4. The output will appear in the terminal at the bottom of VS Code.

## Algorithm Explanation
The program follows these steps:
1. **Read Input:** Extracts DFA data from file.
2. **Initialize Table:** Creates a table to track **distinguishable** state pairs.
3. **Mark Final vs Non-final:** Marks pairs with different finality.
4. **Iterate Until Stable:** Marks states based on transitions.
5. **Extract Equivalent States:** Identifies unmarked state pairs as **equivalent**.
6. **Print Results:** Outputs the pairs in lexicographical order.

 
## References
Kozen, Dexter C. (1997). *Automata and Computability*. Springer-Verlag. ISBN: 0387949070.  
Dr. Insightful. (2024, 3 noviembre). DFA minimization: Table filling method explained [Vídeo]. YouTube. https://www.youtube.com/watch?v=7F4zI_qnPhk
