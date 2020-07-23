#!/bin/bash
if [ -f /tmp/imapsyncicon_piojox ]; then 
	echo $(</tmp/imapsyncicon_piojox)
else	
	new=$(find /home/piojox/.local/share/mail/*/Inbox/new/* /home/piojox/.local/share/mail/*/INBOX/new/* /home/piojox/.local/share/mail/*/inbox/new/* 2>/dev/null | wc -l)
	echo "✉ $new"
fi
