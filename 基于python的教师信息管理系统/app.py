from flask import Flask,request,render_template
import teacherdao
app = Flask(__name__)


@app.route('/')
def hello_world():
    results=teacherdao.loadAll()
    print(results)
    return render_template('index.html',results=results)

@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        results = teacherdao.loadAll()
        print(results)
        return render_template('index.html', results=results)

#添加操作
@app.route('/addInformation',methods=['GET','POST'])
def addInformation():
   if request.method=='GET':
    return render_template('add.html')
   else:
       number = request.form.get('number')
       print(number)
       name = request.form.get('name')
       id_card = request.form.get('id_card')
       birthday = request.form.get('birthday')
       address = request.form.get('address')
       phone = request.form.get('phone')
       department = request.form.get('department')
       money = request.form.get('money')
       work_time = request.form.get('work_time')
       professon = request.form.get('professon')
       zhiwu = request.form.get('zhiwu')
       remark = request.form.get('remark')
       teacherdao.add(number,name,id_card,birthday,address,phone,department,money,work_time,professon,zhiwu,remark)
       results = teacherdao.loadAll()
       print(results)
       return render_template('index.html', results=results)
#修改操作
@app.route('/update',methods=['GET','POST'])
def update():
   if request.method=='GET':
    number = request.args['number']
    return render_template('update.html',number=number)
   else:
       number = request.form.get('number')
       print(number)
       name = request.form.get('name')
       id_card = request.form.get('id_card')
       birthday = request.form.get('birthday')
       address = request.form.get('address')
       phone = request.form.get('phone')
       department = request.form.get('department')
       money = request.form.get('money')
       work_time = request.form.get('work_time')
       professon = request.form.get('professon')
       zhiwu = request.form.get('zhiwu')
       remark = request.form.get('remark')
       teacherdao.update(number,name,id_card,birthday,address,phone,department,money,work_time,professon,zhiwu,remark)
       results = teacherdao.loadAll()
       print(results)
       return render_template('index.html', results=results)
@app.route('/delete')
def delete():
    number=request.args['number']
    teacherdao.delete(number)
    results = teacherdao.loadAll()
    print(results)
    return render_template('index.html', results=results)
#根据编号操作
@app.route('/select',methods=['GET','POST'])
def select():
    type=request.form.get('type')
    if type=="number":
        number=request.form.get('content')
        results=teacherdao.loadNumber(number)
        return render_template('index.html',results=results)
    if type=='name':
        name=request.form.get('content')
        results=teacherdao.loadName(name)
        return render_template('index.html', results=results)
    if type=='money':
        money1=request.form.get('money1')
        money2=request.form.get('money2')
        results=teacherdao.loadMoney(money1,money2)
        return render_template('index.html', results=results)
    if type=='work_time':
        time1 = request.form.get('money1')
        time2 = request.form.get('money2')
        results = teacherdao.loadWork_time(time1, time2)
        return render_template('index.html', results=results)
    if type=='birthday':
        date1 = request.form.get('date1')
        date2 = request.form.get('date2')
        results = teacherdao.loadBirthday(date1, date2)
        return render_template('index.html', results=results)
if __name__ == '__main__':
    app.run(debug=True)
