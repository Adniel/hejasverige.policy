import logging
from Products.CMFCore.utils import getToolByName
from plone.app.controlpanel.security import ISecuritySchema

def setupSiteSecurity(portal, logger):
    """
        site security setup!
    """
    secSchema = ISecuritySchema(portal)
    secSchema.set_enable_self_reg(True)
    secSchema.set_enable_user_pwd_choice(False)
    secSchema.set_enable_user_folders(False)
    secSchema.set_use_email_as_login(True)

def setupGroups(portal, logger):
    acl_users = getToolByName(portal, 'acl_users')
    if not acl_users.searchGroups(name='Staff'):
        gtool = getToolByName(portal, 'portal_groups')
        gtool.addGroup('Staff', roles=['StaffMember'])

def importVarious(context):
    """Miscellanous steps import handle
    """
    if context.readDataFile('hejasverige.policy-various.txt') is None:
        return

    logger = logging.getLogger('hejasverige.policy')

    portal = context.getSite()
    setupGroups(portal, logger)
    setupSiteSecurity(portal, logger)
  