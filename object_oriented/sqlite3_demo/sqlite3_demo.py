import sqlite3

class Field:
	def __init__(self, name, dataType):
		self.name = name
		self.dataType = dataType

fields = (Field('name', 'TEXT'),
		  Field('g_number', 'TEXT'),
		  Field('gpa', 'REAL'))

# this class needs to define attributes corresponding to the fields above
class Student:
	def __init__(self, name, g_number, gpa):
		self.name =		name
		self.g_number =	g_number
		self.gpa =		gpa

students = (Student('Bob', 		'G123456789',	'3.02'),
			Student('Alice',	'G234567890',	'2.93'),
			Student('Perry',	'G345678901',	'3.95'),
			Student('Charlie',	'G456789012',	'1.25'))

dbFileName =		'students.sqlite3'
sqlFileName =		'students.sqldb'
studentTableName =	'students'

def readSQL(fileName, conn):
	f = open(fileName, 'r')
	sql = f.read()
	f.close()
	conn.executescript(sql)

def writeSQL(fileName, conn):
	f = open(fileName, 'w')
	for line in conn.iterdump():
		print(line, file=f)
	f.close()

def run(readSQLfile, writeSQLfile):

	conn = sqlite3.connect(':memory:')

	if readSQLfile:
		readSQL(sqlFileName, conn)
	
	crsr = conn.cursor()
	
	if not readSQLfile:
		sqlFields = ''.join([f'{field.name} {field.dataType}, ' for field in fields])[:-2]
		sqlStr = f'CREATE TABLE {studentTableName} ({sqlFields})'
		crsr.execute(sqlStr)
	
		# for field in fields[1:]:
		# 	crsr.execute(f"ALTER TABLE {studentTableName} ADD COLUMN '{field.name}' {field.type}")
	
		for student in students:
			sqlStr = f'INSERT INTO {studentTableName} ' \
					 f'({fields[0].name}, {fields[1].name}, {fields[2].name}) ' \
					 f"VALUES ('{student.name}', '{student.g_number}', '{student.gpa}')"
			crsr.execute(sqlStr)
		
	sqlStr = f'SELECT * FROM {studentTableName}'
	crsr.execute(sqlStr)
	selectedStudents = crsr.fetchall()

	sqlStr = f'SELECT * FROM {studentTableName} WHERE {fields[2].name} > 3'
	crsr.execute(sqlStr)
	selectedStudents = crsr.fetchall()

	conn.commit()

	if writeSQLfile:
		writeSQL(sqlFileName, conn)

	conn.close()

run(False, False)
# run(False, True)
# run(True, False)
# run(True, True)
