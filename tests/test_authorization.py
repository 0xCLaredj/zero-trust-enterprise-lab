import importlib.util
from pathlib import Path
import unittest
spec = importlib.util.spec_from_file_location('authorization', Path(__file__).resolve().parents[1] / 'app/authorization.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class RoleBoundaryTests(unittest.TestCase):
    def test_employee_cannot_admin(self):
        self.assertFalse(module.is_portal_admin(['employee']))
    def test_admin_role_allows(self):
        self.assertTrue(module.is_portal_admin(['employee', 'portal-admin']))
    def test_missing_and_malformed_claims_fail_closed(self):
        for claim in (None, 'portal-admin', {'portal-admin': True}, [], 1):
            with self.subTest(claim=claim):
                self.assertFalse(module.is_portal_admin(claim))

if __name__ == '__main__': unittest.main()
