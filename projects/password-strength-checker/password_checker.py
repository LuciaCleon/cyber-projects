#!/usr/bin/env python3
import re
from getpass import getpass

def score_password(pw: str) -> tuple[int, list[str]]:
    tips = []
    score = 0

    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters (12+ is better).")

    if re.search(r"[A-Z]", pw):
        score += 1
    else:
        tips.append("Add an uppercase letter (A-Z).")

    if re.search(r"[a-z]", pw):
        score += 1
    else:
        tips.append("Add a lowercase letter (a-z).")

    if re.search(r"\d", pw):
        score += 1
    else:
        tips.append("Add a number (0-9).")

    if re.search(r"[^\w\s]", pw):
        score += 1
    else:
        tips.append("Add a symbol (e.g., ! @ # $).")

    # Basic common-pattern warnings
    common_patterns = ["password", "1234", "qwerty", "letmein", "admin"]
    if any(p in pw.lower() for p in common_patterns):
        tips.append("Avoid common words/patterns (e.g., 'password', '1234').")
        score = max(0, score - 1)

    return score, tips

def label(score: int) -> str:
    if score <= 2:
        return "WEAK"
    if score <= 4:
        return "OK"
    return "STRONG"

def main():
    print("Password Strength Checker (local use only)")
    pw = getpass("Enter a password to check: ")
    score, tips = score_password(pw)

    print(f"\nResult: {label(score)} (score {score}/6)")
    if tips:
        print("\nImprove it by:")
        for t in tips:
            print(f"- {t}")
    else:
        print("\nNice! This password meets strong basic criteria.")

if __name__ == "__main__":
    main()
