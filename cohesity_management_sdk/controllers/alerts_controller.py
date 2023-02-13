# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.alert_category_name import AlertCategoryName
from cohesity_management_sdk.models.notification_rule import NotificationRule
from cohesity_management_sdk.models.alert_resolution import AlertResolution
from cohesity_management_sdk.models.alert_metadata import AlertMetadata
from cohesity_management_sdk.models.alert import Alert
from cohesity_management_sdk.exceptions.request_error_error_exception import RequestErrorErrorException


class AlertsController(BaseController):
    """A Controller to access Endpoints in the cohesity_management_sdk API."""
    def __init__(self, config=None, client=None, call_back=None):
        super(AlertsController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)
        self.config = config

    def get_alert_categories(self):
        """Does a GET request to /public/alertCategories.

        Returns alert categories in Cohesity cluster.

        Returns:
            list of AlertCategoryName: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_alert_categories called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_alert_categories.')
            _url_path = '/public/alertCategories'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_alert_categories.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_alert_categories.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_alert_categories')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_alert_categories.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(
                _context.response.raw_body, AlertCategoryName.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_notification_rules(self):
        """Does a GET request to /public/alertNotificationRules.

        Gets all alert notification rules containing criteria to deliver
        notification
        to delivery targets such as email addresses, invoking external apis
        etc.

        Returns:
            list of NotificationRule: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_notification_rules called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_notification_rules.')
            _url_path = '/public/alertNotificationRules'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_notification_rules.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_notification_rules.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_notification_rules')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_notification_rules.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              NotificationRule.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_notification_rule(self, body=None):
        """Does a POST request to /public/alertNotificationRules.

        Creates a new notification rule with provided delivery targets such as
        email
        addresses and external apis.

        Args:
            body (NotificationRule, optional): Create Notification Rule
                argument.

        Returns:
            NotificationRule: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_notification_rule called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for create_notification_rule.')
            _url_path = '/public/alertNotificationRules'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_notification_rule.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_notification_rule.'
            )
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='create_notification_rule')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for create_notification_rule.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              NotificationRule.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_notification_rule(self):
        """Does a PUT request to /public/alertNotificationRules.

        Updates delivery targets such as email addresses and external apis in
        an
        existing notification rule.

        Returns:
            NotificationRule: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_notification_rule called.')

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for update_notification_rule.')
            _url_path = '/public/alertNotificationRules'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_notification_rule.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_notification_rule.'
            )
            _request = self.http_client.put(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='update_notification_rule')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for update_notification_rule.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              NotificationRule.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def delete_notification_rule(self, rule_id):
        """Does a DELETE request to /public/alertNotificationRules/{ruleId}.

        Deletes an existing alert notification rule matching the rule id.

        Args:
            rule_id (long|int): Specifies the rule id.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_notification_rule called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for delete_notification_rule.')
            self.validate_parameters(rule_id=rule_id)

            # Prepare query URL
            self.logger.info(
                'Preparing query URL for delete_notification_rule.')
            _url_path = '/public/alertNotificationRules/{ruleId}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'ruleId': rule_id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for delete_notification_rule.'
            )
            _request = self.http_client.delete(_query_url)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='delete_notification_rule')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info(
                'Validating response for delete_notification_rule.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_resolutions(self,
                        max_resolutions,
                        resolution_id_list=None,
                        alert_id_list=None,
                        start_date_usecs=None,
                        end_date_usecs=None,
                        tenant_ids=None,
                        all_under_hierarchy=None):
        """Does a GET request to /public/alertResolutions.

        Returns all Alert Resolution objects found on the Cohesity Cluster
        that match the filter criteria specified using parameters.
        If no filter parameters are specified,
        all Alert Resolution objects are returned.
        Each object provides details about the Alert Resolution such as
        the resolution summary and details.

        Args:
            max_resolutions (int): Specifies the number of returned
                Resolutions to be returned. The newest Resolutions are
                returned.
            resolution_id_list (list of long|int, optional): Specifies list of
                Alert Resolution ids to filter resolutions by.
            alert_id_list (list of string, optional): Specifies list of Alert
                Resolution ids to filter resolutions by.
            start_date_usecs (long|int, optional): Specifies Start Time Unix
                epoch in microseconds to filter resolutions by.
            end_date_usecs (long|int, optional): Specifies End Time Unix epoch
                in microseconds to filter resolutions by.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of AlertResolution: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_resolutions called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_resolutions.')
            self.validate_parameters(max_resolutions=max_resolutions)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_resolutions.')
            _url_path = '/public/alertResolutions'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'maxResolutions': max_resolutions,
                'resolutionIdList': resolution_id_list,
                'alertIdList': alert_id_list,
                'startDateUsecs': start_date_usecs,
                'endDateUsecs': end_date_usecs,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_resolutions.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_resolutions.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_resolutions')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_resolutions.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AlertResolution.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def create_resolution(self, body):
        """Does a POST request to /public/alertResolutions.

        Create an Alert Resolution and apply it to one or more Alerts.
        Mark the Alerts as resolved.

        Args:
            body (AlertResolutionRequest): Request to create an Alert
                Resolution and apply it to the specified Alerts.

        Returns:
            AlertResolution: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_resolution called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for create_resolution.')
            self.validate_parameters(body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for create_resolution.')
            _url_path = '/public/alertResolutions'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_resolution.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for create_resolution.')
            _request = self.http_client.post(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='create_resolution')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_resolution.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AlertResolution.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_resolution_by_id(self, id):
        """Does a GET request to /public/alertResolutions/{id}.

        Returns the Alert Resolution object corresponding to passed in Alert
        Resolution Id.

        Args:
            id (long|int): Unique id of the Alert Resolution to return.

        Returns:
            AlertResolution: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_resolution_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_resolution_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_resolution_by_id.')
            _url_path = '/public/alertResolutions/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_resolution_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_resolution_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request,
                                            name='get_resolution_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_resolution_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AlertResolution.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def update_resolution(self, id, body):
        """Does a PUT request to /public/alertResolutions/{id}.

        Apply an existing Alert Resolution to one or more additional Alerts.
        Mark those additional Alerts as resolved.

        Args:
            id (long|int): Unique id of the Alert Resolution to return.
            body (UpdateResolutionParams): Request to apply an existing
                resolution to the specified Alerts.

        Returns:
            AlertResolution: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_resolution called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for update_resolution.')
            self.validate_parameters(id=id, body=body)

            # Prepare query URL
            self.logger.info('Preparing query URL for update_resolution.')
            _url_path = '/public/alertResolutions/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for update_resolution.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for update_resolution.')
            _request = self.http_client.put(
                _query_url,
                headers=_headers,
                parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='update_resolution')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_resolution.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AlertResolution.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_alert_types(self, alert_category_list=None):
        """Does a GET request to /public/alertTypes.

        Returns registered alerts in the Cohesity cluster that match the
        filter
        criteria specified using parameters. If no filter parameters are
        specified,
        all registered alerts in the Cohesity cluster are returned.

        Args:
            alert_category_list (list of AlertCategoryListEnum, optional):
                Specifies a list of Alert Categories to filter alert types by.
                Specifies the category of an Alert.

        Returns:
            list of AlertMetadata: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_alert_types called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_alert_types.')
            _url_path = '/public/alertTypes'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'alertCategoryList': alert_category_list
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_alert_types.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_alert_types.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_alert_types')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_alert_types.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              AlertMetadata.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_alerts(self,
                   max_alerts,
                   alert_id_list=None,
                   alert_type_list=None,
                   alert_category_list=None,
                   property_key=None,
                   property_value=None,
                   start_date_usecs=None,
                   end_date_usecs=None,
                   alert_state_list=None,
                   alert_severity_list=None,
                   alert_type_bucket_list=None,
                   resolution_id_list=None,
                   tenant_ids=None,
                   all_under_hierarchy=None):
        """Does a GET request to /public/alerts.

        Returns all Alert objects found on the Cohesity Cluster that
        match the filter criteria specified using parameters.
        The Cohesity Cluster creates an Alert when a potential problem
        is found or when a threshold has been exceeded on the Cohesity
        Cluster.
        If no filter parameters are specified, all Alert objects are
        returned.
        Each object provides details about the Alert such as the Status and
        Severity.

        Args:
            max_alerts (int): Specifies the number of returned Alerts to be
                returned. The newest Alerts are returned.
            alert_id_list (list of string, optional): Specifies list of Alert
                ids to filter alerts by.
            alert_type_list (list of int, optional): Specifies list of Alert
                Types to filter alerts by.
            alert_category_list (list of AlertCategoryListGetAlertsEnum,
                optional): Specifies list of Alert Categories.
            property_key (string, optional): Specifies name of the property to
                filter alerts by.
            property_value (string, optional): Specifies value of the property
                to filter alerts by.
            start_date_usecs (long|int, optional): Specifies start time Unix
                epoch time in microseconds to filter alerts by.
            end_date_usecs (long|int, optional): Specifies end time Unix epoch
                time in microseconds to filter alerts by.
            alert_state_list (list of AlertStateListEnum, optional): Specifies
                list of Alert States to filter alerts by.
            alert_severity_list (list of AlertSeverityListEnum, optional):
                Specifies list of Alert severity to filter alerts by.
            alert_type_bucket_list (list of AlertTypeBucketListEnum,
                optional): Specifies the list of Alert type bucket. Specifies
                the Alert type bucket.
            resolution_id_list (list of long|int, optional): Specifies alert
                resolution ids to filter alerts by.
            tenant_ids (list of string, optional): TenantIds contains ids of
                the tenants for which objects are to be returned.
            all_under_hierarchy (bool, optional): AllUnderHierarchy specifies
                if objects of all the tenants under the hierarchy of the
                logged in user's organization should be returned.

        Returns:
            list of Alert: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_alerts called.')

            # Validate required parameters
            self.logger.info('Validating required parameters for get_alerts.')
            self.validate_parameters(max_alerts=max_alerts)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_alerts.')
            _url_path = '/public/alerts'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'maxAlerts': max_alerts,
                'alertIdList': alert_id_list,
                'alertTypeList': alert_type_list,
                'alertCategoryList': alert_category_list,
                'propertyKey': property_key,
                'propertyValue': property_value,
                'startDateUsecs': start_date_usecs,
                'endDateUsecs': end_date_usecs,
                'alertStateList': alert_state_list,
                'alertSeverityList': alert_severity_list,
                'alertTypeBucketList': alert_type_bucket_list,
                'resolutionIdList': resolution_id_list,
                'tenantIds': tenant_ids,
                'allUnderHierarchy': all_under_hierarchy
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder, _query_parameters,
                Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_alerts.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_alerts.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_alerts')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_alerts.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Alert.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise

    def get_alert_by_id(self, id):
        """Does a GET request to /public/alerts/{id}.

        Returns the Alert object corresponding to the specified id.

        Args:
            id (string): Unique id of the Alert to return.

        Returns:
            Alert: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_alert_by_id called.')

            # Validate required parameters
            self.logger.info(
                'Validating required parameters for get_alert_by_id.')
            self.validate_parameters(id=id)

            # Prepare query URL
            self.logger.info('Preparing query URL for get_alert_by_id.')
            _url_path = '/public/alerts/{id}'
            _url_path = APIHelper.append_url_with_template_parameters(
                _url_path, {'id': id})
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_alert_by_id.')
            _headers = {'accept': 'application/json'}

            # Prepare and execute request
            self.logger.info(
                'Preparing and executing request for get_alert_by_id.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request, self.config)
            _context = self.execute_request(_request, name='get_alert_by_id')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_alert_by_id.')
            if _context.response.status_code == 0:
                raise RequestErrorErrorException('Error', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body,
                                              Alert.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info=True)
            raise
