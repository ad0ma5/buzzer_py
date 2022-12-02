import tones as t

tempo = 0.15

violin = [ 
t.G4 , t.G4, t.G4, t.DS4, t.AS4, 
t.G4 , t.DS4, t.AS4, t.G4      , 
t.D5 , t.D5, t.D5, t.DS5, t.AS4, 
t.FS4, t.DS4, t.AS4, t.G4      , 

t.G5, t.G4, t.G4, t.G5, t.FS5, t.F5, 
t.E5, t.DS5, t.E5, 0, t.GS4, t.CS5, t.C5, t.B4, 
t.AS4, t.A4, t.AS4, 0, t.DS4, t.FS4, t.DS4, t.G4, 
t.AS4, t.G4, t.AS4, t.D5        , 

t.G5, t.G4, t.G4, t.G5, t.FS5, t.F5, 
t.E5, t.DS5, t.E5, 0, t.GS4, t.CS5, t.C5, t.B4, 
t.AS4, t.A4, t.AS4, 0, t.DS4, t.FS4, t.DS4, t.AS4, 
t.G4, t.DS4, t.AS4, t.G4  
]

bass   = [ 
t.G3, t.G3, t.G3, t.DS3  , 
t.G3, t.DS3 , t.G3, t.G3, 
t.G3, t.G3, t.G3, t.DS3 , 
t.DS3 , t.DS3 , t.G3, t.G3,

t.G3, t.G3, t.G3, t.G3,
t.CS3, t.CS3, t.CS3, t.CS3,
t.DS3, t.DS3, t.DS3, t.DS3,
t.G3, t.DS3, t.G3, t.G3,

t.DS3, t.DS3, t.G3, t.G3,
t.CS3, t.CS3, t.CS3, t.CS3,
t.DS3, t.DS3, t.DS3, t.DS3,
t.G3, t.DS3, t.G3
]

v_dur  = [ 
4, 4, 4, 3, 1, 
4, 3, 1, 8, 
4, 4, 4, 3, 1, 
4, 3, 1, 8,

4, 3, 1, 4, 3, 1,
1, 1, 2, 2, 2, 4, 3, 1,
1, 1, 2, 2, 2, 4, 3, 1,
4, 3, 1, 8,

4, 3, 1, 4, 3, 1,
1,1,2, 2, 2,4,3,1,
1,1,2, 2, 2,4,3,1,
4,3,1,8

]

b_dur  = [ 
4, 4, 4, 4, 
4, 4, 4, 4, 
4, 4, 4, 4, 
4, 4, 4, 4,

4, 4, 4, 4, 
4, 4, 4, 4, 
4, 4, 4, 4, 
4, 4, 4, 4,

4, 4, 4, 4, 
4, 4, 4, 4, 
4, 4, 4, 4, 
4, 4, 8

]

record = []
compresor = []
