from flask import Flask, request, Response, redirect, render_template_string, url_for

Flask.jinja_options = {'line_statement_prefix': '#'}

BLACKLIST = ['pwd','cd','mkdir','rm','cp','mv','bash','sh','file','cat','grep','head','cat','awk','sort','date','tail','7z','alpine','pic','pico','ptx','python','rvim','sed','ss','uniq','ar','arj','arp','as','ascii-xfr','aspell','atobm','awk','base64','base32','base58','basez','bconsole','bridge','busybox','check_memory','cmp','column','cpio','cupsfilter','csvtool','dd','ed','ex','eqn','fold','fmt','fping','gawk','gcc','gdb','gimp','git','hexdump','hd','highlight','iconv','irb','jjs','latex','ltrace','lua','strace','man','nm','nl','nmap','node','nroff','od','paste','php','pg','cut','diff','tee','eval','exec','zsh','ping','scp','xxd','zip','dig','ln','chown','\\','\\x','=','>','{','}','flag','"','\"']
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    if "source" in request.args:
        return Response(open(__file__).read(), mimetype='text/plain')
    return open("index.html").read()

@app.route('/create', methods=["POST"])
def create():
    wish = request.form['wish']
    return redirect(url_for("view_user", wish=wish))

@app.route('/user', methods=["GET"])
def view_user():
    wish = request.args.get("wish", None)
    if any(i in wish.lower() for i in "{}" and BLACKLIST) :
        return "What are you doing!?"
    if (len(wish)) >103:
        return "That's pretty long, make it shorter please!!!"
    return render_template_string(f'''
        {wish}
    ''',wish=wish)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
