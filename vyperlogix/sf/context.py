__copyright__ = """\
(c). Copyright 2008-2014, Vyper Logix Corp., All Rights Reserved.

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

def getSalesForceContext():
    from vyperlogix.decorators import addto
    from pyax.context import Context

    _ctx = Context()

    @addto.addto(_ctx)
    def get__login_servers(self):
	try:
	    return self.__dict__['_Context__login_servers']
	except:
	    pass
	return []
    
    return _ctx

if __name__ == "__main__":
    import sys
    print >>sys.stdout, __copyright__
    print >>sys.stderr, __copyright__
