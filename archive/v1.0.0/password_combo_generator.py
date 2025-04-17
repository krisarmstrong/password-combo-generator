from itertools import permutations, product

# Original password
password = "kja!!2008"

# Generate all combinations of upper and lower case for the letters
def generate_combinations(password):
    chars = [(char.lower(), char.upper()) if char.isalpha() else (char,) for char in password]
    return [''.join(combination) for combination in product(*chars)]

# Generate all permutations of each combination
def generate_permutations(combinations):
    permuted_passwords = set()
    for combination in combinations:
        perms = permutations(combination)
        for perm in perms:
            permuted_passwords.add(''.join(perm))
    return permuted_passwords

# Get all combinations
combinations = generate_combinations(password)

# Get all permutations
permutations_set = generate_permutations(combinations)

# Print all permutations
for perm in permutations_set:
    print(perm)