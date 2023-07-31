"""

tell() -   return current position of file pointer
seek() -   reset the position of file pointer

***************************************************************

tell()
It returns an integer giving the file pointer current position in the file represented as a number
of bytes. File Pointer/File Handler is like a cursor, which defines from where the data has to be read
or written in the file. Sometimes it becomes important for us to know the position of the File Pointer.
With the help of tell(), this task can be performed easily

Syntax:  tell()
Parameters Required: No parameters are required.
Return Value:  tell() function returns the current position of the file pointer within the file.

*****************************************************************

seek():
When we open a file, the system points to the beginning of the file. Any read or write will happen from
the start. To change the file object’s position, use seek(offset, whence) function. The position will compute
by adding offset to a reference point, and the whence argument selects the reference point. It is useful
when operating over an open file. If we want to read the file but skip the first 5 bytes, open the file,
use function seek(5) to move to where you want to start reading, and then continue reading the file.

Description:
Syntax:  file_pointer .seek(offset, whence).
Offset:  In seek() function, offset is required. Offset is the position of the read/write pointer within the file.
Whence: This is optional. It defines the point of reference. The default is 0, which means absolute file positioning.

Value   Meaning
0   Absolute file positioning. The position is relative to the start of the file. The first argument cannot be negative.
1   Seek relative to the current position. The first argument can be negative to move backward or positive to move forward
2   Seek relative to the file’s end. The first argument must be negative.

*******************

The seek(offset[, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved.
The from argument specifies the reference position from where the bytes are to be moved.

If from is set to 0, it means use the beginning of the file as the reference position and
1 means use the current position as the reference position and if it is set to 2 then the end of the file would be taken as the reference position.

Example

"""

f = open("test.txt")
f.seek(0)

print(f.tell())
print(f.readline(), end="")
print(f.tell())              # the file pointer updated after read operation

print(f.readline(), end="")
print(f.tell())
f.close()

# ******************

#  To perform end-relative seeks in a text file, you need to use 'r+' mode.
# However, it's worth noting that even with 'r+' mode,
# you cannot perform end-relative seeks with the f.seek() method.

#  The f.seek() method in text mode only allows you to seek from the beginning of the file (0).

