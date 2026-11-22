from collections import Counter

# Input data
text = "ABRACADABRA"

# Calculate character probabilities
frequency = Counter(text)
total = len(text)
probability = {
    char: frequency[char] / total
    for char in frequency
}

# Build cumulative probability intervals
low_range = {}
high_range = {}
cumulative = 0.0

for char in sorted(probability):
    low_range[char] = cumulative
    cumulative += probability[char]
    high_range[char] = cumulative

# Arithmetic encoding
low = 0.0
high = 1.0

for char in text:
    current_range = high - low
    high = low + current_range * high_range[char]
    low = low + current_range * low_range[char]

encoded_value = (low + high) / 2

# Arithmetic decoding
decoded_text = ""
low = 0.0
high = 1.0

for _ in range(len(text)):
    value = (encoded_value - low) / (high - low)

    for char in sorted(probability):
        if low_range[char] <= value < high_range[char]:
            decoded_text += char

            current_range = high - low
            high = low + current_range * high_range[char]
            low = low + current_range * low_range[char]
            break

# Display results
print("Original Text:", text)
print("Character Frequencies:", frequency)
print("Probabilities:", probability)
print("Low Intervals:", low_range)
print("High Intervals:", high_range)
print("Encoded Value:", encoded_value)
print("Decoded Text:", decoded_text)
