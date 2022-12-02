from flask import Flask

import tones as m
app = Flask(__name__)

@app.route("/")
def hello_world():
    rest = ""
    m_keys = dir(m)
    mm = [] 
    for mk in m_keys:
        mm[mk] = getattr(m,mk)
    ns = sorted(mm, key=lambda x: x, reverse=False)
    notes = dir(ns)
    for note in notes:
        if not note.startswith("__"):
            rest = rest + "<div onclick=\"play('"+note+"')\" >"+note+"</div>"
    return '''
    <p>Hello, World!</p>
    <script>
    function play(note){
      fetch("play/"+note);
    }
    alert('ok')
    </script>
    <style>div{display: inline-block; margin: 30px }</style>
    '''+rest

@app.route("/play/<note>")
def play_note(note):
    import play
    m.violin = []
    m.bass = []
    m.record = []
    m.compresor = []
    play.play(m, "note", note, 0.5 )
    return "<p>play!</p>"
