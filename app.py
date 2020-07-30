from flask import Flask,render_template
# request,redirect,session
# import sqlite3
app = Flask(__name__)
# app.sevret_key = "sunabaco"



@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/hello')

def greet():
    return render_template('index.html')

@app.route('/top')
def top():
    return "ここがああ"

# @app.route('/list')
# def tasklist():
#     if "user_id" in session:
#         user_id
#     conn = sqlite3.connect('flasktest.db')
#     c = conn.cursor()
#     c.execute("SELECT id , task FROM task")
#     task_list = []
#     for row in c.fetchll():
#         task_list.append({"id":row[0],!task:row[1]})
# c.close
# print(task_list)

# @app.route('/edit/<int:id>')
# def edit(id):
#     if "user_id" in session:
#         conn = sqlite3connect('flasktest.db')
#         c = conn.cursor()
#         c.execute("SELECT task FROM task WHERE id = ?",(id,))
#         py_task = c.fetchone()
#         c.close()
#         if py_task is None:
#             return"タスクがありません”
#     else:
#         task = py_task[0]
#     py_item = {"dic_id":id,"dic_task":py_task}
# return render_template("edit.html",html_task = py_task = py_task)

# def update_task():
#     item_id = request.form.get("task_id")
#     #入力フォームは文字列方なのでint型に変換しました。
#     item_id = int(item_id)
#     conn = sqlite3connect('flasktest.db')
#     c = conn.cursor()
#     c.execute("UPDATE task SET task = ? WHERE id = ?",(task,item_id))
#     conn.commit()

#     @app.route('/del/<int:id>')
#     def delete(id):
#         conn = sqlite3.connect('flasktest.db')
#         c= conn.cursor()
#         c.execute("DELETE FROM task WHERE id = ?",(id,))
#         conn.commit()
#         c.close()
#         return redirect('/list')
        

# @app.route("/regist")
# def regist_get():
#     return render_template('regist.html')


# @app.route('/regist',methods=['POST'])
# def regist_post():
#     py_name = request.form.get("member_name")
#     py_password = request.form.get("member_password")
#     conn = sqlite3.connect('flasktest.db')
#         c= conn.cursor()
#         c.execute("INSERT INTO member VALUES (null,?,?)",(py_name,py_password))
#         conn.commit()
#         c.close()
#         return redirect('/login')

# @app.route("/login")
# def login_get():
#     if "user_id" in session:
#         return redirect('/list')
#     else:
#         return render_template("login.html")

# @app.route("/login",methods=['POST'])
# def login_post():
#     py_name = request.form.get("member_password")
#     conn = sqlite3.connect('flasktest.db')
#         c= conn.cursor()
#     c.execute("SELECT id FROM member WHERE name = ? AND password = ?",(py_name,py_password))
#     user_id = c.fetchone()
#     c.close()
#     if user_id id None:
#         return render_template("login.html")
#     else:
#         session["user_id"] = user_id
#         redirect("/list")
# @app.route('/logout')
# def logout():
#     session.pop("user_id",None)
#     re
if __name__ == '__main__':
    app.run(debug = True)

