from flask import Flask, request, session, redirect, render_template
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

ADMIN_PASSWORD = os.getenv("PASSWORD")
MEMBERS_PASSWORD = os.getenv("MPASSWORD")

@app.route("/")
def index():
    return render_template("index.html")

# ---------- ADMIN ----------

@app.route("/adminlogin")
def admin_login():
    return render_template("AdminLogin.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        password = request.form.get("password")  # ← HTML admin

        if password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/admin")
        else:
            return redirect("/adminlogin")

    if not session.get("admin"):
        return redirect("/adminlogin")

    return render_template("Admin.html")

# ---------- MEMBERS ----------

@app.route("/memberslogin")
def members_login():
    return render_template("MembersLogin.html")

@app.route("/members", methods=["GET", "POST"])
def members():
    if request.method == "POST":
        password = request.form.get("memberspassword")  # ← HTML members

        if password == MEMBERS_PASSWORD:
            session["members"] = True
            return redirect("/members")
        else:
            return redirect("/memberslogin")

    if not session.get("members"):
        return redirect("/memberslogin")

    return render_template("Members.html")

# ---------- LOGOUT ----------

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
