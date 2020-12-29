import sys
print("This script will return DNA lenght and AA sequence lenght")


#Strip the \n char in the end of each line:
def fix_input(target):
    total_seq = ''
    for line in target:
        lines = str(line).rstrip()
        total_seq += lines
        target = total_seq
    return target

print("Paste your DNA sequence: ( ctrl+shift+v to paste, ctrl+d end the input.)")
dna_input = sys.stdin.readlines()
print("DNA input has ended")

print("Paste your AA sequence: ( ctrl+shift+v to paste, ctrl+d end the input.)")

aa_input = sys.stdin.readlines()
print("AA input has ended")

dna_input = fix_input(dna_input)

aa_input = fix_input(aa_input)

print(f"DNA sequence lenght is {len(dna_input)} and AA sequence lenght is {len(aa_input)}!")
