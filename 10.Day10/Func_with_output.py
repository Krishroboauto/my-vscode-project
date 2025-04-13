#function with an output

def format_name(f_name, l_name):
    
    # Take a first and lastname and format it
    
    f_title = f_name.title()
    l_title = l_name.title()
    return f"{f_title} {l_title}"
    #print(f_title, l_title)

formated_name = format_name("SriKrRISHna", "MANtravadi")
print(formated_name)

output = len("Srikrishna Mantravadi")
print(output)