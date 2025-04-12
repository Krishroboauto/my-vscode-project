def calculate_love_score(name1,name2):

    check = (name1+name2).upper()

    t_count = check.count("T")
    r_count = check.count("R")
    u_count = check.count("U")
    e_count_true = check.count("E")
    total_true = t_count + r_count + u_count + e_count_true

    l_count = check.count("L")
    o_count = check.count("O")
    v_count = check.count("V")
    e_count_love = check.count("E")
    total_love = l_count + o_count + v_count + e_count_love

    Total = 10*total_true + total_love
    print(f"Love Score = {Total}")

calculate_love_score("kayne West","Kim Kardashian")



