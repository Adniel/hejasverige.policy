import logging
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType
from plone.app.controlpanel.security import ISecuritySchema
from zope.interface import alsoProvides
from Products.CMFCore.WorkflowCore import WorkflowException
from hejasverige.policy import _
from hejasverige.policy.interfaces import IMyPagesFolder


def setupSiteSecurity(portal, logger):
    """
        site security setup!
    """
    secSchema = ISecuritySchema(portal)
    secSchema.set_enable_self_reg(True)
    secSchema.set_enable_user_pwd_choice(False)
    secSchema.set_enable_user_folders(True)
    secSchema.set_use_email_as_login(True)


def setupGroups(portal, logger):
    acl_users = getToolByName(portal, 'acl_users')
    if not acl_users.searchGroups(name='Staff'):
        gtool = getToolByName(portal, 'portal_groups')
        gtool.addGroup('Staff', roles=['StaffMember'])


def setupMyPagesFolder(portal, logger=None):
    if logger:
        logger.info('')
    folder_id = 'my-pages'
    folder_title = u'Mina sidor'
    object_type = 'Folder'
    view = '@@my-pages'

    existing_objects = portal.objectIds()

    if folder_id in existing_objects:
        logger.info("Object exists in folder")
    else:
        _createObjectByType(object_type, portal, id=folder_id,
                            title=_(folder_title))

    obj = portal.get(folder_id, None)
    if obj:
        if obj.Type() == object_type:
            try:
                alsoProvides(obj, IMyPagesFolder)
            except:
                logger.info("Could not apply marker interface...")

            try:
                obj.setLayout(view)
            except:
                logger.info("Could not set layout property...")

            try:
                workflowTool = getToolByName(portal, 'portal_workflow')
                workflowTool.doActionFor(obj, 'publish_internally')
            except WorkflowException:
                logger.info("Could not apply workflow publish_internally transition. Trying publish...")
                try:
                    workflowTool.doActionFor(obj, 'publish')
                except WorkflowException:
                    logger.info("Workflow transition 'publish' failed...")


def importVarious(context):
    """Miscellanous steps import handle
    """
    if context.readDataFile('hejasverige.policy-various.txt') is None:
        return

    logger = logging.getLogger('hejasverige.policy')

    portal = context.getSite()
    setupGroups(portal, logger)
    setupSiteSecurity(portal, logger)
    #setupMyPagesFolder(portal, logger)
