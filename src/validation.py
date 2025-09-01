import re
import pandas as pd


def validate_data(df: pd.DataFrame, rules: list) -> dict:
    """
    Validate data against rules defined in config.
    Returns a dictionary of issues found.
    """
    print("🔎 Starting data validation...")
    issues = {}

    for rule in rules:
        col = rule.get("column")
        if col not in df.columns:
            print(f"⚠️ Column '{col}' not found, skipping validation")
            continue

        col_issues = []

        # Check min
        if "min" in rule:
            invalid_rows = df[df[col] < rule["min"]]
            if not invalid_rows.empty:
                col_issues.append(f"{len(invalid_rows)} values below {rule['min']}")

        # Check max
        if "max" in rule:
            invalid_rows = df[df[col] > rule["max"]]
            if not invalid_rows.empty:
                col_issues.append(f"{len(invalid_rows)} values above {rule['max']}")

        # Check regex
        if "regex" in rule:
            pattern = re.compile(rule["regex"])
            invalid_rows = df[~df[col].astype(str).str.match(pattern)]
            if not invalid_rows.empty:
                col_issues.append(f"{len(invalid_rows)} values do not match regex {rule['regex']}")

        # Check unique
        if rule.get("unique", False):
            duplicates = df[df.duplicated(col, keep=False)]
            if not duplicates.empty:
                col_issues.append(f"{len(duplicates)} duplicate values found")

        if col_issues:
            issues[col] = col_issues
            print(f"❌ Validation issues in '{col}': {col_issues}")

    if not issues:
        print("✅ No validation issues found")

    return issues
