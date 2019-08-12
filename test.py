from cpt.cpt import Cpt
model = Cpt()

model.fit([['hello', 'world'],
           ['hello', 'this', 'is', 'me'],
           ['hello', 'me']
          ])

model.predict([['hello'], ['hello', 'this']])
