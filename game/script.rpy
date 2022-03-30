label start:
    call Init_Variables
    $ Playing = True
    while Playing:
        menu:
            c "Hi"
            "HI":
                pass
            "Bye":
                $ Playing = False
        call screen tutScreen("Test \nnew line")
    return
