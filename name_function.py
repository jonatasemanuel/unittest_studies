def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' '+ last_name
        return full_name.title()
    else:
        full_name = first_name +' '+ last_name
        return full_name.title()


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person

if __name__ == '__main__':
    musician = build_person('Jimi', 'Hendrix', 27) 
    musician1 = get_formatted_name('\njimi', 'hendrix')
    musician2 = get_formatted_name('\n john', 'hooker', 'lee')
    print(musician)
    print(musician1)
    print(musician2)
