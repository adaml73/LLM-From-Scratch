import re

text = "Hello, world. This, is a test."
result = re.split(r'([,.:?_!"()\']|--|\s)', text)
result = [item.strip() for item in result if item.strip()]
print(result)

print("now with example text")

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

real_result = re.split(r'([,.:?_!"()\']|--|\s)', raw_text)
real_result = [item.strip() for item in real_result if item.strip()]
print(real_result)