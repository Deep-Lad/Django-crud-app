from django.shortcuts import render,redirect
import mysql.connector as sql
# Create your views here.
connection = sql.connect(host="localhost",user="root",passwd="deep2003",database="dbs")
cursor = connection.cursor()
def home(request):
    return render(request,'home.html')

def display(request):
         cursor.execute("select * from purchase;")
         data = cursor.fetchall()
         return render(request, 'display.html', {'categories': data})


def add(request):
    return render(request, 'create.html')

def insert(request):
        if request.method == 'POST':
            id=request.POST['id']
            name=request.POST['name']
            quantity=request.POST['quantity']
            amount=request.POST['amount']
            cursor.execute("insert into purchase values('{}','{}','{}','{}') ".format(id,name,quantity,amount))
            connection.commit()
            return redirect(add)
        else:
            return redirect(add)

def delete(reuest,id):
    cursor.execute("delete from purchase where id = {}".format(id))
    connection.commit()
    return redirect(display)

def edit(request,id):
    cursor.execute("select * from purchase where id = {}".format(id))
    data = cursor.fetchone()
    return render(request,'edit.html',{'categories':data})

def update(request):
    if request.method == 'POST':
        id=request.POST['id']
        name=request.POST['name']
        quantity=request.POST['quantity']
        amount=request.POST['amount']
        cursor.execute("update purchase set name='{}',quantity='{}',amount='{}' where id='{}'".format(name,quantity,amount,id))
        connection.commit()
        return redirect(display)

    else:
        return redirect(display)

