# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class MailboxTypeEnum(object):

    """Implementation of the 'MailboxType' enum.
    Specifies the type of mailbox associated Specifies the type of user
    mailbox. 'kUserMailbox' indicates that the user has been assigned an
    individual mailbox. 'kSharedMailbox' indicates that the user has been
    assigned a shared mailbox.


    Attributes:
        KUSERMAILBOX: TODO: type description here.
        KSHAREDMAILBOX: TODO: type description here.

    """

    KUSERMAILBOX = 'kUserMailbox'

    KSHAREDMAILBOX = 'kSharedMailbox'
