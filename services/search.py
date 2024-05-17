def count_character(character):
    dynasties = ['ming', 'qing', 'song', 'tang']
    counts = []

    for dynasty in dynasties:
        with open(f'corpus/{dynasty}/{dynasty}.txt', 'r', encoding='utf8') as file:
            contents = file.read()
        
        counts.append(contents.count(character))
        
    return counts