#!/usr/bin/env python

from mock_class import MockClass, RFDFMockClass
import testcaseprint


class MockClassC3LinearizationMROTester(testcaseprint.TestCasePrint):

    def test_class_with_no_parents(self):
        O = MockClass('O')
        expected = ['O']
        self.assertEqual(O.mro_names(), expected)

    def test_print_mro_on_single_class(self):
        O = MockClass('O')
        expected_output = 'O'
        self.assertPrints(O.print_mro, expected_output)

    def test_two_level_hierarchy_no_multiple_inheritance(self):
        O = MockClass('O')
        A1 = MockClass('A1', O)
        A2 = MockClass('A2', O)
        expected = ['O']
        expected1 = ['A1', 'O']
        expected2 = ['A2', 'O']
        self.assertEqual(O.mro_names(), expected)
        self.assertEqual(A1.mro_names(), expected1)
        self.assertEqual(A2.mro_names(), expected2)

    def test_two_level_hierarchy_with_multiple_inheritance(self):
        O1 = MockClass('O1')
        O2 = MockClass('O2')
        A = MockClass('A', O1, O2)
        expectedA = ['A', 'O1', 'O2']
        self.assertEqual(A.mro_names(), expectedA)

    def test_three_level_hierarchy_no_multiple_inheritance(self):
        O = MockClass('O')
        A1 = MockClass('A1', O)
        A2 = MockClass('A2', O)
        B1 = MockClass('B1', A1)
        B2 = MockClass('B2', A2)
        expectedO = ['O']
        expectedA1 = ['A1', 'O']
        expectedA2 = ['A2', 'O']
        expectedB1 = ['B1', 'A1', 'O']
        expectedB2 = ['B2', 'A2', 'O']
        self.assertEqual(O.mro_names(), expectedO)
        self.assertEqual(A1.mro_names(), expectedA1)
        self.assertEqual(A2.mro_names(), expectedA2)
        self.assertEqual(B1.mro_names(), expectedB1)
        self.assertEqual(B2.mro_names(), expectedB2)

    def test_three_level_hierarchy_with_multiple_inheritance(self):
        O = MockClass('O')
        A1 = MockClass('A1', O)
        A2 = MockClass('A2', O)
        B = MockClass('B', A1, A2)
        expectedB = ['B', 'A1', 'A2', 'O']
        self.assertEqual(B.mro_names(), expectedB)

    def test_four_level_hierarchy_with_multiple_inheritance(self):
        O = MockClass('O')
        A1 = MockClass('A1', O)
        A2 = MockClass('A2', O)
        A3 = MockClass('A3', O)
        A4 = MockClass('A4', O)
        A5 = MockClass('A5', O)
        B1 = MockClass('B1', A1, A2, A3)
        B2 = MockClass('B2', A4, A2, A5)
        B3 = MockClass('B3', A4, A1)
        C = MockClass('C', B1, B2, B3)
        expected = ['C', 'B1', 'B2', 'B3', 'A4', 'A1', 'A2', 'A3', 'A5', 'O']
        self.assertEqual(C.mro_names(), expected)

    def test_print_mro(self):
        O = MockClass('O')
        A1 = MockClass('A1', O)
        A2 = MockClass('A2', O)
        A3 = MockClass('A3', O)
        A4 = MockClass('A4', O)
        A5 = MockClass('A5', O)
        B1 = MockClass('B1', A1, A2, A3)
        B2 = MockClass('B2', A4, A2, A5)
        B3 = MockClass('B3', A4, A1)
        C = MockClass('C', B1, B2, B3)
        expected = ['C', 'B1', 'B2', 'B3', 'A4', 'A1', 'A2', 'A3', 'A5', 'O']
        expected_output = '\n'.join(expected)
        self.assertPrints(C.print_mro, expected_output)


class MockClassRFDFLinearizationTester(testcaseprint.TestCasePrint):

    def test_class_with_no_parents(self):
        O = RFDFMockClass('O')
        expected = ['O']
        self.assertEqual(O.mro_names(), expected)

    def test_two_level_hierarchy_no_multiple_inheritance(self):
        O = RFDFMockClass('O')
        A1 = RFDFMockClass('A1', O)
        A2 = RFDFMockClass('A2', O)
        expected = ['O']
        expected1 = ['A1', 'O']
        expected2 = ['A2', 'O']
        self.assertEqual(O.mro_names(), expected)
        self.assertEqual(A1.mro_names(), expected1)
        self.assertEqual(A2.mro_names(), expected2)

    def test_two_level_hierarchy_with_multiple_inheritance(self):
        O1 = RFDFMockClass('O1')
        O2 = RFDFMockClass('O2')
        A = RFDFMockClass('A', O1, O2)
        expected1 = ['O1']
        expected2 = ['O2']
        expectedA = ['A', 'O1', 'O2']
        self.assertEqual(O1.mro_names(), expected1)
        self.assertEqual(O2.mro_names(), expected2)
        self.assertEqual(A.mro_names(), expectedA)

    def test_three_level_hierarchy_with_multiple_inheritance(self):
        O = RFDFMockClass('O')
        A1 = RFDFMockClass('A1', O)
        A2 = RFDFMockClass('A2', O)
        B = RFDFMockClass('B', A1, A2)
        expectedO = ['O']
        expected1 = ['A1', 'O']
        expected2 = ['A2', 'O']
        expectedB = ['B', 'A1', 'A2', 'O']
        self.assertEqual(O.mro_names(), expectedO)
        self.assertEqual(A1.mro_names(), expected1)
        self.assertEqual(A2.mro_names(), expected2)
        self.assertEqual(B.mro_names(), expectedB)

    def test_complicated_hierarchy_with_multiple_inheritance(self):
        self.assertFalse(True)
        


if __name__ == '__main__':
    testcaseprint.main()
