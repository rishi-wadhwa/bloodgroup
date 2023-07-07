'''
Created on Jan 10, 2017

@author: hanif
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    data = db.read(None)
    
    return render_template('index.html')
@app.route('/index7')
def index7():
    data = db.read(None)
    
    return render_template('index7.html',data=data)
@app.route('/stock1')
def stock1():
   
    data = db.read3(None)
    
    return render_template('stock1.html',data=data)
@app.route('/viewcontact')
def viewcontact():
   
    data = db.read34(None)
    
    return render_template('viewcontact.html',data=data)


@app.route('/hm/')
def hm():
    return render_template('index.html')
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/login/')
def login():
    return render_template('login.html')
@app.route('/contact/')
def contact():
    return render_template('contact.html')
@app.route('/centers/')
def centers():
    return render_template('centers.html')
	
@app.route('/stocks/')
def stocks():
    return render_template('stocks.html')
@app.route('/viewm/')
def viewm():
    return render_template('viewm.html')


@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')
@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("New Record  Added")
        else:
            flash("New Record not Added")
            
        return redirect(url_for('add'))
    else:
        return redirect(url_for('index'))
@app.route('/addp', methods = ['POST', 'GET'])
def addp():
    if request.method == 'POST' and request.form['save']:
        if db.insertp(request.form):
            flash("New Record  Added")
        else:
            flash("New Record not Added")
            
        return redirect(url_for('viewm'))
    else:
        return redirect(url_for('index'))
@app.route('/addmenu1', methods = ['POST', 'GET'])
def addmenu1():
    if request.method == 'POST' and request.form['save']:
        if db.insertc(request.form):
            flash("New Record  Added")
        else:
            flash("New Record not Added")
            
        return redirect(url_for('contact'))
    else:
        return redirect(url_for('index'))
@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);
    
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)
@app.route('/updateadmin1', methods = ['POST'])
def updateadmin1():
    if request.method == 'POST' and request.form['update']:
        
        if db.updateadmin(session['update'], request.form):
            flash('A rollno has been updated')
           
        else:
            flash('A rollno can not be updated')
        
        session.pop('update', None)
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read22(id);
    
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)
@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:
        
        if db.delete(session['delete']):
            flash('data  has been deleted')
           
        else:
            flash('data has can not be deleted')
        
        session.pop('delete', None)
        
        return redirect(url_for('index7'))
    else:
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = True, port=8181, host="0.0.0.0")