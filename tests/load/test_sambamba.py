# -*- coding: utf-8 -*-

from __future__ import absolute_import

from chanjo.store import Store
from chanjo.load import sambamba as load_sambamba
from chanjo.parse import bed as parse_bed
from get_bedrows import get_bedlines

bed_lines = get_bedlines()


class TestSambamba:
    def setup(self):
        self.store = Store(':memory:')
        self.store.set_up()
        self.row_data = parse_bed.chanjo(bed_lines)

    def teardown(self):
        self.store.tear_down()
        self.store.session.close()

    def test_connection(self):
        self.store.dialect == 'sqlite'

    def test_rows(self):
        stats = load_sambamba.rows(self.store.session, self.row_data)
        all_stats = [stat for stat in stats]
        assert len(all_stats) == 4
