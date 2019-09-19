tell application "iTerm2"
  tell current window
    set newTab1 to (create tab with default profile)
    tell current session of newTab1
      write text "echo exporting flask app"
      write text "python node.py -n Oradea -ip 5001 -t backbone"
    end tell
    set newTab2 to (create tab with default profile)
    tell current session of newTab2
      write text "echo exporting flask app"
      write text "python node.py -n Zerind -ip 5002 -t backbone"
    end tell
    set newTab3 to (create tab with default profile)
    tell current session of newTab3
      write text "echo exporting flask app"
      write text "python node.py -n Arad -ip 5003 -t backbone"
    end tell
    set newTab4 to (create tab with default profile)
    tell current session of newTab4
      write text "echo exporting flask app"
      write text "python node.py -n Timisoara -ip 5004 -t backbone"
    end tell
    set newTab5 to (create tab with default profile)
    tell current session of newTab5
      write text "echo exporting flask app"
      write text "python node.py -n Lugoj -ip 5005 -t backbone"
    end tell
    set newTab6 to (create tab with default profile)
    tell current session of newTab6
      write text "echo exporting flask app"
      write text "python node.py -n Mehadia -ip 5006 -t backbone"
    end tell
    set newTab7 to (create tab with default profile)
    tell current session of newTab7
      write text "echo exporting flask app"
      write text "python node.py -n Drobeta -ip 5007 -t backbone"
    end tell
    set newTab8 to (create tab with default profile)
    tell current session of newTab8
      write text "echo exporting flask app"
      write text "python node.py -n Craiova -ip 5008 -t backbone"
    end tell
    set newTab9 to (create tab with default profile)
    tell current session of newTab9
      write text "echo exporting flask app"
      write text "python node.py -n Pitesti -ip 5009 -t backbone"
    end tell
    set newTab10 to (create tab with default profile)
    tell current session of newTab10
      write text "echo exporting flask app"
      write text "python node.py -n Rimnicu_Vilcea -ip 5010 -t backbone"
    end tell
    set newTab11 to (create tab with default profile)
    tell current session of newTab11
      write text "echo exporting flask app"
      write text "python node.py -n Sibiu -ip 5011 -t backbone"
    end tell
    set newTab12 to (create tab with default profile)
    tell current session of newTab12
      write text "echo exporting flask app"
      write text "python node.py -n Fagaras -ip 5012 -t backbone"
    end tell
    set newTab13 to (create tab with default profile)
    tell current session of newTab13
      write text "echo exporting flask app"
      write text "python node.py -n Bucharest -ip 5013 -t backbone"
    end tell
    set newTab14 to (create tab with default profile)
    tell current session of newTab14
      write text "echo exporting flask app"
      write text "python node.py -n Giurgiu -ip 5014 -t backbone"
    end tell
    set newTab15 to (create tab with default profile)
    tell current session of newTab15
      write text "echo exporting flask app"
      write text "python node.py -n Urziceni -ip 5015 -t backbone"
    end tell
    set newTab16 to (create tab with default profile)
    tell current session of newTab16
      write text "echo exporting flask app"
      write text "python node.py -n Hirsova -ip 5016 -t backbone"
    end tell
    set newTab17 to (create tab with default profile)
    tell current session of newTab17
      write text "echo exporting flask app"
      write text "python node.py -n Eforie -ip 5017 -t backbone"
    end tell
    set newTab18 to (create tab with default profile)
    tell current session of newTab18
      write text "echo exporting flask app"
      write text "python node.py -n Vaslui -ip 5018 -t backbone"
    end tell
    set newTab19 to (create tab with default profile)
    tell current session of newTab19
      write text "echo exporting flask app"
      write text "python node.py -n Iasi -ip 5019 -t backbone"
    end tell
    set newTab20 to (create tab with default profile)
    tell current session of newTab20
      write text "echo exporting flask app"
      write text "python node.py -n Neamt -ip 5020 -t backbone"
    end tell
  end tell
end tell
