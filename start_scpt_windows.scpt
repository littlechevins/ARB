tell application "iTerm2"
  tell current window
    set newTab0 to (create tab with default profile)
    tell current session of newTab0
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5000"
    end tell
    set newTab1 to (create tab with default profile)
    tell current session of newTab1
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5001"
    end tell
    set newTab2 to (create tab with default profile)
    tell current session of newTab2
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5002"
    end tell
    set newTab3 to (create tab with default profile)
    tell current session of newTab3
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5003"
    end tell
    set newTab4 to (create tab with default profile)
    tell current session of newTab4
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5004"
    end tell
    set newTab5 to (create tab with default profile)
    tell current session of newTab2
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5005"
    end tell
    set newTab6 to (create tab with default profile)
    tell current session of newTab6
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5006"
    end tell
    set newTab7 to (create tab with default profile)
    tell current session of newTab7
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5007"
    end tell
    set newTab8 to (create tab with default profile)
    tell current session of newTab8
      write text "echo exporting flask app"
      write text "export FLASK_APP=node.py"
      write text "python -m flask run -p 5008"
    end tell
  end tell
end tell
