# Substring Search Algorithm Performance Report

## Overview

This report presents a comparative performance analysis of three well-known substring search algorithms implemented in Python:

Knuth-Morris-Pratt (KMP)

Boyer-Moore

Rabin-Karp

Each algorithm was tested on two different articles (article1 and article2) and evaluated for two cases:

A real substring (exists in the text)

A fake substring (does not exist in the text)

The execution time for each test was measured using Python’s timeit module.

## Test Results

📘 Article 1

🔍 Pattern

⏱️ KMP

⚡ Boyer-Moore

🔣 Rabin-Karp

✅ Real Substring

0.001843s

⭐ 0.000502s

0.005820s

❌ Fake Substring

0.068129s

⭐ 0.023279s

0.241063s

📗 Article 2

🔍 Pattern

⏱️ KMP

⚡ Boyer-Moore

🔣 Rabin-Karp

✅ Real Substring

0.151614s

⭐ 0.058285s

0.383087s

❌ Fake Substring

0.165225s

⭐ 0.035184s

0.305916s

## Conclusions

Boyer-Moore algorithm consistently outperformed the others across all tests.

It was the fastest for both real and fake substrings in both articles.

Its efficiency is especially notable in long texts and non-matching cases, due to its ability to skip sections of the text.

KMP performed reasonably well, especially for real substrings, but was slower than Boyer-Moore in every case.

Rabin-Karp was the slowest across all tests, particularly for fake substrings. This is likely due to the additional hash computation overhead and increased chance of collisions.

## Final Verdict

Best Performing Algorithm: Boyer-Moore

Recommended Use: When performance and speed are critical, especially in large texts and scenarios where the pattern might not be found.
