from flask import request, session, redirect, url_for, render_template
import os

password = os.getenv("PASSWORD")

@app_route(/)
def home():
  return render_template("index.html")

@app_route(/adminlogin)
def home():
  return render_template("AdminLogin.html")

@app.route("/Admin", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password")

        if password == ADMIN_PASSWORD:
            session["admin"] = True
            return render_template("Admin.html")
        else:
            return redirect("/adminlogin")

    if not session.get("admin"):
        return redirect("/adminlogin")

    return render_template("Admin.html")
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
