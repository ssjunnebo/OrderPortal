"""OrderPortal: A portal for orders to a facility from its users.
An order can be a project application, a request, a report, etc.
"""

from __future__ import print_function, absolute_import

import os

__version__ = '3.6.36'

# Default settings, may be changed in a settings YAML file.
settings = dict(
    ROOT_DIR=os.path.dirname(__file__),
    BASE_URL='http://localhost/',
    TORNADO_DEBUG=False,
    LOGGING_DEBUG=False,
    LOGGING_FORMAT='%(levelname)s [%(asctime)s] %(message)s',
    LOGGING_FILEPATH=None,
    LOGGING_FILEMODE=None,
    DATABASE_SERVER='http://localhost:5984/',
    DATABASE_NAME='orderportal',
    MARKDOWN_URL='http://agea.github.io/tutorial.md/',
    SITE_DIR='{ROOT_DIR}/site',
    SITE_NAME='OrderPortal',
    SITE_FAVICON='orderportal32.png',
    SITE_HOST_ICON=None,
    SITE_HOST_TITLE=None,
    SITE_HOST_URL=None,
    ACCOUNT_MESSAGES_FILEPATH='{SITE_DIR}/account_messages.yaml',
    ORDER_STATUSES_FILEPATH='{SITE_DIR}/order_statuses.yaml',
    ORDER_TRANSITIONS_FILEPATH='{SITE_DIR}/order_transitions.yaml',
    ORDER_MESSAGES_FILEPATH='{SITE_DIR}/order_messages.yaml',
    UNIVERSITIES_FILEPATH='{SITE_DIR}/swedish_universities.yaml',
    COUNTRY_CODES_FILEPATH='{SITE_DIR}/country_codes.yaml',
    SUBJECT_TERMS_FILEPATH='{SITE_DIR}/subject_terms.yaml',
    TERMINOLOGY=dict(),         # Terms translation lookup.
    MIN_PASSWORD_LENGTH=8,
    LOGIN_MAX_AGE_DAYS=14,
    LOGIN_MAX_FAILURES=6,
    DISPLAY_DEFAULT_PAGE_SIZE=25,
    DISPLAY_MAX_RECENT_ORDERS=10,
    DISPLAY_ORDERS_MOST_RECENT=500,
    DISPLAY_MAX_PENDING_ACCOUNTS=10,
    DISPLAY_DEFAULT_MAX_LOG=20,
    DISPLAY_NEWS=True,
    DISPLAY_MAX_NEWS=4,
    DISPLAY_EVENTS=True,
    DISPLAY_MENU_INFORMATION=True,
    DISPLAY_MENU_DOCUMENTS=True,
    DISPLAY_MENU_ABOUT_US=True,
    ORDER_IDENTIFIER_FORMAT=None,
    ORDER_IDENTIFIER_REGEXP=None,
    ORDER_TAGS=True,
    ORDER_USER_TAGS=True,
    ORDER_LINKS=True,
    ORDER_REPORT=True,
    ORDERS_LIST_TAGS=True,
    ORDERS_LIST_FIELDS=[],
    ORDERS_LIST_STATUSES=[],
    ORDERS_SEARCH_DELIMS_LINT=[':', ',', ';', "'"],
    ORDERS_SEARCH_LINT=['an', 'to', 'in', 'on', 'of', 
                        'and', 'the', 'is', 'was', 'not'],
    ORDERS_SEARCH_FIELDS=[],
    ACCOUNT_PI_INFO=True,
    ACCOUNT_POSTAL_INFO=True,
    ACCOUNT_INVOICE_INFO=True,
    ACCOUNT_FUNDER_INFO=True,
    ACCOUNT_FUNDER_INFO_GENDER=True,
    ACCOUNT_FUNDER_INFO_GROUP_SIZE=True,
    ACCOUNT_FUNDER_INFO_SUBJECT=True,
    ACCOUNT_DEFAULT_COUNTRY_CODE='SE',
    )
