
def vehicle_exit(floor1,floor2,floor3,veh_no):
    for i in floor1,floor2,floor3:
        for k in i:
            if k['vehicle_no'] == veh_no:
                i.remove(k)
                break