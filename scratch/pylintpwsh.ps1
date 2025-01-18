$rating = pylint "C:\code\CloudResume\SAM\Lambda\app.py" --disable=C0114,C0115,C0116,E0110,E1101,E1123,R0801,C0103,W0613,W0612
write-output($rating)