age = int(input("input ur age: "))
report = input("uploaded report?(yes/no): ")
vip_level = int(input("input ur vip level(1/2/3): "))

if 18 <= age <= 45:
    print("u age is legal!")
    if report == "yes":
        print("u can jpin the match!")
        if vip_level == 1:
            print("u can get a car!")
        elif vip_level == 2:
            print("u can get a bicycle!")
        elif vip_level == 3:
            print("u can get a pen!")
        else:
            print("u cant get gift!")
    else:
        print("u can't join the match!")
else:
    print("u can't join the match!")