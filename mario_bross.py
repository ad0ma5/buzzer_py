
import tones as t

tempo = 0.15

violin = [
        #intro
    t.E4, t.E4, 0   , t.E4 , 0, t.C4, t.E4,
    t.G4, 0   , t.G3, 0,
        #repeat1
    t.C4, 0   , t.G3, 0    , t.E3, 
    0   , t.A3, t.B3, t.AS3, t.A3,
    t.G3, t.E4, t.G4, t.A4 , t.F4, t.G4,
    0   , t.E4, t.C4, t.D4 , t.B3, 0,
        #repeat1
    t.C4, 0   , t.G3, 0    , t.E3, 
    0   , t.A3, t.B3, t.AS3, t.A3,
    t.G3, t.E4, t.G4, t.A4 , t.F4, t.G4,
    0   , t.E4, t.C4, t.D4 , t.B3, 0,
        #repeat2
    0, t.G4 , t.FS4, t.F4, t.DS4, t.E4,
    0, t.GS3, t.A3 , t.C4, 0    , t.A3, t.C4, t.D4,
    0, t.G4 , t.FS4, t.F4, t.DS4, t.E4,
    0, t.C5 , t.C5 , t.C5, 0,

    0, t.G4 , t.FS4, t.F4, t.DS4, t.E4,
    0, t.GS3, t.A3 , t.C4, 0    , t.A3, t.C4, t.D4,
    0, t.DS4, 0    , t.D4, 0,
    t.C4, 0 , 0,
        #repeat2
    0, t.G4 , t.FS4, t.F4, t.DS4, t.E4,
    0, t.GS3, t.A3 , t.C4, 0    , t.A3, t.C4, t.D4,
    0, t.G4 , t.FS4, t.F4, t.DS4, t.E4,
    0, t.C5 , t.C5 , t.C5, 0,

    0, t.G4 , t.FS4, t.F4, t.DS4, t.E4,
    0, t.GS3, t.A3 , t.C4, 0    , t.A3, t.C4, t.D4,
    0, t.DS4, 0    , t.D4, 0,
    t.C4, 0 , 0,
        #norepeat
    t.C4, t.C4, 0, t.C4, 0, t.C4, t.D4,
    t.E4, t.C4, 0, t.A3, t.G3,
    t.C4, t.C4, 0, t.C4, 0, t.C4, t.D4, t.E4,
    0,

    t.C4, t.C4, 0, t.C4, 0, t.C4, t.D4,
    t.E4, t.C4, 0, t.A3, t.G3,
    t.E4, t.E4, 0, t.E4, 0, t.C4, t.E4, 
    t.G4, 0, t.G3, 0, 
        #repeat1
    t.C4, 0   , t.G3, 0    , t.E3, 
    0   , t.A3, t.B3, t.AS3, t.A3,
    t.G3, t.E4, t.G4, t.A4 , t.F4, t.G4,
    0   , t.E4, t.C4, t.D4 , t.B3, 0,
        #repeat1
    t.C4, 0   , t.G3, 0    , t.E3, 
    0   , t.A3, t.B3, t.AS3, t.A3,
    t.G3, t.E4, t.G4, t.A4 , t.F4, t.G4,
    0   , t.E4, t.C4, t.D4 , t.B3, 0,
        #repeat3
    t.E4, t.C4, t.G3, 0, t.GS3,
    t.A3, t.F4, t.F4, t.A3, 0,
    t.B3, t.A4, t.A4, t.A4, t.G4, t.F4,
    t.E4, t.C4, t.A3, t.G3, 0,

    t.E4, t.C4, t.G3, 0, t.GS3,
    t.A3, t.F4, t.F4, t.A3, 0,
    t.B3, t.F4, t.F4, t.F4, t.E4, t.D4,
    t.G3, t.E3, t.E3, t.C3, 0,
        #repeat3
    t.E4, t.C4, t.G3, 0, t.GS3,
    t.A3, t.F4, t.F4, t.A3, 0,
    t.B3, t.A4, t.A4, t.A4, t.G4, t.F4,
    t.E4, t.C4, t.A3, t.G3, 0,

    t.E4, t.C4, t.G3, 0, t.GS3,
    t.A3, t.F4, t.F4, t.A3, 0,
    t.B3, t.F4, t.F4, t.F4, t.E4, t.D4,
    t.G3, t.E3, t.E3, t.C3, 0,
        #norepeat2
    t.C4, t.C4, 0, t.C4, 0, t.C4, t.D4,
    t.E4, t.C4, 0, t.A3, t.G3,
    t.C4, t.C4, 0, t.C4, 0, t.C4, t.D4, t.E4,
    0, t.E4, t.G4, t.E5, t.C5, t.D5, t.G5,

    t.C4, t.C4, 0, t.C4, 0, t.C4, t.D4,
    t.E4, t.C4, 0, t.A3, t.G3,
    t.E4, t.E4, 0   , t.E4 , 0, t.C4, t.E4,
    t.G4, 0   , t.G3, 0,
        #repeat3
    t.E4, t.C4, t.G3, 0, t.GS3,
    t.A3, t.F4, t.F4, t.A3, 0,
    t.B3, t.A4, t.A4, t.A4, t.G4, t.F4,
    t.E4, t.C4, t.A3, t.G3, 0,

    t.E4, t.C4, t.G3, 0, t.GS3,
    t.A3, t.F4, t.F4, t.A3, 0,
    t.B3, t.F4, t.F4, t.F4, t.E4, t.D4,
    t.G3, t.E3, t.E3, t.C3, 0,
        #repeat3
    t.E4, t.C4, t.G3, 0, t.GS3,
    t.A3, t.F4, t.F4, t.A3, 0,
    t.B3, t.A4, t.A4, t.A4, t.G4, t.F4,
    t.E4, t.C4, t.A3, t.G3, 0,

    t.E4, t.C4, t.G3, 0, t.GS3,
    t.A3, t.F4, t.F4, t.A3, 0,
    t.B3, t.F4, t.F4, t.F4, t.E4, t.D4,
    t.G3, t.E3, t.E3, t.C3, 0,
        #outro
    t.C4, 0, t.G3, 0, t.E3,
    t.A3, t.B3, t.A3, t.GS3, t.AS3, t.GS3,
    t.E3, t.D3, t.E3,
    0


]

v_dur  = [ 
        #intro
    1,1,1,1,1,1,2,
    2,2,2,2,
        #repeat1
    2,1,2,1,2,
    1,2,2,1,2,
    2,1,1,2,1,1,
    1,2,1,1,2,1,
        #repeat1
    2,1,2,1,2,
    1,2,2,1,2,
    2,1,1,2,1,1,
    1,2,1,1,2,1,
        #repeat2
    2,1,1,1,2,1,
    1,1,1,1,1,1,1,1,
    2,1,1,1,2,1,
    1,2,1,2,2,

    2,1,1,1,2,1,
    1,1,1,1,1,1,1,1,
    2,2,1,2,1,
    2,2,4,
        #repeat2
    2,1,1,1,2,1,
    1,1,1,1,1,1,1,1,
    2,1,1,1,2,1,
    1,2,1,2,2,

    2,1,1,1,2,1,
    1,1,1,1,1,1,1,1,
    2,2,1,2,1,
    2,2,4,
        #norepeat
    1,1,1,1,1,1,2,
    1,1,1,1,4,
    1,1,1,1,1,1,1,1,
    8,

    1,1,1,1,1,1,2,
    1,1,1,1,4,
    1,1,1,1,1,1,2,
    2,2,2,2,
        #repeat1
    2,1,2,1,2,
    1,2,2,1,2,
    2,1,1,2,1,1,
    1,2,1,1,2,1,
        #repeat1
    2,1,2,1,2,
    1,2,2,1,2,
    2,1,1,2,1,1,
    1,2,1,1,2,1,
        #repeat3
    1,2,1,2,2,
    1,2,1,2,2,
    1,1,2,1,1,2,
    1,2,1,2,2,

    1,2,1,2,2,
    1,2,1,2,2,
    1,2,1,2,1,1,
    1,2,1,2,2,
        #repeat3
    1,2,1,2,2,
    1,2,1,2,2,
    1,1,2,1,1,2,
    1,2,1,2,2,

    1,2,1,2,2,
    1,2,1,2,2,
    1,2,1,2,1,1,
    1,2,1,2,2,
        #norepeat2
    1,1,1,1,1,1,2,
    1,1,1,1,4,
    1,1,1,1,1,1,1,1,
    2,1,1,1,1,1,1,

    1,1,1,1,1,1,2,
    1,1,1,1,4,
    1,1,1,1,1,1,2,
    2,2,2,2,
        #repeat3
    1,2,1,2,2,
    1,2,1,2,2,
    1,1,2,1,1,2,
    1,2,1,2,2,

    1,2,1,2,2,
    1,2,1,2,2,
    1,2,1,2,1,1,
    1,2,1,2,2,
        #repeat3
    1,2,1,2,2,
    1,2,1,2,2,
    1,1,2,1,1,2,
    1,2,1,2,2,

    1,2,1,2,2,
    1,2,1,2,2,
    1,2,1,2,1,1,
    1,2,1,2,2,
        #outro
    2,1,2,1,2,
    1,1,2,1,1,2,
    1,1,6,
    8
]

bass   = [ 
        #intro
    t.D2, t.D2, 0   , t.D2 , 0, t.D2, t.D2,
    t.G2, 0   , t.G1, 0,
        #repeat1
    t.G2, 0   , t.E2, 0    , t.C2, 
    0   , t.F2, t.G2, t.FS2, t.F2,
    t.E2, t.C3, t.E3, t.F3 , t.D3, t.E3,
    0   , t.C3, t.A2, t.B2 , t.G2, 0,
        #repeat1
    t.G2, 0   , t.E2, 0    , t.C2, 
    0   , t.F2, t.G2, t.FS2, t.F2,
    t.E2, t.C3, t.E3, t.F3 , t.D3, t.E3,
    0   , t.C3, t.A2, t.B2 , t.G2, 0,
        #repeat2
    t.C2, 0, t.G2, 0, t.C3,
    t.F2, 0, t.C3, t.C2, t.F2,
    t.C2, 0, t.G2, 0, t.G2, t.C3,
    0, t.G3, t.G3, t.G3, t.G2,

    t.C2, 0, t.G2, 0, t.C3,
    t.F2, 0, t.C3, t.C2, t.F2,
    t.C2, t.GS2, 0, t.AS2, 0,
    t.C3, 0, t.G2, t.G2, t.C2,
        #repeat2
    t.C2, 0, t.G2, 0, t.C3,
    t.F2, 0, t.C3, t.C2, t.F2,
    t.C2, 0, t.G2, 0, t.G2, t.C3,
    0, t.G3, t.G3, t.G3, t.G2,

    t.C2, 0, t.G2, 0, t.C3,
    t.F2, 0, t.C3, t.C2, t.F2,
    t.C2, t.GS2, 0, t.AS2, 0,
    t.C3, 0, t.G2, t.G2, t.C2,
        #norepeat
    t.GS1, 0, t.DS2, 0, 0, t.GS2, 
    t.G2 , 0, t.C2 , 0, t.G1,
    t.GS1, 0, t.DS2, 0, 0, t.GS2, 
    t.G2 , 0, t.C2 , 0, t.G1,

    t.GS1, 0, t.DS2, 0, 0, t.GS2, 
    t.G2 , 0, t.C2 , 0, t.G1,
    t.D2, t.D2, 0   , t.D2 , 0, t.D2, t.D2,
    t.G2, 0   , t.G1, 0,

        #repeat1
    t.G2, 0   , t.E2, 0    , t.C2, 
    0   , t.F2, t.G2, t.FS2, t.F2,
    t.E2, t.C3, t.E3, t.F3 , t.D3, t.E3,
    0   , t.C3, t.A2, t.B2 , t.G2, 0,
        #repeat1
    t.G2, 0   , t.E2, 0    , t.C2, 
    0   , t.F2, t.G2, t.FS2, t.F2,
    t.E2, t.C3, t.E3, t.F3 , t.D3, t.E3,
    0   , t.C3, t.A2, t.B2 , t.G2, 0,
        #repeat3
    t.C2, 0, t.FS2, t.G2, t.C3,
    t.F2, t.F2, t.C3, t.C3, t.F2,
    t.D2, 0, t.F2, t.G2, t.B2,
    t.F2, t.F2, t.C3, t.C3, t.F2,

    t.C2, 0, t.FS2, t.G2, t.C3,
    t.F2, t.F2, t.C3, t.C3, t.F2,
    t.G2,t.G2,t.G2,t.G2,t.A2,t.B2,
    t.C3, t.G2, t.C2, 0,
        #repeat3
    t.C2, 0, t.FS2, t.G2, t.C3,
    t.F2, t.F2, t.C3, t.C3, t.F2,
    t.D2, 0, t.F2, t.G2, t.B2,
    t.F2, t.F2, t.C3, t.C3, t.F2,

    t.C2, 0, t.FS2, t.G2, t.C3,
    t.F2, t.F2, t.C3, t.C3, t.F2,
    t.G2,t.G2,t.G2,t.G2,t.A2,t.B2,
    t.C3, t.G2, t.C2, 0,
        #norepeat2
    t.GS1, 0, t.DS2, 0, 0, t.GS2,
    t.G2, 0, t.C2, 0, t.G1,
    t.GS1, 0, t.DS2, 0,0, t.GS2,
    t.G2, 0, t.C2, 0, t.G1,

    t.GS1, 0, t.DS2, 0,0, t.GS2,
    t.G2, 0, t.C2, 0, t.G1,
    t.D2, t.D2, 0   , t.D2 , 0, t.D2, t.D2,
    t.G2, 0   , t.G1, 0,
        #repeat3
    t.C2, 0, t.FS2, t.G2, t.C3,
    t.F2, t.F2, t.C3, t.C3, t.F2,
    t.D2, 0, t.F2, t.G2, t.B2,
    t.F2, t.F2, t.C3, t.C3, t.F2,

    t.C2, 0, t.FS2, t.G2, t.C3,
    t.F2, t.F2, t.C3, t.C3, t.F2,
    t.G2,t.G2,t.G2,t.G2,t.A2,t.B2,
    t.C3, t.G2, t.C2, 0,
        #repeat3
    t.C2, 0, t.FS2, t.G2, t.C3,
    t.F2, t.F2, t.C3, t.C3, t.F2,
    t.D2, 0, t.F2, t.G2, t.B2,
    t.F2, t.F2, t.C3, t.C3, t.F2,

    t.C2, 0, t.FS2, t.G2, t.C3,
    t.F2, t.F2, t.C3, t.C3, t.F2,
    t.G2,t.G2,t.G2,t.G2,t.A2,t.B2,
    t.C3, t.G2, t.C2, 0,
        #outro
    t.G2, 0, t.E2, 0, t.C2,
    t.F2, t.CS2,
    t.C2,
    0
]

b_dur  = [ 
        #intro
    1,1,1,1,1,1,2,
    2,2,2,2,
        #repeat1
    2,1,2,1,2,
    1,2,2,1,2,
    2,1,1,2,1,1,
    1,2,1,1,2,1,
        #repeat1
    2,1,2,1,2,
    1,2,2,1,2,
    2,1,1,2,1,1,
    1,2,1,1,2,1,
        #repeat2
    2,1,1,2,2,
    2,1,1,2,2,
    2,1,1,2,1,1,
    1,2,1,2,2,

    2,1,1,2,2,
    2,1,1,2,2,
    2,2,1,2,1,
    2,1,1,2,2,
        #repeat2
    2,1,1,2,2,
    2,1,1,2,2,
    2,1,1,2,1,1,
    1,2,1,2,2,

    2,1,1,2,2,
    2,1,1,2,2,
    2,2,1,2,1,
    2,1,1,2,2,
        #norepeat
    2,1,1,1,1,2,
    2,1,1,2,2,
    2,1,1,1,1,2,
    2,1,1,2,2,

    2,1,1,1,1,2,
    2,1,1,2,2,
    1,1,1,1,1,1,2,
    2,2,2,2,
        #repeat1
    2,1,2,1,2,
    1,2,2,1,2,
    2,1,1,2,1,1,
    1,2,1,1,2,1,
        #repeat1
    2,1,2,1,2,
    1,2,2,1,2,
    2,1,1,2,1,1,
    1,2,1,1,2,1,
        #repeat3
    2,1,1,2,2,
    2,2,1,1,2,
    2,1,1,2,2,
    2,2,1,1,2,

    2,1,1,2,2,
    2,2,1,1,2,
    1,2,1,2,1,1,
    2,2,2,2,
        #repeat3
    2,1,1,2,2,
    2,2,1,1,2,
    2,1,1,2,2,
    2,2,1,1,2,

    2,1,1,2,2,
    2,2,1,1,2,
    1,2,1,2,1,1,
    2,2,2,2,
        #norepeat2
    2,1,1,1,1,2,
    2,1,1,2,2,
    2,1,1,1,1,2,
    2,1,1,2,2,

    2,1,1,1,1,2,
    2,1,1,2,2,
    1,1,1,1,1,1,2,
    2,2,2,2,
        #repeat3
    2,1,1,2,2,
    2,2,1,1,2,
    2,1,1,2,2,
    2,2,1,1,2,

    2,1,1,2,2,
    2,2,1,1,2,
    1,2,1,2,1,1,
    2,2,2,2,
        #repeat3
    2,1,1,2,2,
    2,2,1,1,2,
    2,1,1,2,2,
    2,2,1,1,2,

    2,1,1,2,2,
    2,2,1,1,2,
    1,2,1,2,1,1,
    2,2,2,2,
        #outro
    2,1,2,1,2,
    4,4,
    8,
    8
]
record = []
r_dur = []
compresor = []
c_dir = []
guitar = []
g_dur = []
