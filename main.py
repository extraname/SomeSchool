from settings import app, api
from views.school import MySchool
from views.courses import SingleCourse, Courses, CourseModules, \
    CourseTeacher, CourseStudents
from views.modules import Modules, SingleModule, ModuleCourse
from views.teachers import Teachers, SingleTeacher, TeacherCourse, \
    TeacherStudents


api.add_resource(MySchool, '/school')

api.add_resource(Courses, "/courses")
api.add_resource(SingleCourse, "/courses/<int:course_id>")
api.add_resource(CourseModules, "/courses/<int:course_id>/modules")
api.add_resource(CourseTeacher, "/courses/<int:course_id>/teacher")
api.add_resource(CourseStudents, "/courses/<int:course_id>/students")

api.add_resource(Modules, "/modules")
api.add_resource(SingleModule, "/modules/<int:module_id>")
api.add_resource(ModuleCourse, "/modules/<int:module_id>/course")

api.add_resource(Teachers, "/teachers")
api.add_resource(SingleTeacher, "/teachers/<int:teacher_id>")
api.add_resource(TeacherCourse, "/teachers/<int:teacher_id>/course")
api.add_resource(TeacherStudents, "/teachers/<int:teacher_id>/students")

if __name__ == "__main__":
    app.run()
