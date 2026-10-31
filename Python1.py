num=int(input())
result_list=[]
op_dict={"%":1,"*":1,"+":0}
for i in range(num):
    S_list=input().split()
    result=0
    if op_dict[S_list[1]]>op_dict[S_list[3]]:
        result=int(S_list[0])