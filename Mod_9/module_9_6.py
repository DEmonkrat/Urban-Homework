def all_variants(text):
    start_chr = 0
    for width in range(1, len(text) + 1):
        for start_chr in range(len(text) - width + 1):
            yield text[start_chr:start_chr + width]


a = all_variants('text')
for i in a:
    print(i)
