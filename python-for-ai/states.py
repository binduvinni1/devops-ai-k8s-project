with open("states.json", 'r') as jf:
    with open("states_copy.json", 'w') as jfw:
        jfw.write(jf.read())

        