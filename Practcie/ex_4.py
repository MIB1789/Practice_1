from collections import Counter

text = input("Введите текст: ").lower()

char_counts = Counter(text)

top_3 = char_counts.most_common(3)

print("3 самых частых символа:")
for char, count in top_3:
    print(f"Символ '{char}' встречается {count} раз(а)")
