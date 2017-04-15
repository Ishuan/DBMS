from django.shortcuts import render
import MySQLdb


def start(request):
    if 'username' in request.session:
        return render(request, "welcome.html", {})
    else:
        return render(request, "login.html", {})


def home(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select email, pass from admin where email=\'" + request.POST['username'] + "\'"
    cur.execute(statement)
    rs = cur.fetchone()

    if rs:
        if rs[1] == request.POST['password']:
            return render(request, "welcome.html", {})


def cs(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='computer science'"
    cur.execute(statement)
    details = cur.fetchone()
    return render(request, "cs.html", {"details": details})


def sis(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    return render(request, "sis.html", {"details": details})


def bio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    return render(request, "bio.html", {"details": details})
