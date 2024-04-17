import unittest

from customLinkedListController import CustomLinkedListController

class TestCustomLinkedListController(unittest.TestCase):

    def buildTestMonthsDatabase(self):

        TempCustomLinkedList = CustomLinkedListController({"head": {}})

        yearObject = self.createYearObject(2020)

        yearObject['months'].append(self.createMonthObject(
            8,
            0,
            6,
            [{"flag": "add", "type": "months", "ID": "ID4140609502003290", "name": "first", "value": 5, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createMonthObject(
            5,
            2,
            8,
            [{"flag": "add", "type": "months", "ID": "ID41656003290", "name": "first", "value": 15, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createMonthObject(
            2,
            10,
            16,
            [{"flag": "add", "type": "months", "ID": "ID468716560", "name": "first", "value": -67, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createMonthObject(
            2,
            10,
            16*12,
            [{"flag": "add", "type": "months", "ID": "ID41568735432", "name": "first", "value": 115, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createMonthObject(
            9,
            2,
            3,
            [{"flag": "add", "type": "months", "ID": "ID536836422132", "name": "first", "value": 1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))

        TempCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(2019)
        yearObject['months'].append(self.createMonthObject(
            1,
            5,
            6,
            [{"flag": "add", "type": "months", "ID": "ID22132", "name": "first", "value": -1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))

        TempCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(2050)
        yearObject['months'].append(self.createMonthObject(
            7,
            1,
            3,
            [{"flag": "add", "type": "months", "ID": "ID9464732", "name": "first", "value": 20, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createMonthObject(
            2,
            1,
            116,
            [{"flag": "add", "type": "months", "ID": "ID464732", "name": "first", "value": 220, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))

        TempCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(20)
        yearObject['months'].append(self.createMonthObject(
            11,
            11,
            63,
            [{"flag": "add", "type": "months", "ID": "ID954264732", "name": "first", "value": -20, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createMonthObject(
            1,
            0,
            3000*12,
            [{"flag": "add", "type": "months", "ID": "ID95867565424264732", "name": "first", "value": 0, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))

        TempCustomLinkedList.add(yearObject)

        return TempCustomLinkedList

    def buildTestInfDatabase(self):

        TempCustomLinkedList = CustomLinkedListController({"head": {}})

        yearObject = self.createYearObject(2020)

        yearObject['months'].append(self.createInfObject(
            8,
            [{"flag": "add", "type": "months", "ID": "ID4140609502003290", "name": "first", "value": 5, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createInfObject(
            5,
            [{"flag": "add", "type": "months", "ID": "ID41656003290", "name": "first", "value": 15, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createInfObject(
            2,
            [{"flag": "add", "type": "months", "ID": "ID468716560", "name": "first", "value": -67, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createInfObject(
            2,
            [{"flag": "add", "type": "months", "ID": "ID41568735432", "name": "first", "value": 115, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createInfObject(
            9,
            [{"flag": "add", "type": "months", "ID": "ID536836422132", "name": "first", "value": 1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))

        TempCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(2019)
        yearObject['months'].append(self.createInfObject(
            1,
            [{"flag": "add", "type": "months", "ID": "ID22132", "name": "first", "value": -1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))

        TempCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(2050)
        yearObject['months'].append(self.createInfObject(
            7,
            [{"flag": "add", "type": "months", "ID": "ID9464732", "name": "first", "value": 20, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createInfObject(
            2,
            [{"flag": "add", "type": "months", "ID": "ID464732", "name": "first", "value": 220, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))

        TempCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(20)
        yearObject['months'].append(self.createInfObject(
            11,
            [{"flag": "add", "type": "months", "ID": "ID954264732", "name": "first", "value": -20, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))
        yearObject['months'].append(self.createInfObject(
            1,
            [{"flag": "add", "type": "months", "ID": "ID95867565424264732", "name": "first", "value": 0, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111}]
        ))

        TempCustomLinkedList.add(yearObject)

        return TempCustomLinkedList

    def setUp(self):
        # for `add`
        self.CleanCustomLinkedList = CustomLinkedListController({"head": {}})
        self.TestMonthsCustomLinkedList = self.buildTestMonthsDatabase()
        self.TestInfCustomLinkedList = self.buildTestInfDatabase()

    def createInfObject(self, month, objects = {'OBJECTS': 'OBJECTS'}):
        infObject = {}
        infObject['month'] = month
        infObject['objects'] = objects
        return infObject

    def createMonthObject(self, month, start, end, objects = {'OBJECTS': 'OBJECTS'}):
        monthObject = {}
        monthObject['month'] = month
        monthObject['SE'] = []
        monthObject['SE'].append({
            'start': start,
            'end': end,
            'objects': objects
        })

        return monthObject

    def createYearObject(self, year):
        yearObject = {}
        yearObject['year'] = year
        yearObject['months'] = []

        return yearObject

    def test_add_simple_error(self):
            emptyObject = {}

            self.CleanCustomLinkedList.add(emptyObject)

            self.assertEqual(
                str(self.CleanCustomLinkedList.returnLinkedList()),
                "{'head': {}}"
            )

    def test_add_month(self):

        yearObject = self.createYearObject(2020)
        yearObject['months'].append(self.createMonthObject(5, 0, 6))

        self.CleanCustomLinkedList.add(yearObject)

        self.assertEqual(
            str(self.CleanCustomLinkedList.returnLinkedList()),
            "{'head': {'value': {'year': 2020, 'months': [{'month': 5, 'SE': [{'start': 0, 'end': 6, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': 'null'}}"
        )

    def test_add_month_error(self):

        yearObject = self.createYearObject(2020)
        yearObject['months'].append(self.createMonthObject(5, 4, 2))

        self.CleanCustomLinkedList.add(yearObject)

        self.assertEqual(
            str(self.CleanCustomLinkedList.returnLinkedList()),
            "{'head': {}}"
        )
    
    def test_add_month_multipleSE(self):

        yearObject = self.createYearObject(2020)

        yearObject['months'].append(self.createMonthObject(8, 0, 6))
        yearObject['months'].append(self.createMonthObject(5, 2, 8))
        yearObject['months'].append(self.createMonthObject(2, 10, 16))
        yearObject['months'].append(self.createMonthObject(9, 2, 3))

        self.CleanCustomLinkedList.add(yearObject)

        self.assertEqual(
            str(self.CleanCustomLinkedList.returnLinkedList()),
            "{'head': {'value': {'year': 2020, 'months': [{'month': 8, 'SE': [{'start': 0, 'end': 6, 'objects': {'OBJECTS': 'OBJECTS'}}]}, {'month': 5, 'SE': [{'start': 2, 'end': 8, 'objects': {'OBJECTS': 'OBJECTS'}}]}, {'month': 2, 'SE': [{'start': 10, 'end': 16, 'objects': {'OBJECTS': 'OBJECTS'}}]}, {'month': 9, 'SE': [{'start': 2, 'end': 3, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': 'null'}}"
        )
    
    def test_add_month_multipleSE_error(self):

        yearObject = self.createYearObject(2020)

        yearObject['months'].append(self.createMonthObject(8, 0, 6))
        yearObject['months'].append(self.createMonthObject(5, 2, 8))
        yearObject['months'].append(self.createMonthObject(2, 20, 16))
        yearObject['months'].append(self.createMonthObject(9, 2, 3))

        self.CleanCustomLinkedList.add(yearObject)

        self.assertEqual(
            str(self.CleanCustomLinkedList.returnLinkedList()),
            "{'head': {}}"
        )
    
    def test_add_months(self):

        yearObject = self.createYearObject(1040)
        yearObject['months'].append(self.createMonthObject(1, 5, 6))
        self.CleanCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(81218)
        yearObject['months'].append(self.createMonthObject(7, 1, 3))
        self.CleanCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(3568534)
        yearObject['months'].append(self.createMonthObject(11, 11, 63))
        self.CleanCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(5348917)
        yearObject['months'].append(self.createMonthObject(5, 2, 5))
        self.CleanCustomLinkedList.add(yearObject)

        self.assertEqual(
            str(self.CleanCustomLinkedList.returnLinkedList()),
            "{'head': {'value': {'year': 1040, 'months': [{'month': 1, 'SE': [{'start': 5, 'end': 6, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': {'value': {'year': 81218, 'months': [{'month': 7, 'SE': [{'start': 1, 'end': 3, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': {'value': {'year': 3568534, 'months': [{'month': 11, 'SE': [{'start': 11, 'end': 63, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': {'value': {'year': 5348917, 'months': [{'month': 5, 'SE': [{'start': 2, 'end': 5, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': 'null'}}}}}"
        )

    def test_add_months_error(self):

        yearObject = self.createYearObject(1040)
        yearObject['months'].append(self.createMonthObject(1, 5, 6))
        self.CleanCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(81218)
        yearObject['months'].append(self.createMonthObject(7, 1, 3))
        self.CleanCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(3568534)
        yearObject['months'].append(self.createMonthObject(11, 63, 11))
        self.CleanCustomLinkedList.add(yearObject)

        yearObject = self.createYearObject(5348917)
        yearObject['months'].append(self.createMonthObject(5, 2, 5))
        self.CleanCustomLinkedList.add(yearObject)

        self.assertEqual(
            str(self.CleanCustomLinkedList.returnLinkedList()),
            "{'head': {'value': {'year': 1040, 'months': [{'month': 1, 'SE': [{'start': 5, 'end': 6, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': {'value': {'year': 81218, 'months': [{'month': 7, 'SE': [{'start': 1, 'end': 3, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': {'value': {'year': 5348917, 'months': [{'month': 5, 'SE': [{'start': 2, 'end': 5, 'objects': {'OBJECTS': 'OBJECTS'}}]}]}, 'next': 'null'}}}}"
        )

    def test_search_months(self):

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.search(2018, 1, "month")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'SE': []}, {'month': 1, 'SE': [{'start': 0, 'end': 36000, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': 'null'}}"
        )

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.search(2022, 8, "month")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'SE': []}, {'month': 1, 'SE': [{'start': 0, 'end': 36000, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'SE': []}]}, 'next': {'value': {'year': 2020, 'months': [{'month': 8, 'SE': []}, {'month': 5, 'SE': []}, {'month': 2, 'SE': []}, {'month': 2, 'SE': [{'start': 10, 'end': 192, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41568735432', 'name': 'first', 'value': 115, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 9, 'SE': []}]}, 'next': 'null'}}}}"
        )

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.search(2050, 8, "month")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'SE': []}, {'month': 1, 'SE': [{'start': 0, 'end': 36000, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'SE': []}]}, 'next': {'value': {'year': 2020, 'months': [{'month': 8, 'SE': []}, {'month': 5, 'SE': []}, {'month': 2, 'SE': []}, {'month': 2, 'SE': []}, {'month': 9, 'SE': []}]}, 'next': {'value': {'year': 2050, 'months': [{'month': 7, 'SE': [{'start': 1, 'end': 3, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID9464732', 'name': 'first', 'value': 20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 2, 'SE': [{'start': 1, 'end': 116, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID464732', 'name': 'first', 'value': 220, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': 'null'}}}}}"
        )

    def test_search_months_missMatch(self):

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.search(2018, 12, "month")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'SE': []}, {'month': 1, 'SE': [{'start': 0, 'end': 36000, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': 'null'}}"
        )

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.search(2019, 8, "month")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'SE': []}, {'month': 1, 'SE': [{'start': 0, 'end': 36000, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'SE': []}]}, 'next': 'null'}}}"
        )

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.search(5000, 8, "month")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'SE': []}, {'month': 1, 'SE': []}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'SE': []}]}, 'next': {'value': {'year': 2020, 'months': [{'month': 8, 'SE': []}, {'month': 5, 'SE': []}, {'month': 2, 'SE': []}, {'month': 2, 'SE': []}, {'month': 9, 'SE': []}]}, 'next': {'value': {'year': 2050, 'months': [{'month': 7, 'SE': []}, {'month': 2, 'SE': []}]}, 'next': 'null'}}}}}"
        )

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.search(2, 8, "month")),
            "{'head': {}}"
        )

    def test_search_inf(self):

        self.assertEqual(
            str(self.TestInfCustomLinkedList.search(2018, 12, "inf")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID954264732', 'name': 'first', 'value': -20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 1, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': 'null'}}"
        )

        self.assertEqual(
            str(self.TestInfCustomLinkedList.search(2022, 1, "inf")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID954264732', 'name': 'first', 'value': -20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 1, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID22132', 'name': 'first', 'value': -1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': {'value': {'year': 2020, 'months': [{'month': 8, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID4140609502003290', 'name': 'first', 'value': 5, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 5, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41656003290', 'name': 'first', 'value': 15, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 2, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID468716560', 'name': 'first', 'value': -67, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 2, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41568735432', 'name': 'first', 'value': 115, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 9, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID536836422132', 'name': 'first', 'value': 1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': 'null'}}}}"
        )

        self.assertEqual(
            str(self.TestInfCustomLinkedList.search(2050, 9, "inf")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID954264732', 'name': 'first', 'value': -20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 1, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID22132', 'name': 'first', 'value': -1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': {'value': {'year': 2020, 'months': [{'month': 8, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID4140609502003290', 'name': 'first', 'value': 5, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 5, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41656003290', 'name': 'first', 'value': 15, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 2, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID468716560', 'name': 'first', 'value': -67, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 2, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41568735432', 'name': 'first', 'value': 115, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 9, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID536836422132', 'name': 'first', 'value': 1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': {'value': {'year': 2050, 'months': [{'month': 7, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID9464732', 'name': 'first', 'value': 20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 2, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID464732', 'name': 'first', 'value': 220, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': 'null'}}}}}"
        )

        self.assertEqual(
            str(self.TestInfCustomLinkedList.search(20500, 3, "inf")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID954264732', 'name': 'first', 'value': -20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 1, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID22132', 'name': 'first', 'value': -1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': {'value': {'year': 2020, 'months': [{'month': 8, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID4140609502003290', 'name': 'first', 'value': 5, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 5, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41656003290', 'name': 'first', 'value': 15, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 2, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID468716560', 'name': 'first', 'value': -67, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 2, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41568735432', 'name': 'first', 'value': 115, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 9, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID536836422132', 'name': 'first', 'value': 1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': {'value': {'year': 2050, 'months': [{'month': 7, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID9464732', 'name': 'first', 'value': 20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}, {'month': 2, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID464732', 'name': 'first', 'value': 220, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': 'null'}}}}}"
        )

    def test_search_inf_missMatch(self):

        self.assertEqual(
            str(self.TestInfCustomLinkedList.search(20, 10, "inf")),
            "{'head': {'value': {'year': 20, 'months': [{'month': 1, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, 'next': 'null'}}"
        )

    def test_object_months_add(self):

        self.TestMonthsCustomLinkedList.object(
            "month",
            2019,
            1,
            {"flag": "add", "type": "months", "ID": "ID123", "name": "first", "value": -1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
            "add",
            5,
            6,
        )

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.returnLinkedList()),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'SE': [{'start': 11, 'end': 63, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID954264732', 'name': 'first', 'value': -20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 1, 'SE': [{'start': 0, 'end': 36000, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'SE': [{'start': 5, 'end': 6, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID22132', 'name': 'first', 'value': -1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}, {'flag': 'add', 'type': 'months', 'ID': 'ID123', 'name': 'first', 'value': -1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2020, 'months': [{'month': 8, 'SE': [{'start': 0, 'end': 6, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID4140609502003290', 'name': 'first', 'value': 5, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 5, 'SE': [{'start': 2, 'end': 8, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41656003290', 'name': 'first', 'value': 15, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 2, 'SE': [{'start': 10, 'end': 16, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID468716560', 'name': 'first', 'value': -67, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 2, 'SE': [{'start': 10, 'end': 192, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41568735432', 'name': 'first', 'value': 115, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 9, 'SE': [{'start': 2, 'end': 3, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID536836422132', 'name': 'first', 'value': 1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2050, 'months': [{'month': 7, 'SE': [{'start': 1, 'end': 3, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID9464732', 'name': 'first', 'value': 20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 2, 'SE': [{'start': 1, 'end': 116, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID464732', 'name': 'first', 'value': 220, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': 'null'}}}}}"
        )

    def test_object_months_add_error(self):

        self.TestMonthsCustomLinkedList.object(
            "month",
            2019,
            1,
            {"ID":"UNDFINMED", "value":"a756"},
            "add",
            5,
            6,
        )

        self.assertEqual(
            str(self.TestMonthsCustomLinkedList.returnLinkedList()),
            "{'head': {'value': {'year': 20, 'months': [{'month': 11, 'SE': [{'start': 11, 'end': 63, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID954264732', 'name': 'first', 'value': -20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 1, 'SE': [{'start': 0, 'end': 36000, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID95867565424264732', 'name': 'first', 'value': 0, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2019, 'months': [{'month': 1, 'SE': [{'start': 5, 'end': 6, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID22132', 'name': 'first', 'value': -1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2020, 'months': [{'month': 8, 'SE': [{'start': 0, 'end': 6, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID4140609502003290', 'name': 'first', 'value': 5, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 5, 'SE': [{'start': 2, 'end': 8, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41656003290', 'name': 'first', 'value': 15, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 2, 'SE': [{'start': 10, 'end': 16, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID468716560', 'name': 'first', 'value': -67, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 2, 'SE': [{'start': 10, 'end': 192, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID41568735432', 'name': 'first', 'value': 115, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 9, 'SE': [{'start': 2, 'end': 3, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID536836422132', 'name': 'first', 'value': 1, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': {'value': {'year': 2050, 'months': [{'month': 7, 'SE': [{'start': 1, 'end': 3, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID9464732', 'name': 'first', 'value': 20, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}, {'month': 2, 'SE': [{'start': 1, 'end': 116, 'objects': [{'flag': 'add', 'type': 'months', 'ID': 'ID464732', 'name': 'first', 'value': 220, 'product': 'rpg', 'method': 'mete', 'start': 1, 'end': 2, 'date': 1111}]}]}]}, 'next': 'null'}}}}}"
        )

    def test_object_months_update(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.object(
                "month",
                2019,
                1,
                {"flag": "add", "type": "months", "ID": "ID22132", "name": "first", "value": -1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
                "update",
                5,
                6,
            ),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.object(
                "month",
                2020,
                8,
                {"flag": "add", "type": "months", "ID": "ID4140609502003290", "name": "first", "value": 15, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
                "update",
                0,
                6,
            ),
            True
        )

    def test_object_months_update_error(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.object(
                "month",
                2019,
                1,
                {"flag": "add", "type": "months", "ID": "ID2", "name": "first", "value": -1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
                "update",
                5,
                6,
            ),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.object(
                "month",
                2020,
                8,
                {"flag": "add", "type": "months", "ID": "ID41406090", "name": "first", "value": 15, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
                "update",
                0,
                6,
            ),
            False
        )

    def test_object_months_remove(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.object(
                "month",
                2019,
                1,
                {"flag": "add", "type": "months", "ID": "ID22132", "name": "first", "value": -1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
                "remove",
                5,
                6,
            ),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.object(
                "month",
                2020,
                8,
                {"flag": "add", "type": "months", "ID": "ID4140609502003290", "name": "first", "value": 15, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
                "remove",
                0,
                6,
            ),
            True
        )

    def test_object_months_remove_error(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.object(
                "month",
                2019,
                1,
                {"flag": "add", "type": "months", "ID": "ID2", "name": "first", "value": -1, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
                "remove",
                5,
                6,
            ),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.object(
                "month",
                2020,
                8,
                {"flag": "add", "type": "months", "ID": "ID41406090", "name": "first", "value": 15, "product": "rpg", "method": "mete", "start": 1, "end": 2, "date": 1111},
                "remove",
                0,
                6,
            ),
            False
        )

    def test_thisYearExist(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisYearExist(2020),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisYearExist(2019),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisYearExist(20),
            True
        )

    def test_thisYearExist_error(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisYearExist(111),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisYearExist(2741),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisYearExist(999),
            False
        )

    def test_thisMonthExist(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisMonthExist(2020, 8),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisMonthExist(2019, 1),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisMonthExist(20, 11),
            True
        )

    def test_thisMonthExist_error(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisMonthExist(2020, 11),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisMonthExist(2019, 5),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisMonthExist(20, 4),
            False
        )

    def test_thisSEExist(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisSEExist(2020, 8, 0, 6),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisSEExist(2019, 1, 5, 6),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisSEExist(20, 11, 11, 63),
            True
        )

    def test_thisSEExist_error(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisSEExist(2020, 8, 3, 6),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisSEExist(2019, 1, 7, 1),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.thisSEExist(20, 11, 1, 11),
            False
        )

    def test_addSE(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.addSE(
                2020,
                8,
                {
                    "start": 1,
                    "end": 11,
                    "objects": {}
                }
            ),
            True
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.addSE(
                20,
                11,
                {
                    "start": 7,
                    "end": 16,
                    "objects": {}
                }
            ),
            True
        )
    
    def test_addSE_error(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.addSE(
                2020,
                8,
                {
                    "start": 11,
                    "end": 1,
                    "objects": {}
                }
            ),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.addSE(
                20,
                11,
                {
                    "start": 7,
                    "objects": {}
                }
            ),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.addSE(
                20,
                11,
                {
                }
            ),
            False
        )

        self.assertEqual(
            self.TestMonthsCustomLinkedList.addSE(
                20,
                11,
                {
                    "start": 1,
                    "end": 2,
                }
             ),
            False
        )

    def test_sumAllYearsMonths(self):

        self.assertEqual(
            self.TestMonthsCustomLinkedList.sumAllYearsMonths(),
            288.0
        )

    def test_sumAllYearsInf(self):

        self.assertEqual(
            self.TestInfCustomLinkedList.sumAllYearsInf(),
            288.0
        )

    def test_toMonthsArray(self):

        tempCustomLinkedList = CustomLinkedListController(self.TestMonthsCustomLinkedList.search(2020,6,"month"))

        accounts = tempCustomLinkedList.toMonthsArray(2020, 6)

        valueTable = [
            {
                "year": 20,
                "start": 24005,
                "end": 36000,
                "value": 0
            },{
                "year": 2020,
                "start": 3,
                "end": 8,
                "value": 15
            },{
                "year": 2020,
                "start": 14,
                "end": 16,
                "value": -67
            },{
                "year": 2020,
                "start": 14,
                "end": 192,
                "value": 115
            },
        ]

        self.assertEqual(
            len(accounts),
            4
        )

        for index, account in enumerate(accounts):

            self.assertEqual(
                account["year"],
                valueTable[index]["year"]
            )
            self.assertEqual(
                account["start"],
                valueTable[index]["start"]
            )
            self.assertEqual(
                account["end"],
                valueTable[index]["end"]
            )
            self.assertEqual(
                account["value"],
                valueTable[index]["value"]
            )

    def test_toInfArray(self):

        tempCustomLinkedList = CustomLinkedListController(self.TestInfCustomLinkedList.search(2020,6,"inf"))

        accounts = tempCustomLinkedList.toInfArray(2020, 6)

        valueTable = [
            {
                "year": 20,
                "month": 11,
                "value": -20
            },{
                "year": 20,
                "month": 1,
                "value": 0
            },{
                "year": 2019,
                "month": 1,
                "value": -1
            },{
                "year": 2020,
                "month": 5,
                "value": 15
            },{
                "year": 2020,
                "month": 2,
                "value": -67
            },{
                "year": 2020,
                "month": 2,
                "value": 115
            },
        ]

        self.assertEqual(
            len(accounts),
            6
        )

        for index, account in enumerate(accounts):

            self.assertEqual(
                account["year"],
                valueTable[index]["year"]
            )

            self.assertEqual(
                account["month"],
                valueTable[index]["month"]
            )

            self.assertEqual(
                account["value"],
                valueTable[index]["value"]
            )

    def test_calcTheEvolution(self):

        querry = {
            "year": 3,
            "month": 7
        }

        target = {
            "year": 2,
            "month": 9,
            "start": 7,
            "end": 2,
        }

        self.assertEqual(
            self.TestMonthsCustomLinkedList.calcTheEvolution(
                querry["year"],
                querry["month"],
                target["year"],
                target["month"],
                target["start"],
                target["end"]
            )["start"],
            17
        )

        querry = {
            "year": 8,
            "month": 2
        }

        target = {
            "year": 2,
            "month": 1,
            "start":12,
            "end": 83,
        }

        self.assertEqual(
            self.TestMonthsCustomLinkedList.calcTheEvolution(
                querry["year"],
                querry["month"],
                target["year"],
                target["month"],
                target["start"],
                target["end"]
            )["start"],
            85
        )



if __name__ == '__main__':
    unittest.main()