try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap
	from zcrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zcrmsdk.src.com.zoho.crm.api.param import Param
	from zcrmsdk.src.com.zoho.crm.api.header import Header
	from zcrmsdk.src.com.zoho.crm.api.header_map import HeaderMap
except Exception:
	from ..exception import SDKException
	from ..parameter_map import ParameterMap
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param
	from ..header import Header
	from ..header_map import HeaderMap


class NotesOperations(object):
	def __init__(self):
		"""Creates an instance of NotesOperations"""
		pass

	def get_notes(self, param_instance=None, header_instance=None, parent_module=None, parent_id=None):
		"""
		The method to get notes

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		if parent_module and parent_id:
			api_path = api_path + f'/crm/v2/{parent_module}/{parent_id}/Notes'
		else:
			api_path = api_path + '/crm/v2/Notes'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_notes(self, request):
		"""
		The method to create notes

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/Notes'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_notes(self, request):
		"""
		The method to update notes

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/Notes'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_notes(self, param_instance=None):
		"""
		The method to delete notes

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/Notes'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_note(self, id, param_instance=None, header_instance=None):
		"""
		The method to get note

		Parameters:
			id (int) : An int representing the id
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/Notes/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_note(self, id, request):
		"""
		The method to update note

		Parameters:
			id (int) : An int representing the id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/Notes/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_note(self, id):
		"""
		The method to delete note

		Parameters:
			id (int) : An int representing the id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v2/Notes/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		try:
			from zcrmsdk.src.com.zoho.crm.api.notes.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetNotesParam(object):
	page = Param('page', 'com.zoho.crm.api.Notes.GetNotesParam')
	per_page = Param('per_page', 'com.zoho.crm.api.Notes.GetNotesParam')
	fields = Param('fields', 'com.zoho.crm.api.Notes.GetNotesParam')


class GetNotesHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.Notes.GetNotesHeader')


class DeleteNotesParam(object):
	ids = Param('ids', 'com.zoho.crm.api.Notes.DeleteNotesParam')


class GetNoteParam(object):
	fields = Param('fields', 'com.zoho.crm.api.Notes.GetNoteParam')


class GetNoteHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.Notes.GetNoteHeader')
