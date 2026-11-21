
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().split()

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts

def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]

result = frequencies(calls, STOP)

print("Word frequencies:", result)
print("Top 3 words:", top(result, 3))

# Group complaints by district
complaints = {
    "Chennai": ["Seeds delayed", "Fertiliser shortage"],
    "Madurai": ["Water shortage", "Crop disease"],
    "Salem": ["Seeds not received"]
}

districts = {}

for district, texts in complaints.items():
    districts.setdefault(district, []).extend(texts)

print("District complaints:", districts)
