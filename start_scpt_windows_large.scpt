tell application "iTerm2"
  tell current window
    set newTab0 to (create tab with default profile)
    tell current session of newTab0
      write text "echo exporting flask app"
      write text "python node.py -n node_1 -ip 5001 -t backbone"
    end tell
    set newTab1 to (create tab with default profile)
    tell current session of newTab1
      write text "echo exporting flask app"
      write text "python node.py -n node_2 -ip 5002 -t backbone"
    end tell
    set newTab2 to (create tab with default profile)
    tell current session of newTab2
      write text "echo exporting flask app"
      write text "python node.py -n node_3 -ip 5003 -t backbone"
    end tell
    set newTab3 to (create tab with default profile)
    tell current session of newTab3
      write text "echo exporting flask app"
      write text "python node.py -n node_4 -ip 5004 -t backbone"
    end tell
    set newTab4 to (create tab with default profile)
    tell current session of newTab4
      write text "echo exporting flask app"
      write text "python node.py -n node_5 -ip 5005 -t end"
    end tell
    set newTab5 to (create tab with default profile)
    tell current session of newTab5
      write text "echo exporting flask app"
      write text "python node.py -n node_6 -ip 5006 -t end"
    end tell
    set newTab6 to (create tab with default profile)
    tell current session of newTab6
      write text "echo exporting flask app"
      write text "python node.py -n node_7 -ip 5007 -t end"
    end tell
    set newTab7 to (create tab with default profile)
    tell current session of newTab7
      write text "echo exporting flask app"
      write text "python node.py -n node_8 -ip 5008 -t end"
    end tell
    set newTab8 to (create tab with default profile)
    tell current session of newTab8
      write text "echo exporting flask app"
      write text "python node.py -n node_9 -ip 5009 -t end"
    end tell
    set newTab10 to (create tab with default profile)
    tell current session of newTab10
      write text "echo exporting flask app"
      write text "python node.py -n node_10 -ip 5010 -t end"
    end tell
    set newTab11 to (create tab with default profile)
    tell current session of newTab11
      write text "echo exporting flask app"
      write text "python node.py -n node_11 -ip 5011 -t end"
    end tell
    set newTab12 to (create tab with default profile)
    tell current session of newTab12
      write text "echo exporting flask app"
      write text "python node.py -n node_12 -ip 5012 -t end"
    end tell
    set newTab13 to (create tab with default profile)
    tell current session of newTab13
      write text "echo exporting flask app"
      write text "python node.py -n node_13 -ip 5013 -t end"
    end tell
    set newTab14 to (create tab with default profile)
    tell current session of newTab14
      write text "echo exporting flask app"
      write text "python node.py -n node_14 -ip 5014 -t end"
    end tell
    set newTab15 to (create tab with default profile)
    tell current session of newTab15
      write text "echo exporting flask app"
      write text "python node.py -n node_15 -ip 5015 -t end"
    end tell
    set newTab16 to (create tab with default profile)
    tell current session of newTab16
      write text "echo exporting flask app"
      write text "python node.py -n node_16 -ip 5016 -t end"
    end tell
    set newTab17 to (create tab with default profile)
    tell current session of newTab17
      write text "echo exporting flask app"
      write text "python node.py -n node_17 -ip 5017 -t end"
    end tell
    set newTab18 to (create tab with default profile)
    tell current session of newTab18
      write text "echo exporting flask app"
      write text "python node.py -n node_18 -ip 5018 -t end"
    end tell
    set newTab19 to (create tab with default profile)
    tell current session of newTab19
      write text "echo exporting flask app"
      write text "python node.py -n node_19 -ip 5019 -t end"
    end tell
    set newTab20 to (create tab with default profile)
    tell current session of newTab20
      write text "echo exporting flask app"
      write text "python node.py -n node_20 -ip 5020 -t end"
    end tell
  end tell
end tell
