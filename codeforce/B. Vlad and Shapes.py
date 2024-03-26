for _ in range(int(input())):
    ans = ""
    for __ in range(int(input())):
        st = input()
        if st.count("1") == 1 and ans == "":
            ans = ("TRIANGLE")
    
    print("SQUARE") if ans == "" else print(ans)
            
