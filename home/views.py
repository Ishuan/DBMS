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


def logout(request):
    request.session.flush()
    return render(request, "login.html", {})


def cs(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year, "semester": semester, "courseID": courseID,
                   "courseName": courseName, "fname": fname})


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
    fname = get_fname(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year, "semester": semester, "courseID": courseID,
                   "courseName": courseName, "fname": fname})


def bio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year, "semester": semester, "courseID": courseID,
                   "courseName": courseName, "fname": fname})


#####################
## Computer Science
#####################

def faccs(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    search_room = find_fac(request.GET['OfficeRooms'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year, "fac_room": search_room, "semester": semester,
                   "courseID": courseID, "courseName": courseName, "fname": fname})


def fyearcs(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    fac_by_year = find_fac_year(request.GET['fac_year'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year, "fac_by_year": fac_by_year, "semester": semester,
                   "courseID": courseID, "courseName": courseName, "fname": fname})


def coursecs(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    faculty = get_fac_by_course(request.GET['fac_course'], request.GET['semesters'])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "faculty": faculty, "courseName": courseName,
                   "fname": fname})


def getcsCourseID(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    course_code = get_course_code(request.GET['Cname'], details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "course_code": course_code,
                   "fname": fname})


def getcsCourseClass(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    class_room, class_time = get_course_class(request.GET['Cname'], details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "class_room": class_room,
                   "class_time": class_time, "fname": fname})


def getcsCID(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    cid = get_CID_Fac_Sem(request.GET['fname'], request.GET['semester'])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname, "cid": cid})


def officecsdetails(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    office = get_Office_Details(request.GET['fname'])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname,
                   "office_details": office})


def year_cs_details(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Computer Science'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    working_since = get_Years_Details(request.GET['fname'])
    return render(request, "cs.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname,
                   "working_since": working_since})


#####################
## SIS
#####################

def facsis(request):
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
    fname = get_fname(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year, "fac_room": search_room, "semester": semester,
                   "courseID": courseID, "courseName": courseName, "fname": fname})


def fyearsis(request):
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
    fname = get_fname(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year, "fac_by_year": fac_by_year, "semester": semester,
                   "courseID": courseID, "courseName": courseName, "fname": fname})


def coursesis(request):
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
    fname = get_fname(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "faculty": faculty, "courseName": courseName,
                   "fname": fname})


def getsisCourseID(request):
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
    fname = get_fname(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "course_code": course_code,
                   "fname": fname})


def getsisCourseClass(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    class_room, class_time = get_course_class(request.GET['Cname'], details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "class_room": class_room,
                   "class_time": class_time, "fname": fname})


def getsisCID(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    cid = get_CID_Fac_Sem(request.GET['fname'], request.GET['semester'])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname, "cid": cid})


def office_sis_details(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    office = get_Office_Details(request.GET['fname'])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname,
                   "office_details": office})


def year_sis_details(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Software and Information System'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    working_since = get_Years_Details(request.GET['fname'])
    return render(request, "sis.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname,
                   "working_since": working_since})


#####################
## BIOINFORMATICS
#####################

def facbio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    search_room = find_fac(request.GET['OfficeRooms'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year, "fac_room": search_room, "semester": semester,
                   "courseID": courseID, "courseName": courseName, "fname": fname})


def fyearbio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    fac_by_year = find_fac_year(request.GET['fac_year'], details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseID, semester = get_course(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year, "fac_by_year": fac_by_year, "semester": semester,
                   "courseID": courseID, "courseName": courseName, "fname": fname})


def coursebio(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    faculty = get_fac_by_course(request.GET['fac_course'], request.GET['semesters'])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "faculty": faculty, "courseName": courseName,
                   "fname": fname})


def getbioCourseID(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    course_code = get_course_code(request.GET['Cname'], details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "course_code": course_code,
                   "fname": fname})


def getbioCourseClass(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    class_room, class_time = get_course_class(request.GET['Cname'], details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "class_room": class_room,
                   "class_time": class_time, "fname": fname})


def getbioCID(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    cid = get_CID_Fac_Sem(request.GET['fname'], request.GET['semester'])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname, "cid": cid})


def office_bio_details(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    office = get_Office_Details(request.GET['fname'])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname,
                   "office_details": office})


def year_bio_details(request):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select * from departments where dname='Bioinformatics and Genomics'"
    cur.execute(statement)
    details = cur.fetchone()
    courseID, semester = get_course(details[0])
    rooms = get_rooms(details[0])
    year = get_year(details[0])
    courseName = get_course_name(details[0])
    fname = get_fname(details[0])
    working_since = get_Years_Details(request.GET['fname'])
    return render(request, "bio.html",
                  {"details": details, "office": rooms, "year": year,
                   "semester": semester, "courseID": courseID, "courseName": courseName, "fname": fname,
                   "working_since": working_since})


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


def get_fname(dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    statement = "select DISTINCT fname from work_in where dname=\'" + dname + "\' order by fname asc"
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
                "w.fname = t.fname and c.cname=\'" + Cname + "\' and w.dname = \'" + dname + "\'"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def get_course_class(Cname, dname):
    conn = MySQLdb.connect(user="root", password="root123", database="project_DBS", host='localhost')
    cur = conn.cursor()
    cur1 = conn.cursor()
    statement = "select distinct c.classroom from courses c, teaches t, work_in w where c.CRN = t.CRN " \
                "and w.fname = t.fname and c.cname=\'" + Cname + "\' and w.dname = \'" + dname + "\'"
    statement1 = "select t.class_time from courses c, teaches t, work_in w where c.CRN = t.CRN " \
                 "and w.fname = t.fname and c.cname=\'" + Cname + "\' and w.dname = \'" + dname + "\'"
    cur.execute(statement)
    cur1.execute(statement1)
    rs = cur.fetchall()
    rs1 = cur1.fetchall()
    return (rs, rs1)


def get_CID_Fac_Sem(fname, sem):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select c.course_code from courses c, teaches t where t.CRN= c.CRN and c.semester=\'" + \
                sem + "\' and t.fname=\'" + fname + "\' order by c.course_code asc"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def get_Office_Details(fname):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select office_room from faculties where fname=\'" + fname + "\'"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs


def get_Years_Details(fname):
    conn = MySQLdb.connect(user='root', password='root123', database='project_DBS', host='localhost')
    cur = conn.cursor()
    statement = "select since from work_in where fname=\'" + fname + "\'"
    cur.execute(statement)
    rs = cur.fetchall()
    return rs
