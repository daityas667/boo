

#!/usr/bin/env pytho# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():

    start_cmd = ['./webserver', '']
    session = Session(
        target=Target(
            connection=SocketConnection("127.0.0.1", 8888, proto='tcp'),
            procmon=pedrpc.Client("127.0.0.1", 26002),
            procmon_options={"start_commands": [start_cmd]}
        ),
    )

    '''
    HTTP Format:
    GET / HTTP/1.1
    Host: 127.0.0.1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    '''

    s_initialize(name="URI")
    s_static("GET ", name='Method')
    s_delim(" ", name='space-1')
    s_string("/index.html", name='Request-URI')
    s_static("\r\n", name="Request-Line-CRLF-1")

    s_initialize(name="Host")
    s_static("Host: ", name='HostM')
    s_delim(" ", name='space-2')
    s_string("127.0.0.1", name='SetHost')
    s_static("\r\n", name="Request-Line-CRLF-2")

    s_initialize(name="Agent")
    s_static("User-Agent: ", name='UserM')
    s_delim(" ", name='space-3')
    s_string("Mozilla", name='SetAgent')
    s_static("\r\n", name="Request-Line-CRLF-3")

    s_initialize(name="Accept")
    s_static("Accept: ", name='AcceptM')
    s_delim(" ", name='space-4')
    s_string("text/html", name='SetAccept')
    s_static("\r\n", name="Request-Line-CRLF-4")

    s_initialize(name="Language")
    s_static("Accept-Language: ", name='LangM')
    s_delim(" ", name='space-5')
    s_string("en-US,en;q=0.5", name='SetLang')
    s_static("\r\n", name="Request-Line-CRLF-5")

    s_initialize(name="Encoding")
    s_static("Accept-Encoding: ", name='EncM')
    s_delim(" ", name='space-6')
    s_string("gzip, deflate", name='SetEnc')
    s_static("\r\n", name="Request-Line-CRLF-6")

    s_initialize(name="Connection")
    s_static("Connection: ", name='ConnM')
    s_delim(" ", name='space-7')
    s_string("Connection: ", name='SetConn')
    s_static("\r\n", name="Request-Line-CRLF-7")

    s_initialize(name="Requests")
    s_static("Upgrade-Insecure-Requests: ", name='ReqM')
    s_delim(" ", name='space-8')
    s_string("1", name='SetReq')
    s_static("\r\n", name="Request-Line-CRLF-8")

   # s_static("User-Agent: Mozilla\r\n")
   # s_static("Accept: text/html\r\n")
   # s_static("Accept-Language: en-US,en;q=0.5\r\n")
   # s_static("Accept-Encoding: gzip, deflate\r\n")
   # s_static("Connection: keep-alive\r\n")
   # s_static("Upgrade-Insecure-Requests: 1\r\n")

    session.connect(s_get("URI"))
    session.connect(s_get("Host"))
    session.connect(s_get("Agent"))
    session.connect(s_get("Accept"))
    session.connect(s_get("Language"))
    session.connect(s_get("Encoding"))
    session.connect(s_get("Connection"))
    session.connect(s_get("Requests"))
    session.fuzz()


if __name__ == "__main__":
    main()
