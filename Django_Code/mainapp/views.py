from django.shortcuts import render
from mainapp.ml_predict.ml_predict import ML_Predict
from django.http import HttpResponse
from mainapp.models import Member
from django.db.models import Count


# Create your views here.

def login(request):
    return render(
        request, 
        'mainapp/login.html',
        {}
    )
    
def gologin(request):
    mem_id=request.POST.get('id')
    mem_pass=request.POST.get('password')

    mem_dict = Member.objects.filter(mem_id=mem_id, mem_pass=mem_pass).aggregate(Count("mem_id"))
    
    if mem_dict["mem_id__count"] == 0:
        msg="""
            <script type='text/javascript'>
                alert('아이디 또는 패스워드가 일치하지 않습니다. 다시 확인 후 로그인 해주세요!!');
                history.go(-1);
            </script>
        """
        return HttpResponse(msg)
    
    ### 아이디와 패스워드 정보가 있다면
    request.session["ses_mem_id"] = mem_id
    
    return render(
        request,
        "mainapp/index.html",
        {"mem_id":mem_id}
    )

def outline(request):
    return render(
        request,
        'mainapp/index.html',
        {}
    )

def visualization(request):
    return render(
        request,
        'mainapp/visualization.html',
        {}
    )

def predict(request):
    return render(
        request,
        'mainapp/predict.html',
        {}
    )

def predict_View(request):
    ari_co=request.POST.get("ARI_CO")
    ari_po=request.POST.get("ARI_PO")
    ship_type_category=request.POST.get("SHIP_TYPE_CATEGORY")
    dist=request.POST.get("DIST")
    breadth=request.POST.get("BREADTH")
    built=request.POST.get("BUILT")
    deadweight=request.POST.get("DEADWEIGHT")
    depth=request.POST.get("DEPTH")
    draught=request.POST.get("DRAUGHT")
    gt=request.POST.get("GT")
    length=request.POST.get("LENGTH")
    flag=request.POST.get("FLAG")
    u_wind=request.POST.get("U_WIND")
    v_wind=request.POST.get("V_WIND")
    air_temperature=request.POST.get("AIR_TEMPERATURE")
    bn=request.POST.get("BN")
    ata_lt=request.POST.get("ATA_LT")
    port_size=request.POST.get("PORT_SIZE")
    year=request.POST.get("year")
    month=request.POST.get("month")
    day=request.POST.get("day")
    hour=request.POST.get("hour")
    minute=request.POST.get("minute")
    weekday=request.POST.get("weekday")
    X =[ari_co, ari_po, ship_type_category, dist, breadth, built, deadweight, depth, draught,
                gt, length, flag, u_wind, v_wind, air_temperature, bn, ata_lt, port_size, year, month,
                day, hour, minute, weekday]
    random_X = list(map(float,X))
    random_X = [random_X]
    ml_pred = ML_Predict()
    pred_y = ml_pred.getModelPredict(random_X)  
    return HttpResponse(f"예측값: {pred_y}")

def team(request):
    return render(
        request,
        'mainapp/team_member.html',
        {}
    )