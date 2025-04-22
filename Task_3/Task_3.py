import timeit

# KMP Search
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # If characters match, increment length and assign to lps[i]
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # If there was a previous match, fall back to the previous prefix length
                length = lps[length - 1]
            else:
                # No match found, set lps[i] to 0
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    # Preprocess the pattern to generate the lps array
    lps = compute_lps(pattern)

    i = j = 0 # i - index for main_string, j - index for pattern


    while i < N:
        if pattern[j] == main_string[i]:
            # If characters match, move both pointers forward
            i += 1
            j += 1
        elif j != 0:
            # If mismatch after some matches, use lps to avoid unnecessary comparisons
            j = lps[j - 1]
        else:
            # If no matches, move main string pointer forward
            i += 1

        if j == M:
            # Match found, return the starting index of the match in main_string
            return i - j

    return -1 


# Boyer-Moore Search
def build_shift_table(pattern):
    """Create a shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)

    # Set shift values for all characters except the last one
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    # Set default shift for the last character
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0  # Start index for scanning the text

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Start comparing from the end of the pattern

        # Compare pattern from end to beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i  # Match found at index i

        # Mismatch: shift based on bad character rule
        mismatch_char = text[i + len(pattern) - 1]
        i += shift_table.get(mismatch_char, len(pattern))

    return -1  # Pattern not found

# Rabin-Karp Search
def polynomial_hash(s, base=256, modulus=101):
    """
    Returns the polynomial hash of string s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Lengths of the main string and the substring to search for
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Base number for hashing and modulus
    base = 256 
    modulus = 101  
    
    # Hash value for the substring and the current window in the main string
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    # Precomputed value for rolling hash recalculation
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    # Iterate through the main string
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

# Download text
def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
    
text1 = load_text('article1.txt')
text2 = load_text('article2.txt')

# Substrings for search
real_substring = "алгоритми"
fake_substring = "fakesubstring"

# Function to measure time
def time_search(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=10)

# Test
algorithms = {
    "KMP": kmp_search,
    "Boyer-Moore": boyer_moore_search,
    "Rabin-Karp": rabin_karp_search,
}

texts = {
    "Article1": text1,
    "Article2": text2
}

patterns = {
    "Real Substring": real_substring,
    "Fake Substring": fake_substring,
}

print("Performance Results:\n")
for text_name, text_content in texts.items():
    for pattern_name, pattern_value in patterns.items():
        print(f"Text: {text_name}, Pattern: {pattern_name}")
        for alg_name, alg_func in algorithms.items():
            time_taken = time_search(alg_func, text_content, pattern_value)
            print(f"{alg_name}: {time_taken:.6f} seconds")
        print("-" * 50)