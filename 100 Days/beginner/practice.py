def format_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

owner = format_name("jose",'LAURITO')
print(owner)
