def search4letters(phrase='Let`s go!', letters='aeoi,!'):
    return set(phrase).intersection(set(letters))