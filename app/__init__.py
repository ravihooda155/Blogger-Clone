from flask import Flask
from flask import session
from flask import redirect, url_for
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
import models as dbHandler

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'MKhJHJH798798kjhkjhkjGHh'

@app.route('/')
def home():
    blogs_sent = dbHandler.getAll()
    if 'username' in session:
        return render_template("indexhome.html", logged_in = True,  username=session['username'], blogs=blogs_sent)
    else:
       return render_template("indexhome.html", logged_in = False,  username=None, blogs=blogs_sent) 

@app.route('/home')
def index():
   blogs_sent = dbHandler.getAll()
   if 'username' in session:
       return render_template("index.html", logged_in = True,  username=session['username'], blogs=blogs_sent)
   else:
       return render_template("index.html", logged_in = False,  username=None, blogs=blogs_sent)
 

@app.route('/login', methods=['POST', 'GET'])
def login():
    blogs_sent = dbHandler.getAll()
    if 'username' in session:
        return render_template("admin.html",logged_in = True, username = session["username"], blogs = blogs_sent)
    elif request.method == 'POST':
        if dbHandler.authenticate(request):
            session['username'] = request.form['username']
            return render_template("index.html",logged_in = True, username = session["username"], blogs = blogs_sent)
        else:
            return render_template("login.html", logged_in=False, username=None)   
    return render_template('login.html', logged_in = False, username=None, blogs=blogs_sent)




@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return index()
        # return render_template("index.html")
    
    return index()


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        if dbHandler.insertUser(request):
            return render_template("login.html", logged_in=False)
        else:
	        return render_template("index.html")
    
    return render_template('register.html')

###########################################################################
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == "GET":
      print "HI - in init"
      res, msg = dbHandler.addUser(request.args)
   else:
      res, msg = dbHandler.addUser(request.form)

   return 'hope working'
   #return render_template("result.html", result = res, message = request.method + " : " + msg)

@app.route('/editor/<blog_id>', methods=["GET","POST"])
def editor(blog_id):
    if "username" in session:
        msg, title1 = dbHandler.retrieveParticular(blog_id)
        print msg
        return render_template('editor.html',abc= msg, title=title1)
    else:
        return login()

@app.route('/editor')
def blank_editor():
    if "username" in session:
        return render_template('editor.html',abc="")
    else:
        return login()

@app.route('/admin')
def admin():
   
#    print "in init --------------", session['username']
   if 'username' in session:
       blogs_sent = dbHandler.retrieveBlogs(session['username'])
       return render_template("admin.html", logged_in = True,  username=session['username'], blogs=blogs_sent)
   else:
       return login()


@app.route('/showall')
def showall():
    msg = dbHandler.getAll()
    return render_template('abc.html',user=msg)

@app.route('/comment',methods = ['POST', 'GET'])
def comments():
    if request.method == "GET":
        msg = dbHandler.comment(request.args["blog_id"])
    else:
        print "form : ",request.form["blog_id"]
        msg = dbHandler.comment(request.form["blog_id"])
    
    return render_template('comment_div.html',user=msg)

@app.route('/add_comment',methods = ['POST', 'GET'])
def add_comment():
    if request.method =="POST":
        dbHandler.add_comment(request.form, session)
        return index()
    else:
        return index()

@app.route('/add_comment_blog',methods = ['POST', 'GET'])
def add_comment_blog():
    if request.method =="POST":
        dbHandler.add_comment(request.form, session)
    print "request.form", request.form["blog_id"]
    return particularBlog(request.form["blog_id"])

@app.route('/del_blog', methods = ["GET","POST"])
def del_blog():
    if request.method=="GET":
        msg = dbHandler.del_blogs(request.args["blog_id"])
        print "blog id is : ",request.args["blog_id"]
        print msg
        if msg:
            return '1'
        return '0'
    else:
        msg = dbHandler.del_blogs(request.form["blog_id"])
        print "blog id is : ",request.form["blog_id"]
        print msg
        if msg:
            return '1'
        return '0'
    
@app.route('/profile/<username>')
def particularProfile(username):
    if request.method=='GET':
        data, profiler = dbHandler.particularProfile(username)
        return render_template('profile.html', posts = data, profile=profiler)
    
@app.route('/blog/<id>')
def particularBlog(id):
    if request.method=='GET':
        blog, com = dbHandler.particularBlog(id)
        print blog[0]["theme"]
        if blog[0]["theme"] == 'theme1' or blog[0]["theme"]==None:
            print "inside theme 1"
            return render_template('blog.html', posts = blog, comment = com)
        if blog[0]["theme"] == 'theme2':
            print "inside theme 2"
            return render_template('blog2.html', posts = blog, comment = com)
        if blog[0]["theme"] == 'theme3':
            print "inside theme 3"
            return render_template('blog3.html', posts = blog, comment = com)

    else:
        blog, com = dbHandler.particularBlog(id)
        print com
        print blog
        print "ELSE"
        if blog[0]["theme"] == 'theme1' or blog[0]["theme"]==None:
            print "inside theme 1"
            return render_template('blog.html', posts = blog, comment = com)
        if blog[0]["theme"] == 'theme2':
            print "inside theme 2"
            return render_template('blog2.html', posts = blog, comment = com)
        if blog[0]["theme"] == 'theme3':
            print "inside theme 3"
            return render_template('blog3.html', posts = blog, comment = com)
