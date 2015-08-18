def way_2_long(words):
    for index, word in enumerate(words):
        if len(word) > 10:
            abbrev = '{}{}{}'.format(word[0], len(word) - 2, word[-1])
            words[index] =  abbrev
    return words

def test_way_2_long():
    result = way_2_long(['localization', 'internationalization', 'word'])
    assert result == ['l10n', 'i18n', 'word']
