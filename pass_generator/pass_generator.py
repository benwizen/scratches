import random


def rand_pass():
    with open('./rand_verbs') as verbs:
        verb_list = [verb[:-1] for verb in verbs]

    with open('./rand_nouns') as nouns:
        noun_list = [noun[:-1] for noun in nouns]

    who_list = ['I', 'She', 'He', 'We', 'You', 'They']
    who = random.sample(who_list, 1)
    verb = random.sample(verb_list, 1)
    noun = random.sample(noun_list, 1)
    if who[0] in ['She','He']:
        if verb[0][-1] == 'e':
            verb[0] += 's'
        else:
            verb[0] += 'es'
    passwd = ' '.join( who + verb + noun)
    replacement_dict = {'e': '3', 's': '$', 'a': '&', 'o': '0'}
    for old, new in replacement_dict.items():
        passwd = passwd.replace(old, new)
    return passwd


if __name__ == "__main__":
    print(rand_pass())
