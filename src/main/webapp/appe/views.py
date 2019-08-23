from django.shortcuts import render, redirect
from .models import Customer_details, Vendor_details,Add_newproduct, Vendor_Addresses


def customersignup(request):
    if request.method == "POST":
        uname = request.POST.get("Username")
        email = request.POST.get("Email")
        mobileno = request.POST.get("Mobileno")
        password = request.POST.get("Password")

        one = uname[-2]
        two = mobileno[-3]
        three = uname[2]
        four = password[-4]
        five = email[5]
        six = password[-1]

        otp = four + one + str(two) + three + five + six

        message = sendEcommerceSMS(mobileno, otp)
        import json
        d1 = json.loads(message)
        if d1['return']:
            qs = Customer_details(USERNAME=uname, PASSWORD=password, EMAIL=email, MOBILENO=mobileno,OTP=otp)

            qs.save()
            return render(request, "customer/customer_otpverify.html")

def check_customerotp(request):
    if request.method == "POST":
        otp = request.POST.get("Otp")
        print(otp)
        qs = Customer_details.objects.filter(OTP=otp)
        if qs:
            return render(request, "customer/customerlogin.html", {"msg": "Registered Successfully"})
        else:
            return render(request, "customer/customer_otpverify.html", {"msg": "Invalid Otp"})


def customerlogin(request):
    email = request.POST.get("Email")
    password = request.POST.get("Password")
    qs = Customer_details.objects.filter(EMAIL=email,PASSWORD=password)
    if qs:
        qs1 = Customer_details.objects.filter(EMAIL=email)
        request.session['cname'] = qs1[0].USERNAME
        request.session['cidno'] = qs1[0].IDNO
        return render(request,"customer/customer_dashboard.html",{"data":qs,"message":"Successfully Login"})
    else:
        return render(request,"customer/customerlogin.html",{"msg":"Invalid Customer"})

def vendorsignup(request):
    if request.method == "POST":
        uname = request.POST.get("Username")
        email = request.POST.get("Email")
        mobileno = request.POST.get("Mobileno")
        password = request.POST.get("Password")

        one = uname[0]
        two = mobileno[-5]
        three = uname[-2]
        four = password[3]
        five = email[2]
        six = password[-1]


        otp = four + one + str(two) + three + five + six

        message = sendEcommerceSMS(mobileno,otp)
        import json
        d1 = json.loads(message)
        if d1['return']:
            Vendor_details(USERNAME=uname,EMAIL=email,MOBILENO=mobileno,PASSWORD=password,OTP=otp).save()
            return render(request, "Registered_Vendor_OtpVerify.html")

def sendEcommerceSMS(mobileno,otp):
    import requests

    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello welcome to Ecommerce........!Your OTP Is......"+otp+"&language=english&route=p&numbers="+mobileno
    headers = {
        'authorization': "76eLvonl6aTGNEBYhmaaTX6xfIGNUuZdFwosHBTpHZvDKDPDF9ollY55mc7L",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text


def check_vendorotp(request):
    if request.method == "POST":
        otp = request.POST.get("Otp")
        print(otp)
        qs = Vendor_details.objects.filter(OTP=otp)
        if qs:
            return render(request, "logins.html", {"msg": "Registered Successfully"})
        else:
            return render(request, "Registered_Vendor_OtpVerify.html", {"msg": "Invalid Otp"})


def vendorlogin(request):
    email = request.POST.get("Email")
    password = request.POST.get("Password")
    qs = Vendor_details.objects.filter(EMAIL=email,PASSWORD=password)
    if qs:
        qs1 = Vendor_details.objects.filter(EMAIL=email)
        request.session['vname'] = qs1[0].USERNAME
        request.session['vidno'] = qs1[0].IDNO
        return render(request,"dashboard.html",{"data":qs,"message":"Successfully Login"})
    else:
        return render(request,"login_Vendor.html",{"msg":"Invalid Vendor"})


def clogout(request):
    del request.session['cname']
    del request.session['cidno']
    return redirect('clogin')


def vlogout(request):
    del request.session['vname']
    del request.session['vidno']
    return redirect('vlogin')


def addnewproduct(request):
    if request.method == "POST":
        type = request.POST.get("type")
        categories = request.POST.get("categories")
        categorytype = request.POST.get("categorytype")
        size = request.POST.get("size")
        quantity = request.POST.get("quantity")
        v_p_name = request.session['vidno']
        name = request.POST.get("name")
        image = request.FILES['image']
        price = request.POST.get("price")
        description = request.POST.get("description")

        print(v_p_name)
        Add_newproduct(TYPE=type,CATEGORIES=categories,CATEGORIETYPE=categorytype,SIZE=size,QUANTITY=quantity,
                        NAME=name,IMAGE=image,PRICE=price,DESCRIPTION=description,V_P_ID_id=v_p_name).save()

        qs = Add_newproduct.objects.all()
        return render(request, "dashboard.html", {"msg": "Product added Successfully", "data": qs})

def saveaddress(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        housenumber = request.POST.get("Housenumber")
        address = request.POST.get("Address")
        city = request.POST.get("City")
        state = request.POST.get("State")
        pincode = request.POST.get("Pincode")
        landmark = request.POST.get("Landmark")
        phone = request.POST.get("Phone")
        vadd_id = request.session['vidno']

        Vendor_Addresses(NAME=name,HOUSENUMBER=housenumber,ADDRESS=address,CITY=city,STATE=state,LANDMARK=landmark,PINCODE=pincode,PHONE=phone,V_A_ID_id=vadd_id).save()
        qs = Vendor_Addresses.objects.all()
        return render(request, "your_Address.html", {"msg": "Address added Successfully", "object_list": qs})


def update_address(request):
    idno = request.GET['idno']
    qs = Vendor_Addresses.objects.filter(VAID=idno)
    return render(request,'update_Address.html',{"idno":idno,"qs":qs})


def address_Update(request):
    if request.method == 'POST':
        idno = request.POST['idno']
        name = request.POST.get("Name")
        housenumber = request.POST.get("Housenumber")
        address = request.POST.get("Address")
        city = request.POST.get("City")
        state = request.POST.get("State")
        pincode = request.POST.get("Pincode")
        landmark = request.POST.get("Landmark")
        phone = request.POST.get("Phone")

        Vendor_Addresses.objects.filter(VAID=idno).update(NAME=name,HOUSENUMBER=housenumber,ADDRESS=address,CITY=city,STATE=state,LANDMARK=landmark,PINCODE=pincode,PHONE=phone)
        qs = Vendor_Addresses.objects.all()
        return render(request, "your_Address.html", {"msg": "Address updated Successfully", "object_list": qs})


def delete_ADDress(request):
    idno = request.GET['idno']
    Vendor_Addresses.objects.filter(VAID=idno).delete()
    del_list = Vendor_Addresses.objects.all()
    return render(request,'your_Address.html',{"object_list":del_list})


def vendor_changepassword(request):
    uname = request.GET['uname']
    return render(request, 'vendor_Changepassword.html', {"uname": uname})


def vendor_updatepassword(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")
        qs = Vendor_details.objects.filter(USERNAME=uname,PASSWORD=oldpassword)
        if qs:
            qs.update(PASSWORD=newpassword)
            qs1 = Vendor_details.objects.all()
            return render(request, "login_Security.html", {"message": "Password Changed Successfully", "data": qs1})
        else:
            qs2 = Vendor_details.objects.all()
            return render(request,"vendor_Changepassword.html",{"message":"Old Password Not Matched,Password not changed","data":qs2,"uname":uname})


def vendorchange_mobilenumber(request):
    uname = request.GET['uname']
    return render(request, 'vendor_Changemobilenumber.html', {"uname": uname})


def vendorupdate_mobileno(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        oldmobilenumber = request.POST.get("oldmobilenumber")
        newmobilenumber = request.POST.get("newmobilenumber")
        qs = Vendor_details.objects.filter(USERNAME=uname,MOBILENO=oldmobilenumber)
        if qs:
            qs.update(MOBILENO=newmobilenumber)
            qs = Vendor_details.objects.all()
            return render(request,"login_Security.html",{"message":"MobileNumber Changed Successfully","data":qs})
        else:
            qs = Vendor_details.objects.all()
            return render(request, "vendor_Changemobilenumber.html", {"message": "Old Mobilenumber Not Matched,MobileNo Not Changed","uname":uname, "data": qs})


def add_to_cart(request):
    name = request.GET['name']
    qs = Add_newproduct.objects.filter(NAME=name)
    return render(request,'checkout.html',{"object_list":qs})


def single(request):
    name = request.GET['name']
    qs = Add_newproduct.objects.filter(NAME=name)
    return render(request,'single.html',{"object_list":qs})


def delete_product(request):
    name =  request.GET['name']
    Add_newproduct.objects.filter(NAME=name).delete()
    del_list = Add_newproduct.objects.filter()
    return render(request, 'products.html', {"object_list": del_list,"msg":"Product deleted successfully"})
