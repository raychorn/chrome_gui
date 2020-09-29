__copyright__ = """\
(c). Copyright 2008-2020, Vyper Logix Corp., All Rights Reserved.

Published under Creative Commons License 
(http://creativecommons.org/licenses/by-nc/3.0/) 
restricted to non-commercial educational use only., 

http://www.VyperLogix.com for details

THE AUTHOR VYPER LOGIX CORP DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
WITH THE USE OR PERFORMANCE OF THIS SOFTWARE !

USE AT YOUR OWN RISK.
"""

def getComputerSystem():
    import wmi
    
    from vyperlogix.hash import lists
    
    d = lists.HashedLists2()
    try:
        computer = wmi.WMI()
        blah = computer.Win32_ComputerSystem()[0]
        for name in blah._properties:
            d[name] = eval('blah.%s' % (name))
    except:
        pass
    return d

def getComputerSystemSmartly():
    from vyperlogix.classes import SmartObject
    
    d = getComputerSystem()
    return SmartObject.StrictSmartObject(d)
