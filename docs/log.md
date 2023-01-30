# Logging
here we explain about our logs
___
## multigames.py
___
### main
- Start the program
- Inside the main loop
    - If the user entered -register
      - ### register
        - Inside the register loop
        - If the user entered unauthorized command
        - If the user entered -return
        - If the user did not follow the written rules
        - If the user did not followed the password rules
        - The user successfully registered
        - If the user entered Duplicate Username
    - If the user entered -login
      - ### login
        - Inside the login loop
        - If the user entered unauthorized command
        - If the user entered -return
        - username login
          - ### select games
            - Inside the select games loop
            - If the user entered unauthorized command
            - If the user entered -logout
            - entered -hm
            - entered -ttt
            - entered -dad
              - ### Dungeon and dragon
                - inside the loop levels d&d
                - If the user entered unauthorized command
                - If the user entered -adv
                - If the user entered -return
                - entered -easy -normal or -hard
                - The user is ready to play
                - After hitting enter by counting 1 2 3
                - [From now on, the game log will be saved in another file]
                  - The user has entered the game
                  - Map and position of player and dragon
                  - Change player position
                  - If possible, change the position of the dragon
                  - Winning and losing
                  - Use game hints
        - If the password is wrong or username
    - If the user entered -help
    - If the user entered -exit
    - If the user entered unauthorized command
    - end the program