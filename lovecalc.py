def calculate_love_score(name1,name2):
    combo=name1+name2
    lower_names=combo.lower()
    
    t=lower_names.count("t")
    r=lower_names.count("r")
    u=lower_names.count("u")
    e=lower_names.count("e")
    first_digit=str(t+r+u+e)
    
        # TODO: write code...
    
    l=lower_names.count("l")
    o=lower_names.count("o")
    v=lower_names.count("v")
    e=lower_names.count("e")
    second_digit=str(l+o+v+e)
    
    total_score=(first_digit+second_digit)
    print(total_score)

calculate_love_score("Afia","Pokuaa")