import sys
import xmpp

class JabberBot:

    def __init__(self, jid, password):
        jid = xmpp.JID(jid)
        self.user, self.server, self.password = jid.getNode(), jid.getDomain(), password
        self.connect()
        self.auth()

    def connect(self):
        self.conn = xmpp.Client(self.server, debug=[])
        conn_result = self.conn.connect()
        if not conn_result:
            print "Can't connect to server"
        sys.exit(1)

    def auth(self):
        auth_result = self.conn.auth(self.user, self.password)
        if not auth_result:
            print "Can't to authorize"
        sys.exit(1)

    def register_handler(self, name, handler):
        self.conn.RegisterHandler(name, handler)

    def step_on(self):
        try:
            self.conn.Process(1)
        except KeyboardInterrupt:
            return 0
        return 1

    def start(self):
        self.conn.sendInitPresence()
        print "Started"
        while self.step_on():
            pass
