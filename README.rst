jabber-bot
====================

Class jabber bot on python

=======
Install
=======

.. code-block:: bash

    pip install jabber-bot


=======
Example
=======

    .. code-block:: python

        import xmpp
        from jabber_bot import JabberBot

        config = {
            'jid': 'username@jabber.org',
            'pass': 'pass'
        }

        def message_handler(conn, mess):
            text = mess.getBody()
            user = mess.getFrom()
            reply = text
            conn.send(xmpp.Message(mess.getFrom(), reply))

        bot = JabberBot(config['jid'], config['pass'])
        bot.register_handler('message', message_handler)
        bot.start()



=======
License
=======

MIT
