from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.testing import z2
from zope.configuration import xmlconfig

class HejaSverigePolicy(PloneSandboxLayer):
	defaultBases = (PLONE_FIXTURE,)

	def setUpZope(self, app, configurationContext):
		# Load ZCML
		import hejasverige.policy
		xmlconfig.file('configure.zcml',
			hejasverige.policy,
			context=configurationContext
			)

		# Install products that use an old-style initialize()
		# function
		z2.installProduct(app, 'Products.PythonField')
		z2.installProduct(app, 'Products.TALESField')
		z2.installProduct(app, 'Products.TemplateFields')
		#z2.installProduct(app, 'Products.PloneFormGen')

	def tearDownZope(self, app):
		# Uninstall products installed above
		#z2.uninstallProduct(app, 'Products.PloneFormGen')
		z2.uninstallProduct(app, 'Products.TemplateFields')
		z2.uninstallProduct(app, 'Products.TALESField')
		z2.uninstallProduct(app, 'Products.PythonField')		
	
	def setUpPloneSite(self, portal):
		applyProfile(portal, 'hejasverige.policy:default')

HEJASVERIGE_POLICY_FIXTURE = HejaSverigePolicy()
HEJASVERIGE_POLICY_INTEGRATION_TESTING = IntegrationTesting(
	bases=(HEJASVERIGE_POLICY_FIXTURE,),
	name="HejaSverige:Integration"
	)


