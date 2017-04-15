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
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    return render(request, "cs.html", {"details": details, "office": rooms, "year": year})


def sis(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    return render(request, "sis.html", {"details": details, "office": rooms, "year": year})


def bio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    return render(request, "bio.html", {"details": details, "office": rooms, "year": year})


def fac(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    print(request.GET['OfficeRooms'])
    search_room = find_fac(request.GET['OfficeRooms'], details[0])
    print(search_room[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    return render(request, "bio.html", {"details": details, "office": rooms, "year": year})


######################################

def get_rooms(dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = "select DISTINCT f.office_room from faculties f , work_in w where f.fname = w.fname and w.dname=\'" + \
                dname + "\' order by f.office_room asc"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def get_year(dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = "select DISTINCT w.since from faculties f, work_in w  where f.fname=w.fname and w.dname=\'" + dname + \
                "\' order by w.since asc"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def find_fac(room, dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = "select f.fname from faculties f, work_in w where f.office_room=\'" + room + "\' and w.dname=\'" + dname + "\' and f.fname=w.fname"
    cur.execute(statement)
    rs = cur.fetchone()
    return rs
