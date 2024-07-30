print('''
             ._
          .-'  `-.
       .-'        \\
      ;    .-'\\    ;
      `._.'    ;   |
               |   |
               ;   :
              ;   :
              ;   :
             /   /
            ;   :                   ,
            ;   |               .-"7|
          .-'"  :            .-' .' :
       .-'       \         .'  .'   `.
     .'           `-. ""-.-'`""    `",`-._..--"7
     ;    .          `-.J `-,    ;"`.;|,_,    ;
   _.'    |         `"" `. ."""--. o \:.-. _.'
.""       :            ,--`;   ,  `--/}o,' ;
;   .___.'        /     ,--.`-. `-..7_.-  /_
 \   :   `..__.._;    .'__;    `---..__.-'-.`"-,
 .'   `--. |   \_;    \'   `-._.-")     \\  `-,
 `.   -.`_):      `.   `-"""`.   ;__.' ;/ ;   "
   `-.__7"  `-..._.'`7     -._;'  ``"-''
                     `--.,__.'     
''')

print("Welcome to play with cat game!")
print("Your mission is to pleasure the cat.")

choice1 = input('Which cat\'s ear will you scratch? Type "left" or "right"\n.').lower()

if choice1 == "left":
   choice2 = input('The cat purrs happily. Do you want to "pet" the cat or "play" with a toy?\n').lower()
   if choice2 == "pet":
      choice3 = input('The cat enjoys the petting. Do you want to "continue" petting or "stop"?\n').lower()
      if choice3 == "continue":
         print("The cat loves the attention. You win!")
      elif choice3 == "stop":
         print("The cat is satisfied and curls up to sleep. You win!")
      else:
         print("Invalid choice. Game over.")
   elif choice2 == "play":
      choice3 = input('The cat chases the toy. Do you want to "throw" the toy again or "stop" playing?\n').lower()
      if choice3 == "throw":
         print("The cat is having fun. You win!")
      elif choice3 == "stop":
         print("The cat looks around for more fun. You win!")
      else:
         print("Invalid choice. Game over.")
   else:
       print("Invalid choice. Game over.")

else:
   print("Game over because cat got mad.")


