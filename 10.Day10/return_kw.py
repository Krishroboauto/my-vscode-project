#function with an output

def format_name(f_name, l_name):
    if fname == "" or l_name == "":
        return "You did not provide any valuble inputs"
    f_title = f_name.title()
    l_title = l_name.title()
    return f"{f_title} {l_title}"
    print(f_title, l_title) # this will not run as return is the last kw in a function

formated_name = format_name("SriKrRISHna", "MANtravadi")
print(formated_name)