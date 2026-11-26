LINE = "I am out of the office and also out of patience, so your email has joined a queue that is currently longer than my vacation."

# The entry must be exactly one line of 1-140 characters.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
assert "\n" not in LINE

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

# Read it back: a silent short write must fail loudly instead of
# passing the gate with a stale or truncated file.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt does not match LINE after write"
