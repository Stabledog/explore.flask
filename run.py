#!/usr/bin/env python3.7


from flask import Flask, render_template

app = Flask(__name__)

def set_trace():
    import pudb
    pudb.set_trace()

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheee",my_list=[i for i in range(5)])

if __name__=="__main__":
    app.jinja_env.globals.update(set_trace=set_trace)
    app.run(host='0.0.0.0',port=9193, debug=True)

