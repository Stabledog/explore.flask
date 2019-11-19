#!/usr/bin/env python3.7


from flask import Flask, render_template

app = Flask(__name__)

@app.context_processor
def dbg_hook():
    def set_trace():
        import pdb
        pdb.set_trace()
    return dict(set_trace=set_trace)

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheee",my_list=[i for i in range(5)])

if __name__=="__main__":
    app.run(host='0.0.0.0',port=9193, debug=True)
