import banner
import struct
import argparse
import zlib
import os
import re
import sys

def str2hex(str):
    return str.encode('hex').upper()

def int2hex(n):
    return '0x'+hex(n)[2:].upper()

def str2num(str, n=0):
    """
    The str2num function takes two arguments: str and n. The str argument represents the binary data stored as a string, 
    and n is an optional parameter that specifies the number of bytes to convert. By default, n is set to 0.
    """
    if n == 4:
        # '!' denotes network byte order (big-endian) and 'I' denotes an unsigned integer of 4 bytes (32 bits).
        return struct.unpack('!I', str)[0]
    else:
        return eval('0x'+str2hex(str))

def WriteFile(filename):
    if os.path.isfile(filename)==True:
        os.remove(filename)
    # The + character in the mode string indicates that the file should be opened in a mode that allows both reading and writing operations.
    file = open(filename, 'wb+')
    return file

def ReadFile(filename):
    try:
        with open(filename, 'rb') as file:
            data = file.read()
    except IOError as e:
        print(banner.red + f'[-]{e}')
        return -1
    return data

class PNG(object):
    def __init__(self, in_file='', out_file='output.png', choices='', mode=0):
        self.in_file = in_file
        self.out_file = out_file
        self.choices = choices
        self.i_mode = mode
    
    def __del__(self):
        try:
            self.file.close()
        # This typically occurs when you make a mistake in the attribute or method name, or when you're trying to access an attribute that is not defined for the object.
        except AttributeError:
            pass

    def AddPayload(self, name, payload, way):
        pass
    def MakeCritical(self, name, payload):
        pass
    def MakeAncillary(self, name, payload):
        pass
    def RanAncillaryName(self):
        pass
    def GetPicInfo(self, ihdr=''):
        pass
    def PrintPicInfo(self):
        pass
    def ClearFilter(self, idat, width, height, challen, bits=8):
        pass
    def zlib_decrypt(self, data):
        pass
    def LoadPNG(self):
        pass
    def DecompressPNG(self, data, channel=3, bits=8, width=1, height=1):
        pass
    def FindAncillary(self, data):
        pass
    def CheckPNG(self):
        pass
    def CheckCRC(self, chunk_type, chunk_data, checksum):
        pass
    def CheckFormat(self, data):
        pass
    def CheckHeader(self, data):
        pass
    def FindIHDR(self, data):
        pass
    def CheckIHDR(self, data):
        pass
    def CheckIDAT(self, data):
        pass
    def FixDos2Unix(self, chunk_type, chunk_data, crc, count):
        pass
    def CheckIEND(self, data):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quiet', action='store_true', help="dont show the banner information")
    parser.add_argument('-y', '--yes', action='store_true', help='auto choose yes')
    parser.add_argument('-v', '--verbose', action='store_true', help='use the safe way to recover')
    parser.add_argument('-m', '--message', action='store_true', help='show the image information')
    parser.add_argument('-n', '--name', metavar='', help='payload name [Default: random]')
    parser.add_argument('-p', help='payload to hide')
    parser.add_argument('-w', type=int, default=1, help='payload chunk: [1]: ancillary [2]: critical [Default: 1]')
    parser.add_argument('-d', help='decompress zlib data file name')
    parser.add_argument('-i', help='Input file name (*.png) [Select from terminal]')
    parser.add_argument('-f', help='Input file name (*.png) [Select from window]')
    parser.add_argument('-o', default='output.png', help='Output repareid file name [Default: output.png]')
    args = parser.parse_args()

    in_file = args.i
    out_file = args.o
    payload = args.p
    payload_name = args.name     
    z_file = args.d
    
    if args.quiet != True:
        banner.banner()

    if z_file != None:
        z_data = ReadFile(z_file)       # User defined ReadFile() function
        my_png = PNG()
        my_png.DecompressPNG(z_data, width=0, height=0)
    else:
        if args.verbose == True:
            mode = 1
        else:
            mdoe = 0
        if args.f == True:
            try:
                import tkinter
                import tkinter.filedialog
                root = tkinter.Tk()
                in_file = tkinter.filedialog.askopenfilename()
                root.destroy()
                if args.yes == True:
                    my_png = PNG(in_file, out_file, choices='y', mode=mode)
                else:
                    my_png = PNG(in_file, out_file, mode=mode)
                if args.message == True:
                    my_png.PrintPicInfo()
                elif payload != None:
                    way = args.way
                    my_png.AddPayload(payload_name, payload, way)
                else:
                    my_png.CheckPNG()
            except ImportError as e:
                print(banner.red + f'[-]{e}')
                print("Try 'pip install tk' to use it" + banner.reset)
        elif in_file != None:
            if args.yes == True:
                my_png = PNG(in_file, out_file, choices='y', mode=mode)
            else:
                my_png = PNG(in_file, out_file, mode=mode)
            if args.message == True:
                my_png.PrintPicInfo()
            elif payload != None:
                way = args.way
                my_png.AddPayload(payload_name, payload, way)
            else:
                my_png.CheckPNG()
        else:
            parser.print_help()
        