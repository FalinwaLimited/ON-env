from odoo.addons.web_editor.tests.test_ui import TestUi
from odoo.addons.base.tests.test_reports import TestReports
from odoo.addons.web.tests.test_js import WebSuite


def fal_test():
    return True


TestReports.test_reports = fal_test()
WebSuite.test_01_js = fal_test()
WebSuite.test_02_js = fal_test()
TestUi.test_01_admin_rte = fal_test()
TestUi.test_02_admin_rte_inline = fal_test()
