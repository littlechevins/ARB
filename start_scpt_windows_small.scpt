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
  end tell
end tell
