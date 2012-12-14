import unittest2 as unittest
from hejasverige.policy.testing import HEJASVERIGE_POLICY_INTEGRATION_TESTING
from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):
    layer = HEJASVERIGE_POLICY_INTEGRATION_TESTING

    def test_portal_title(self):
        portal = self.layer['portal']
        self.assertEqual(
            "Heja Sverige F\xc3\xb6reningar",
            portal.getProperty('title')
            )

    def test_portal_description(self):
        portal = self.layer['portal']
        self.assertEqual(
            "V\xc3\xa4lkommen till Heja Sverige F\xc3\xb6reningar",
            portal.getProperty('description')
            )

    def test_role_added(self):
        portal = self.layer['portal']
        self.assertTrue("StaffMember" in portal.validRoles())

    def test_workflow_installed(self):
        portal = self.layer['portal']
        workflow = getToolByName(portal, 'portal_workflow')
        self.assertTrue('hejasverige_workflow' in workflow)
    
    def test_workflows_mapped(self):
        portal = self.layer['portal']
        workflow = getToolByName(portal, 'portal_workflow')
        self.assertEqual(('hejasverige_workflow',),
        workflow.getDefaultChain())
    
    def test_view_permisison_for_staffmember(self):
        portal = self.layer['portal']
        self.assertTrue('View' in [r['name']
            for r in portal.permissionsOfRole('Reader')
            if r['selected']])
        self.assertTrue('View' in [r['name']
            for r in portal.permissionsOfRole('StaffMember')
            if r['selected']])
    
    def test_staffmember_group_added(self):
        portal = self.layer['portal']
        acl_users = portal['acl_users']
        self.assertEqual(1,
            len(acl_users.searchGroups(name='Staff')))

    def test_PloneFormGen_installed(self):
        portal = self.layer['portal']
        portal_types = getToolByName(portal, 'portal_types')
        self.assertTrue("FormFolder" in portal_types)

    def test_content_installed(self):
        portal = self.layer['portal']
        portal_types = getToolByName(portal, 'portal_types')
        self.assertTrue('hejasverige.Associasion' in portal_types)

    def test_metaTypesNotToList_configured(self):
        portal = self.layer['portal']
        portal_properties = getToolByName(portal, 'portal_properties')
        navtree_properties = portal_properties['navtree_properties']
        metaTypesNotToList = navtree_properties.getProperty('metaTypesNotToList')
        
        self.assertTrue("Promotion" in metaTypesNotToList)
        self.assertTrue("Discussion Item" in metaTypesNotToList)
        self.assertFalse("Associasion" in metaTypesNotToList)

    def test_add_promotion_permission_for_staffmember(self):
        portal = self.layer['portal']

        self.assertTrue('HejaSverige: Add Promotion' in [r['name'] for r in portal.permissionsOfRole('StaffMember') if r['selected']])



