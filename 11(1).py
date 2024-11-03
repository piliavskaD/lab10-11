import csv

with open("english_text.txt", "r") as file:
    text = file.read().replace(",", "")
    words = text.lower().strip().split()

first_four_words = words[:4]
print("Перші 4 слова:", first_four_words)

d = {}
for i in first_four_words:
    d[i] = d.get(i, 0) + words.count(i)

print("Частота слів:", d) 

with open("words.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Word", "Frequency"])
    for word, count in d.items():
        writer.writerow([word, count])
