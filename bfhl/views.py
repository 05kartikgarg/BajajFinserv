from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def evenoddarray(request):
    
    if request.method == 'POST':
        x=request.data
        arr=x['numbers']
        even=[]
        odd=[]
        id='kartik_garg_05122000'
        flag= True
        for i in arr:
            try:
                if int(i):
                    if int(i)%2==0:
                        even.append(i)
                    else:
                        odd.append(i)
            except:
                flag=False
        if flag==True:
             res={'is_success':flag, 'user_id':id,'odd':odd,'even':even}
        else:
            res={'is_success':flag, 'user_id':id}
    
        return Response(res)

   
