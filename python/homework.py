your_money=100
lst=["1","2","3","0"]
service_menu=[]
service_menu.append({"number":"1","m1":"元","m1_name":"人民币","m2":"$","m2_name":"美元","exchange":1/7.14})
service_menu.append({"number":"2","m1":"$","m1_name":"美元","m2":"元","m2_name":"人民币","exchange":7.14})
service_menu.append({"number":"3","m1":"元","m1_name":"人民币","m2":"€","m2_name":"欧元","exchange":0.12})
service_menu.append({"number":"0","m1_name":"结束程序"})

print("**********欢迎使用货币转换服务系统**********")
for list in lst[0:4]:
    for menu in service_menu:
        if menu["number"]==list:
            if list!=lst[-1]:
                print(menu["number"],end="")
                print(" . "+ menu["m1_name"]+"转换"+menu["m2_name"])
                print("欢迎使用"+ menu["m1_name"]+"转换"+menu["m2_name"]+"服务")
                print("您需要转换的"+menu["m1_name"]+"为：",end="")
                print(your_money,end="")
                print(" "+menu["m1"])
                print("兑换成"+menu["m2_name"]+"为：",end="")
                print(your_money*menu["exchange"],end="")
                print(" "+menu["m2"])
            else:
                print(menu["number"],end="")
                print(" . "+ menu["m1_name"])
                print("感谢您的使用，祝您生活愉快，再见！")
            print("==================================")