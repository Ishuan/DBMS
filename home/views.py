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
    courseID, semester = get_course(details[0])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year, "semester": semester, "courseID": courseID})


def sis(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year, "semester": semester, "courseID": courseID,
                   "courseName": courseName})


def bio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year, "semester": semester, "courseID": courseID})


#####################
## Computer Science
#####################

def fac_cs(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    search_room = find_fac(request.GET['OfficeRooms'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    return render(request, "cs.html", {"details": details, "office": rooms, "year": year, "fac_room": search_room})


def fyear_cs(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    search_room = request.GET['fac_room']
    fac_by_year = find_fac_year(request.GET['fac_year'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    return render(request, "cs.html", {"details": details, "office": rooms, "year": year, "fac_by_year": fac_by_year})


#####################
## SIS
#####################

def fac_sis(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    search_room = find_fac(request.GET['OfficeRooms'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year, "fac_room": search_room, "semester": semester,
                   "courseID": courseID, "courseName": courseName})


def fyear_sis(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    fac_by_year = find_fac_year(request.GET['fac_year'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year, "fac_by_year": fac_by_year, "semester": semester,
                   "courseID": courseID, "courseName": courseName})


def course_sis(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    faculty = get_fac_by_course(request.GET['fac_course'], request.GET['semesters'])
    courseName = get_course_name(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "faculty": faculty, "courseName": courseName})


def getCourseID(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    course_code = get_course_code(request.GET['Cname'], details[0])
    courseName = get_course_name(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "course_code": course_code})


#####################
## BIOINFORMATICS
#####################

def fac_bio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    search_room = find_fac(request.GET['OfficeRooms'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    return render(request, "bio.html", {"details": details, "office": rooms, "year": year, "fac_room": search_room})


def fyear_bio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    search_room = request.GET['fac_room']
    fac_by_year = find_fac_year(request.GET['fac_year'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    return render(request, "bio.html", {"details": details, "office": rooms, "year": year, "fac_by_year": fac_by_year})


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
    statement = "select f.fname from faculties f, work_in w where f.office_room=\'" + room + "\' and w.dname=\'" + \
                dname + "\' and f.fname=w.fname"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def find_fac_year(year, dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = "select w.fname from work_in w where w.since=\'" + year + "\' and w.dname=\'" + dname + "\'"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def course_faculty(course, dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = ""
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def get_course(dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    cur1 = conn.cursor()
    if dname == 'Bioinformatics and Genomics':
        statement = "select distinct course_code from courses where course_code like 'BINF%' order by course_code asc"
    elif dname == 'Computer Science':
        statement = "select distinct course_code from courses where course_code like 'ITCS%' order by course_code asc"
    else:
        statement = "select distinct course_code from courses where course_code like 'ITIS%' order by course_code asc"
    statement1 = "select distinct semester from courses"
    cur.execute(statement)
    cur1.execute(statement1)
    rs = cur.fetchall()
    rs1 = cur1.fetchall()
    return (rs, rs1)


def get_fac_by_course(course, sem):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = "select t.fname from teaches t, courses c where t.CRN = c.CRN and c.course_code =\'" + course + \
                "\' and c.semester = \'" + sem + "\'"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def get_course_name(dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = "select distinct c.cname from courses c, teaches t, work_in w where c.CRN = t.CRN and w.fname = t.fname " \
                "and w.dname =\'" + dname + "\' order by c.cname asc"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def get_course_code(Cname, dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = "select distinct c.course_code from courses c, teaches t, work_in w where c.CRN = t.CRN and " \
                "w.fname = t.fname and c.cname=\'" +Cname+ "\' and w.dname = \'"+ dname +"\'"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs
