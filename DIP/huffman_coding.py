import heapq
from collections import Counter

# Input data
text = "ABRACADABRA"

# Calculate character frequencies
frequency = Counter(text)

# Build Huffman tree
heap = [[freq, [char, ""]] for char, freq in frequency.items()]
heapq.heapify(heap)

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    for pair in left[1:]:
        pair[1] = "0" + pair[1]

    for pair in right[1:]:
        pair[1] = "1" + pair[1]

    heapq.heappush(
        heap, [left[0] + right[0]] + left[1:] + right[1:]
    )

# Generate Huffman codes
huffman_codes = dict(sorted(heap[0][1:]))

# Encode the text
encoded_text = "".join(huffman_codes[ch] for ch in text)

# Decode the encoded text
reverse_codes = {code: char for char, code in huffman_codes.items()}
decoded_text = ""
temp = ""

for bit in encoded_text:
    temp += bit
    if temp in reverse_codes:
        decoded_text += reverse_codes[temp]
        temp = ""

# Display results
print("Original Text:", text)
print("Character Frequencies:", frequency)
print("Huffman Codes:", huffman_codes)
print("Encoded Text:", encoded_text)
print("Decoded Text:", decoded_text)
