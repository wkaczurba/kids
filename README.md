# kids

Simple audio program to code and teach Polish alphabet.

## Realease issues:

The code uses `getch` library:
 - it may not work under Windows 10+; consider using msvcrt as an alternative
 - for Linux/Raspberry Pi: Tony Python has problems running getch() in command terminal, so use VisualCode instead.

## Running in visual code - tips.

Since visual code runs python in the main project folder - it might be tricky to get the current directory correct,
and so audio files may not be accessible

To sort this out: add `"cwd": "${fileDirname}"`


```json
"configurations": [
    {
        "name": "Python: Current File",
        "type": "python",
        "request": "launch",
        "program": "${file}",
        "console": "integratedTerminal",
        "justMyCode": true,
        "cwd": "${fileDirname}"
    }
]
```

