def find_occurrences(text, pattern):
    '''
    finds how many times does pattern occurs in text, including overlapping occurences
    '''
    if not text or not pattern:
        return (False, 0, [])
    
    pattern_length = len(pattern)
    occurrences = [i for i in range(len(text) - pattern_length + 1) 
                   if text[i:i + pattern_length] == pattern]
    
    return (bool(occurrences), len(occurrences), occurrences)