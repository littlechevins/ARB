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
      write text "python node.py -n Lugoj -ip 5005 -t end"
    end tell
    set newTab6 to (create tab with default profile)
    tell current session of newTab6
      write text "echo exporting flask app"
      write text "python node.py -n Mehadia -ip 5006 -t end"
    end tell
    set newTab7 to (create tab with default profile)
    tell current session of newTab7
      write text "echo exporting flask app"
      write text "python node.py -n Drobeta -ip 5007 -t end"
    end tell
    set newTab8 to (create tab with default profile)
    tell current session of newTab8
      write text "echo exporting flask app"
      write text "python node.py -n Craiova -ip 5008 -t end"
    end tell
    set newTab9 to (create tab with default profile)
    tell current session of newTab9
      write text "echo exporting flask app"
      write text "python node.py -n Pitesti -ip 5009 -t end"
    end tell
    set newTab10 to (create tab with default profile)
    tell current session of newTab10
      write text "echo exporting flask app"
      write text "python node.py -n Rimnicu Vilea -ip 5010 -t end"
    end tell
    set newTab11 to (create tab with default profile)
    tell current session of newTab11
      write text "echo exporting flask app"
      write text "python node.py -n Sibiu -ip 5011 -t end"
    end tell
    set newTab12 to (create tab with default profile)
    tell current session of newTab12
      write text "echo exporting flask app"
      write text "python node.py -n Fagaras -ip 5012 -t end"
    end tell
  end tell
end tell
