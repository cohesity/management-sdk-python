# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class EmailMetaData(object):

    """Implementation of the 'EmailMetaData' model.

    Specifies details about the emails and the folder containing emails.


    Attributes:

        all_under_hierarchy (bool): AllUnderHierarchy specifies if logs of all
            the tenants under the hierarchy of tenant with id TenantId should
            be returned.
        bcc_recipient_addresses (list of string): Specifies the email addresses
            of the bcc recipients.
        cc_recipient_addresses (list of string): Specifies the email addresses
            of the cc recipients.
        directory_path (string): Specifies the directory path to the item.
        domain_ids (list of long|int): Specifies the domain Ids in which
            mailboxes are registered.
        email_subject (string): Specifies the subject of the email.
        folder_key (long|int): Specifes the Parent Folder key.
        folder_name (string): Specifies the parent folder name of the email.
        has_attachments (bool): Specifies whether the emails have any
            attachments.
        item_key (string): Specifies the Key(unique within mailbox) for Outlook
            item such as Email. This key is not indexed but used for
            identifying the item while restore.
        mailbox_ids (list of long|int): Specifies the mailbox Ids which
            contains the emails/folders.
        protection_job_ids (list of long|int): Specifies the protection job Ids
            which have backed up mailbox(es) continaing emails/folders.
        received_end_time (long|int): Specifies the unix end time for querying
            on email's received time.
        received_start_time (long|int): Specifies the unix start time for
            querying on email's received time.
        received_time_seconds (long|int): Specifies the unix time when the
            email was received.
        recipient_addresses (list of string): Specifies the email addresses of
            the recipients.
        sender_address (string): Specifies the email address of the sender.
        sent_time_seconds (long|int): Specifies the unix time when the email
            was sent.
        show_only_email_folders (bool): Specifies whether the query result
            should include only Email folders.
        tenant_id (string): TenantId specifies the tenant whose action resulted
            in the audit log.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "all_under_hierarchy":'allUnderHierarchy',
        "bcc_recipient_addresses":'bccRecipientAddresses',
        "cc_recipient_addresses":'ccRecipientAddresses',
        "directory_path":'directoryPath',
        "domain_ids":'domainIds',
        "email_subject":'emailSubject',
        "folder_key":'folderKey',
        "folder_name":'folderName',
        "has_attachments":'hasAttachments',
        "item_key":'itemKey',
        "mailbox_ids":'mailboxIds',
        "protection_job_ids":'protectionJobIds',
        "received_end_time":'receivedEndTime',
        "received_start_time":'receivedStartTime',
        "received_time_seconds":'receivedTimeSeconds',
        "recipient_addresses":'recipientAddresses',
        "sender_address":'senderAddress',
        "sent_time_seconds":'sentTimeSeconds',
        "show_only_email_folders":'showOnlyEmailFolders',
        "tenant_id":'tenantId',
    }
    def __init__(self,
                 all_under_hierarchy=None,
                 bcc_recipient_addresses=None,
                 cc_recipient_addresses=None,
                 directory_path=None,
                 domain_ids=None,
                 email_subject=None,
                 folder_key=None,
                 folder_name=None,
                 has_attachments=None,
                 item_key=None,
                 mailbox_ids=None,
                 protection_job_ids=None,
                 received_end_time=None,
                 received_start_time=None,
                 received_time_seconds=None,
                 recipient_addresses=None,
                 sender_address=None,
                 sent_time_seconds=None,
                 show_only_email_folders=None,
                 tenant_id=None,
            ):

        """Constructor for the EmailMetaData class"""

        # Initialize members of the class
        self.all_under_hierarchy = all_under_hierarchy
        self.bcc_recipient_addresses = bcc_recipient_addresses
        self.cc_recipient_addresses = cc_recipient_addresses
        self.directory_path = directory_path
        self.domain_ids = domain_ids
        self.email_subject = email_subject
        self.folder_key = folder_key
        self.folder_name = folder_name
        self.has_attachments = has_attachments
        self.item_key = item_key
        self.mailbox_ids = mailbox_ids
        self.protection_job_ids = protection_job_ids
        self.received_end_time = received_end_time
        self.received_start_time = received_start_time
        self.received_time_seconds = received_time_seconds
        self.recipient_addresses = recipient_addresses
        self.sender_address = sender_address
        self.sent_time_seconds = sent_time_seconds
        self.show_only_email_folders = show_only_email_folders
        self.tenant_id = tenant_id

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        all_under_hierarchy = dictionary.get('allUnderHierarchy')
        bcc_recipient_addresses = dictionary.get("bccRecipientAddresses")
        cc_recipient_addresses = dictionary.get("ccRecipientAddresses")
        directory_path = dictionary.get('directoryPath')
        domain_ids = dictionary.get("domainIds")
        email_subject = dictionary.get('emailSubject')
        folder_key = dictionary.get('folderKey')
        folder_name = dictionary.get('folderName')
        has_attachments = dictionary.get('hasAttachments')
        item_key = dictionary.get('itemKey')
        mailbox_ids = dictionary.get("mailboxIds")
        protection_job_ids = dictionary.get("protectionJobIds")
        received_end_time = dictionary.get('receivedEndTime')
        received_start_time = dictionary.get('receivedStartTime')
        received_time_seconds = dictionary.get('receivedTimeSeconds')
        recipient_addresses = dictionary.get("recipientAddresses")
        sender_address = dictionary.get('senderAddress')
        sent_time_seconds = dictionary.get('sentTimeSeconds')
        show_only_email_folders = dictionary.get('showOnlyEmailFolders')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(
            all_under_hierarchy,
            bcc_recipient_addresses,
            cc_recipient_addresses,
            directory_path,
            domain_ids,
            email_subject,
            folder_key,
            folder_name,
            has_attachments,
            item_key,
            mailbox_ids,
            protection_job_ids,
            received_end_time,
            received_start_time,
            received_time_seconds,
            recipient_addresses,
            sender_address,
            sent_time_seconds,
            show_only_email_folders,
            tenant_id
)