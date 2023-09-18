from flask import Flask

import tones as m
app = Flask(__name__)

@app.route("/")
def hello_world():
    rest = ""
    m_keys = dir(m)
    mm = {} 
    for mk in m_keys:
        print(mk)
        mm[mk] = getattr(m,mk)
        print(mm[mk])
    ns = sorted(mm, key=lambda x: x, reverse=False)
    notes = dir(ns)
    for note_k in m_keys:
        if not note_k.startswith("__"):
            note = mm[note_k]
            rest = rest + "<div onclick=\"play('"+str(note_k)+"')\" >"+str(note_k)+"</div>"
    return '''
    <p>Hello, World!</p>
    <script>
    function play(note){
      fetch("play/"+note);
    }
    function plays(note){
      fetch("plays/"+note);
    }
    function playm(note){
      fetch("playm/"+note);
    }
    alert('ok')
    </script>
    <style>div{display: inline-block; margin: 30px }</style>
    <button onclick="plays('gon')">Play guitar</button>
    <button onclick="plays('rec')">Play record</button>
    <button onclick="plays('com1')">Play compresor slow</button>
    <button onclick="plays('com2')">Play compresor medium</button>
    <button onclick="plays('com3')">Play compresor fast</button>
    <button onclick="playm('imperial_marsh')">Play Imperial March</button>
    <button onclick="playm('mario_bross')">Play Mario Bross</button>
    <button onclick="playm('mario')">Play Mario Underworld</button>
    <button onclick="playm('click')">Play Click</button>
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
@app.route("/playm/<note>")
def play_m(note):
    import importlib
    import play
    loader = importlib.util.find_spec( note)
    if loader is not None:
        m = importlib.import_module( note ) #as m
    else:
        print("not found exit")
    play.play(m, note )
    return "<p>play!</p>"
@app.route("/plays/<note>")
def play_s(note):
    import play
    play.play(m, "serial", note, 1 , True)
    return "<p>play!</p>"

