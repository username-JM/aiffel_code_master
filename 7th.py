def find_max_move(list_charger, my_loc, my_fuel, index, max_point):
    num_charged = 0; #추가로 충전한 횟수
    check = 0 #
    for i in range(len(list_charger)):
        if list_charger[index] - my_loc - my_fuel < 0: # can go more
            index = index+1
            check = 1
            if index > len(list_charger) - 1:
                if list_charger[index-2] + my_fuel >= max_point:
                    num_charged = num_charged
                return [list_charger[index-1], num_charged + 1, 0]
        elif list_charger[index] - my_loc - my_fuel == 0: #need to charge
            return [list_charger[index], num_charged+1, 1]
        else: #go back to previous station and charge
            if check == 0: return [0, 0, -1]
            return [list_charger[index-1], num_charged+1, 1]

#return : my location, fuel status, number of charge

def function():
    temp = list(map(int, input().split()))
    my_fuel = temp[0]
    num_station = temp[1]
    num_charger = temp[2]
    
    list_charger = list(map(int, input().split()))

    ans = 0
    my_loc = 0;

    for i in range(10000):
        if my_loc + my_fuel < num_station: #아직 종점까지 안간 경우
            a = find_max_move(list_charger, my_loc, my_fuel, ans, num_station) #
        else:
            return ans #종점을 지나간경우
        my_loc = a[0] #내 위치 업데이트
        ans = ans + a[1] #충전횟수 업데이트
        if a[2] == -1:  #
            return 0
        if a[2] == 0: break
    return ans














aaa= function()
print(aaa)


###
# 첫 충전소로 간다. 만약 더 갈 수 있다면 우선 가본다
# 다음 충전소로 간다. 더 갈 수 있다면 더 간다. 딱 맞을 경우 충전한다.
# 만약 모자랄 경우 다시 뒤의 충전소로 간다.
