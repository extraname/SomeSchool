from sqlalchemy.dialects.postgresql import JSON
from settings import db


class School(db.Model):
    __tablename__ = "school"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    link = db.Column(db.String(90), unique=True, nullable=False)

    courses = db.relationship("Course", backref="school")
    teachers = db.relationship("Teacher", backref="school")
    students = db.relationship("Student", backref="school")

    def __repr__(self):
        return "School : %r" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "link": self.link,
            "subjects_count": Course.query.count(),
            "students": Student.query.count(),
            "teachers": Teacher.query.count()
        }


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    module = db.relationship('Module', backref="course")
    school_ = db.Column(db.Integer, db.ForeignKey("school.id"))
    teacher = db.relationship("Teacher", backref="course", uselist=False)

    def __repr__(self):
        return f"{self.name}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "modules": str(self.module),
            "teacher": str(self.teacher)
        }


courses_students_table = db.Table(
    "courses_students", db.Model.metadata,
    db.Column('course_id', db.Integer, db.ForeignKey("courses.id")),
    db.Column('student_id', db.Integer, db.ForeignKey("students.id"))
)


class Teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False)
    school_ = db.Column(db.Integer, db.ForeignKey("school.id"))
    course_ = db.Column(db.Integer, db.ForeignKey("courses.id"))

    # students = db.relationship("Student", backref="teacher")

    def __repr__(self):
        return f"{self.name} with unique id: {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "course": str(self.course)
        }


teachers_students_table = db.Table(
    "teachers_students", db.Model.metadata,
    db.Column('teacher_id', db.Integer, db.ForeignKey("teachers.id")),
    db.Column('student_id', db.Integer, db.ForeignKey("students.id"))
)


class Module(db.Model):
    __tablename__ = "modules"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    course_ = db.Column(db.Integer, db.ForeignKey("courses.id"))

    def __repr__(self):
        return f"{self.name}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "course": str(self.course)
        }


modules_students_table = db.Table(
    "modules_students", db.Model.metadata,
    db.Column('module_id', db.Integer, db.ForeignKey("modules.id")),
    db.Column('student_id', db.Integer, db.ForeignKey("students.id"))
)


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False)
    school_ = db.Column(db.Integer, db.ForeignKey("school.id"))
    course = db.relationship("Course", secondary=courses_students_table,
                             backref="students")
    teacher = db.relationship("Teacher", secondary=teachers_students_table,
                              backref="students")
    # teacher = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    grade = db.Column(JSON)
    module = db.relationship("Module", secondary=modules_students_table,
                             backref="students")

    def __repr__(self):
        return f"{self.name} with unique id: {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "course": str(self.course),
            "teacher": str(self.teacher),
            "modules": str(self.module),
            "grade": str(self.grade)
        }


def serialize_multiple(objects: list) -> list:
    return [obj.serialize() for obj in objects]


if __name__ == "__main__":
    db.create_all()
